#!/usr/bin/env python3
"""
Merge newly labeled papers into data/labeldata/labeldata.json.

Usage:
    python merge_labeldata.py labeled.json [--labeldata PATH] [--dry-run]

    # Merge into default labeldata.json:
    python merge_labeldata.py labeled_ASE2025.json

    # Merge into a different file:
    python merge_labeldata.py labeled.json --labeldata data/labeldata/labeldata_v2.json

    # Dry-run (show stats without writing):
    python merge_labeldata.py labeled.json --dry-run
"""

import argparse
import json
import os
import sys

DEFAULT_LABELDATA = os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "..", "data", "labeldata", "labeldata.json"
)


def main():
    parser = argparse.ArgumentParser(description="Merge labeled papers into labeldata.json")
    parser.add_argument("input", help="Labeled JSON file to merge")
    parser.add_argument("--labeldata", default=DEFAULT_LABELDATA,
                        help="Path to labeldata.json (default: data/labeldata/labeldata.json)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show stats without writing")
    parser.add_argument("--no-overwrite", action="store_true",
                        help="Do not overwrite existing entries")
    args = parser.parse_args()

    # Load new papers
    with open(args.input) as f:
        new_papers = json.load(f)
    print(f"New papers to merge: {len(new_papers)}", file=sys.stderr)

    # Load existing labeldata
    if os.path.exists(args.labeldata):
        with open(args.labeldata) as f:
            existing = json.load(f)
        print(f"Existing papers in labeldata: {len(existing)}", file=sys.stderr)
    else:
        existing = {}
        print(f"Creating new labeldata at {args.labeldata}", file=sys.stderr)

    # Validate new papers have required fields
    valid = {}
    invalid = 0
    for title, entry in new_papers.items():
        if not entry.get("labels"):
            invalid += 1
            continue
        if not entry.get("abstract"):
            invalid += 1
            continue
        valid[title] = entry

    if invalid:
        print(f"Skipped {invalid} papers without labels or abstract", file=sys.stderr)

    # Merge
    added = 0
    updated = 0
    skipped = 0
    for title, entry in valid.items():
        if title in existing:
            if args.no_overwrite:
                skipped += 1
            else:
                existing[title] = entry
                updated += 1
        else:
            existing[title] = entry
            added += 1

    print(f"\nMerge summary:", file=sys.stderr)
    print(f"  Added:   {added}", file=sys.stderr)
    print(f"  Updated: {updated}", file=sys.stderr)
    print(f"  Skipped: {skipped}", file=sys.stderr)
    print(f"  Total:   {len(existing)}", file=sys.stderr)

    if args.dry_run:
        print("\n(dry-run, no file written)", file=sys.stderr)
        return

    # Write back
    os.makedirs(os.path.dirname(args.labeldata), exist_ok=True)
    with open(args.labeldata, "w") as f:
        json.dump(existing, f, indent=4, ensure_ascii=False)
    print(f"\nWritten to {args.labeldata}", file=sys.stderr)


if __name__ == "__main__":
    main()
