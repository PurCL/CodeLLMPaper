#!/usr/bin/env python3
"""
Fetch abstracts for NDSS papers from their individual web pages.

NDSS accepted-paper listing pages only contain titles and links — no inline
abstracts. This script reads the extracted JSON (from extract_papers.py),
visits each paper's URL on ndss-symposium.org, scrapes the abstract, and
writes out an updated JSON with abstracts filled in.

Usage:
    python fetch_ndss_abstracts.py /tmp/ndss_extracted.json -o /tmp/ndss_with_abstracts.json

    # Resume after interruption (skips papers already in output):
    python fetch_ndss_abstracts.py /tmp/ndss_extracted.json -o /tmp/ndss_with_abstracts.json --resume

Environment:
    Requires `requests` (pip install requests)
"""

import argparse
import json
import os
import re
import sys
import time

try:
    import requests
except ImportError:
    print("Error: pip install requests", file=sys.stderr)
    sys.exit(1)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def extract_abstract_from_html(html_text):
    """Extract abstract from an NDSS paper page.

    The page structure has the abstract in <p> tags after the author info
    and before resource links. We look for common patterns.
    """
    # Strategy 1: Look for explicit "Abstract" section
    # Some pages have <h2>Abstract</h2> or <strong>Abstract</strong>
    abstract_header = re.search(
        r'(?:<h[23][^>]*>\s*Abstract\s*</h[23]>|<strong>\s*Abstract\s*</strong>)',
        html_text, re.IGNORECASE
    )
    if abstract_header:
        after = html_text[abstract_header.end():]
        paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', after, re.DOTALL)
        abstract_parts = []
        for p in paragraphs:
            text = re.sub(r'<[^>]+>', '', p).strip()
            if not text:
                continue
            # Stop at resource links or other sections
            if re.match(r'^(Paper|Slides|Video|BibTeX|Citation|Presentation)\s*$', text, re.IGNORECASE):
                break
            if 'wp-content/uploads' in p:
                break
            abstract_parts.append(text)
            if len(' '.join(abstract_parts)) > 200:
                break
        if abstract_parts:
            return ' '.join(abstract_parts)

    # Strategy 2: Find the main content area and extract paragraphs
    # NDSS pages typically have: <article> or <div class="entry-content">
    content_match = re.search(
        r'<div class="entry-content">(.*?)</div>\s*(?:<div|<footer|</article)',
        html_text, re.DOTALL
    )
    if not content_match:
        content_match = re.search(
            r'<article[^>]*>(.*?)</article>',
            html_text, re.DOTALL
        )

    if content_match:
        content = content_match.group(1)
        paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', content, re.DOTALL)
        # Filter out short/irrelevant paragraphs (authors, links)
        candidates = []
        for p in paragraphs:
            text = re.sub(r'<[^>]+>', '', p).strip()
            text = re.sub(r'\s+', ' ', text)
            if len(text) < 80:
                continue
            if re.search(r'https?://\S+\.(pdf|pptx?|mp4)', text):
                continue
            candidates.append(text)
        if candidates:
            # The longest paragraph is usually the abstract
            return max(candidates, key=len)

    # Strategy 3: Just find the longest <p> on the page
    all_paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', html_text, re.DOTALL)
    candidates = []
    for p in all_paragraphs:
        text = re.sub(r'<[^>]+>', '', p).strip()
        text = re.sub(r'\s+', ' ', text)
        if len(text) >= 100:
            candidates.append(text)
    if candidates:
        return max(candidates, key=len)

    return ""


def fetch_abstract(url, timeout=15):
    """Fetch a single paper page and extract the abstract."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        resp.raise_for_status()
        return extract_abstract_from_html(resp.text)
    except Exception as e:
        print(f"    FETCH ERROR: {e}", file=sys.stderr)
        return ""


def main():
    parser = argparse.ArgumentParser(description="Fetch NDSS paper abstracts")
    parser.add_argument("input", help="Input JSON from extract_papers.py (NDSS)")
    parser.add_argument("-o", "--output", required=True, help="Output JSON path")
    parser.add_argument("--delay", type=float, default=1.0,
                        help="Delay between requests in seconds (default: 1.0)")
    parser.add_argument("--resume", action="store_true",
                        help="Resume: skip papers already in output file")
    args = parser.parse_args()

    with open(args.input) as f:
        papers = json.load(f)

    # Load existing output for resume
    existing = {}
    if args.resume and os.path.exists(args.output):
        with open(args.output) as f:
            existing = json.load(f)
        print(f"Resuming: {len(existing)} papers already processed", file=sys.stderr)

    result = dict(existing)
    total = len(papers)
    fetched = 0
    skipped = 0
    no_abstract = 0

    for i, (title, entry) in enumerate(papers.items()):
        if title in result and result[title].get("abstract", "").strip():
            skipped += 1
            continue

        url = entry.get("url", "")
        if not url:
            print(f"  [{i+1}/{total}] NO_URL: {title[:60]}", file=sys.stderr)
            result[title] = entry
            no_abstract += 1
            continue

        abstract = fetch_abstract(url)
        entry_copy = dict(entry)
        if abstract:
            entry_copy["abstract"] = abstract
            fetched += 1
            print(f"  [{i+1}/{total}] OK ({len(abstract)} chars): {title[:60]}", file=sys.stderr)
        else:
            no_abstract += 1
            print(f"  [{i+1}/{total}] NO_ABSTRACT: {title[:60]}", file=sys.stderr)

        result[title] = entry_copy

        # Save progress every 20 papers
        if (fetched + no_abstract) % 20 == 0:
            with open(args.output, "w") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

        if args.delay > 0:
            time.sleep(args.delay)

    # Final save
    with open(args.output, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\n=== FETCH COMPLETE ===", file=sys.stderr)
    print(f"  Total: {total}", file=sys.stderr)
    print(f"  Fetched: {fetched}", file=sys.stderr)
    print(f"  No abstract: {no_abstract}", file=sys.stderr)
    print(f"  Skipped (resume): {skipped}", file=sys.stderr)
    print(f"  Output: {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
