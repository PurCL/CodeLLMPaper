#!/usr/bin/env python3
"""
Process all unprocessed venues in a rawdata folder.

Scans a directory (or all of data/rawdata/) for .bib and .html files,
checks each venue against data/venues.json, and runs the full pipeline
(extract -> fetch NDSS abstracts -> filter+label -> merge) for new venues.

Usage:
    # Process all unprocessed venues under data/rawdata/
    python process_folder.py

    # Process a specific year folder
    python process_folder.py data/rawdata/2025/

    # Dry-run: show which venues would be processed
    python process_folder.py --dry-run

    # Filter only (no API calls, no merge)
    python process_folder.py --filter-only
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR))))
VENUES_PATH = os.path.join(REPO_ROOT, "data", "venues.json")
RAWDATA_DIR = os.path.join(REPO_ROOT, "data", "rawdata")


def canonical_venue(filename):
    """Derive canonical venue name from a rawdata filename.

    Examples:
        ASE2025.bib          -> ASE2025
        EMNLP-findings2024.html -> EMNLP2024
        EMNLP-main2024.html  -> EMNLP2024
        NDSS2025.html        -> NDSS2025
        S&P2024.bib          -> S&P2024
    """
    name = os.path.basename(filename)
    name = re.sub(r"\.(bib|html)$", "", name)
    # Strip track suffixes like -findings, -main, etc. but preserve the year
    name = re.sub(
        r"[-_]?(main|findings|short|long|demo|srw|industry)",
        "", name, flags=re.IGNORECASE,
    )
    # Collapse any leftover separators before the year
    name = re.sub(r"[-_]+(\d{4})", r"\1", name)
    return name


def detect_ndss(filepath):
    if not filepath.endswith(".html"):
        return False
    return "ndss" in os.path.basename(filepath).lower()


def load_venues():
    if os.path.exists(VENUES_PATH):
        with open(VENUES_PATH) as f:
            return set(json.load(f))
    return set()


def save_venues(venues):
    with open(VENUES_PATH, "w") as f:
        json.dump(sorted(venues), f, indent=2, ensure_ascii=False)


def find_rawdata_files(directory):
    files = []
    for root, _, fnames in os.walk(directory):
        for fname in sorted(fnames):
            if fname.endswith(".bib") or fname.endswith(".html"):
                files.append(os.path.join(root, fname))
    return sorted(files)


def group_by_venue(files):
    groups = {}
    for f in files:
        venue = canonical_venue(f)
        groups.setdefault(venue, []).append(f)
    return groups


def run_script(script_name, args, capture_stdout=False):
    cmd = [sys.executable, os.path.join(SCRIPT_DIR, script_name)] + args
    print(f"  $ python .../{script_name} {' '.join(args)}", file=sys.stderr)
    if capture_stdout:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"    ERROR: {result.stderr[-500:]}", file=sys.stderr)
            return False, ""
        if result.stderr:
            print(result.stderr, file=sys.stderr, end="")
        return True, result.stdout
    else:
        result = subprocess.run(cmd, stderr=sys.stderr)
        return result.returncode == 0, ""


def process_venue(venue, files, model, region, delay, filter_only=False):
    tmpdir = tempfile.mkdtemp(prefix=f"labeler_{venue}_")
    all_extracted = {}
    has_ndss = False

    for filepath in files:
        is_ndss = detect_ndss(filepath)
        print(f"\n  Extracting {os.path.basename(filepath)}...", file=sys.stderr)

        ok, stdout = run_script("extract_papers.py", [filepath], capture_stdout=True)
        if not ok:
            print(f"    FAILED to extract {os.path.basename(filepath)}", file=sys.stderr)
            continue

        try:
            entries = json.loads(stdout)
            all_extracted.update(entries)
            if is_ndss:
                has_ndss = True
        except json.JSONDecodeError:
            print(f"    FAILED to parse output for {os.path.basename(filepath)}", file=sys.stderr)

    if not all_extracted:
        print(f"  No papers extracted for {venue}", file=sys.stderr)
        return False

    print(f"\n  Total extracted: {len(all_extracted)} papers", file=sys.stderr)

    extracted_path = os.path.join(tmpdir, "extracted.json")

    if has_ndss:
        ndss_raw = os.path.join(tmpdir, "ndss_raw.json")
        with open(ndss_raw, "w") as f:
            json.dump(all_extracted, f, indent=2, ensure_ascii=False)
        print(f"\n  Fetching NDSS abstracts...", file=sys.stderr)
        ok, _ = run_script("fetch_ndss_abstracts.py", [ndss_raw, "-o", extracted_path])
        if not ok:
            print(f"    WARN: abstract fetch failed, continuing without", file=sys.stderr)
            with open(extracted_path, "w") as f:
                json.dump(all_extracted, f, indent=2, ensure_ascii=False)
    else:
        with open(extracted_path, "w") as f:
            json.dump(all_extracted, f, indent=2, ensure_ascii=False)

    labeled_path = os.path.join(tmpdir, "labeled.json")

    if filter_only:
        phase_args = ["--phase", "filter"]
    else:
        phase_args = [
            "--phase", "all",
            "--model", model, "--region", region, "--delay", str(delay),
        ]

    ok, _ = run_script("label_papers.py", [extracted_path] + phase_args + ["-o", labeled_path])
    if not ok:
        print(f"    FAILED to label {venue}", file=sys.stderr)
        return False

    with open(labeled_path) as f:
        labeled = json.load(f)

    if not labeled:
        print(f"  No relevant papers found for {venue}", file=sys.stderr)
        return True

    print(f"  Labeled {len(labeled)} relevant papers", file=sys.stderr)

    if not filter_only:
        ok, _ = run_script("merge_labeldata.py", [labeled_path])
        if not ok:
            print(f"    FAILED to merge {venue}", file=sys.stderr)
            return False

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Process unprocessed venues from a rawdata folder"
    )
    parser.add_argument(
        "directory", nargs="?", default=None,
        help="Directory to scan (default: all of data/rawdata/)",
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Show which venues would be processed, no action")
    parser.add_argument("--filter-only", action="store_true",
                        help="Keyword filter only, no API calls or merge")
    parser.add_argument("--model", default="us.anthropic.claude-sonnet-4-6")
    parser.add_argument("--region", default="us-east-1")
    parser.add_argument("--delay", type=float, default=0.5)
    parser.add_argument("--no-rebuild", action="store_true",
                        help="Skip website rebuild after processing")
    args = parser.parse_args()

    scan_dir = args.directory or RAWDATA_DIR
    if not os.path.isdir(scan_dir):
        print(f"Error: {scan_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    processed_venues = load_venues()
    print(f"Already processed: {len(processed_venues)} venues", file=sys.stderr)

    files = find_rawdata_files(scan_dir)
    venue_groups = group_by_venue(files)
    print(f"Found {len(venue_groups)} venues in {scan_dir}", file=sys.stderr)

    new_venues = {v: fs for v, fs in venue_groups.items() if v not in processed_venues}
    skip_venues = {v: fs for v, fs in venue_groups.items() if v in processed_venues}

    if skip_venues:
        print(f"\nSkipping {len(skip_venues)} already-processed venues:", file=sys.stderr)
        for v in sorted(skip_venues):
            print(f"  [done] {v}", file=sys.stderr)

    if not new_venues:
        print(f"\nNo new venues to process.", file=sys.stderr)
        return

    print(f"\nNew venues to process: {len(new_venues)}", file=sys.stderr)
    for v in sorted(new_venues):
        fnames = [os.path.basename(f) for f in new_venues[v]]
        print(f"  -> {v}: {fnames}", file=sys.stderr)

    if args.dry_run:
        print(f"\n(dry-run, nothing processed)", file=sys.stderr)
        return

    succeeded = []
    failed = []

    for venue in sorted(new_venues):
        print(f"\n{'='*60}", file=sys.stderr)
        print(f"Processing {venue}...", file=sys.stderr)
        print(f"{'='*60}", file=sys.stderr)

        ok = process_venue(
            venue, new_venues[venue],
            model=args.model, region=args.region, delay=args.delay,
            filter_only=args.filter_only,
        )
        if ok:
            succeeded.append(venue)
            if not args.filter_only:
                processed_venues.add(venue)
                save_venues(processed_venues)
            print(f"\n  [OK] {venue}", file=sys.stderr)
        else:
            failed.append(venue)
            print(f"\n  [FAIL] {venue}", file=sys.stderr)

    if succeeded and not args.filter_only and not args.no_rebuild:
        print(f"\nRebuilding website...", file=sys.stderr)
        run_script("build_site.py", [])

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"SUMMARY", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)
    print(f"  Succeeded: {len(succeeded)}", file=sys.stderr)
    for v in succeeded:
        print(f"    [OK] {v}", file=sys.stderr)
    if failed:
        print(f"  Failed: {len(failed)}", file=sys.stderr)
        for v in failed:
            print(f"    [FAIL] {v}", file=sys.stderr)


if __name__ == "__main__":
    main()
