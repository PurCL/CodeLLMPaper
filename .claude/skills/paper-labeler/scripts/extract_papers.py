#!/usr/bin/env python3
"""
Extract papers (title + abstract + metadata) from rawdata files.

Supports:
  - .bib files (BibTeX with abstract field)
  - .html files from ACL Anthology (ACL, EMNLP, NAACL, etc.)
  - .html files from NDSS symposium

Usage:
    python extract_papers.py <input_path> [--venue VENUE] [--year YEAR]
    python extract_papers.py data/rawdata/2025/ASE2025.bib
    python extract_papers.py data/rawdata/2025/ACL2025.html --venue ACL --year 2025
    python extract_papers.py data/rawdata/2025/NDSS2025.html

Output: JSON to stdout, one object per paper with keys:
    type, key, author, booktitle, title, year, abstract, venue, url, ...
"""

import argparse
import json
import os
import re
import sys


def parse_bib(bibpath, venue=None, year=None):
    with open(bibpath, "r", errors="ignore") as f:
        bib_tex = f.read()

    if venue is None:
        venue = os.path.basename(bibpath).replace(".bib", "")
    if year is None:
        for part in bibpath.replace("\\", "/").split("/"):
            if re.match(r"^20\d{2}$", part):
                year = part
                break

    bib_tex = bib_tex.replace("{{", "{").replace("}}", "}")
    entries = {}

    for chunk in re.split(r"\n@", bib_tex):
        chunk = chunk.strip()
        if not chunk:
            continue
        if not chunk.startswith("@"):
            chunk = "@" + chunk

        m = re.match(r"@(\w+)\s*\{([^,]*),", chunk)
        if not m:
            continue

        entry = {
            "type": m.group(1).upper(),
            "key": m.group(2).strip(),
            "venue": venue,
        }

        for km in re.finditer(r"(\w+)\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}", chunk):
            entry[km.group(1).lower()] = km.group(2).strip()
        for km in re.finditer(r'(\w+)\s*=\s*"([^"]*)"', chunk):
            entry[km.group(1).lower()] = km.group(2).strip()

        if "title" not in entry or "abstract" not in entry:
            continue
        if not entry["abstract"].strip():
            continue

        if year and "year" not in entry:
            entry["year"] = year

        title = entry["title"]
        title = re.sub(r"\s+", " ", title).strip()
        entry["title"] = title

        abstract = entry["abstract"]
        abstract = re.sub(r"\s+", " ", abstract).strip()
        entry["abstract"] = abstract

        entries[title] = _normalize_entry(entry, venue)

    return entries


def parse_acl_html(htmlpath, venue=None, year=None):
    if venue is None:
        fname = os.path.basename(htmlpath).replace(".html", "")
        venue = re.sub(r"[-_]?(main|findings|short|long|demo|srw|industry)\d*", "", fname, flags=re.IGNORECASE)
        venue = re.sub(r"\d{4}$", "", venue)
    if year is None:
        for part in htmlpath.replace("\\", "/").split("/"):
            if re.match(r"^20\d{2}$", part):
                year = part
                break
        if year is None:
            m = re.search(r"(\d{4})", os.path.basename(htmlpath))
            if m:
                year = m.group(1)

    venue_label = os.path.basename(htmlpath).replace(".html", "")

    with open(htmlpath, "r", errors="ignore") as f:
        content = f.read()

    title_positions = [
        (m.start(), re.sub(r"<[^>]+>", "", m.group(2)).strip(), m.group(1).strip().strip("\"'"))
        for m in re.finditer(
            r'<strong><a class=align-middle href=([^\s>]+)[^>]*>(.*?)</a></strong>',
            content,
            re.DOTALL,
        )
    ]
    abstract_positions = [
        (m.start(), re.sub(r"<[^>]+>", "", m.group(1)).strip())
        for m in re.finditer(
            r'<div class="card-body p-3 small">(.*?)</div>', content, re.DOTALL
        )
    ]

    entries = {}
    ai = 0
    for ti in range(len(title_positions)):
        tpos, ttitle, turl = title_positions[ti]
        next_tpos = (
            title_positions[ti + 1][0]
            if ti + 1 < len(title_positions)
            else len(content)
        )

        while ai < len(abstract_positions) and abstract_positions[ai][0] < tpos:
            ai += 1
        if ai < len(abstract_positions) and abstract_positions[ai][0] < next_tpos:
            abstract = abstract_positions[ai][1]
            ai += 1
        else:
            continue

        if not abstract.strip() or not ttitle.strip():
            continue

        # Resolve relative ACL Anthology URLs
        paper_url = turl
        if paper_url and not paper_url.startswith("http"):
            paper_url = "https://aclanthology.org" + paper_url

        entries[ttitle] = _normalize_entry(
            {
                "type": "INPROCEEDINGS",
                "key": "",
                "author": "",
                "booktitle": venue_label,
                "title": ttitle,
                "year": year or "",
                "abstract": abstract,
                "url": paper_url,
                "venue": venue_label,
            },
            venue_label,
        )

    return entries


def parse_ndss_html(htmlpath, venue=None, year=None):
    """Parse NDSS HTML — extracts titles and links. Abstracts require fetching individual pages."""
    if venue is None:
        venue = os.path.basename(htmlpath).replace(".html", "")
    if year is None:
        m = re.search(r"(\d{4})", os.path.basename(htmlpath))
        if m:
            year = m.group(1)

    with open(htmlpath, "r", errors="ignore") as f:
        content = f.read()

    entries = {}

    # Two NDSS HTML formats:
    # Old: <h3 class="blog-post-title">...</h3> + <a class="paper-link-abs">
    # New (2026+): <h2 class="pt-cv-title"><a href="...">Title</a></h2>
    if "pt-cv-title" in content:
        ptcv_pattern = re.compile(
            r'<h2 class="pt-cv-title"><a href="([^"]*)"[^>]*>(.*?)</a></h2>',
            re.DOTALL,
        )
        for m in ptcv_pattern.finditer(content):
            url = m.group(1).strip()
            ttitle = re.sub(r"<[^>]+>", "", m.group(2)).strip()
            if not ttitle:
                continue
            entries[ttitle] = _normalize_entry(
                {
                    "type": "INPROCEEDINGS",
                    "key": "",
                    "author": "",
                    "booktitle": venue,
                    "title": ttitle,
                    "year": year or "",
                    "abstract": "",
                    "url": url,
                    "venue": venue,
                },
                venue,
            )
        return entries

    title_pattern = re.compile(
        r'<h3 class="blog-post-title">(.*?)</h3>', re.DOTALL
    )
    link_pattern = re.compile(
        r'<a class="paper-link-abs" href="([^"]+)"', re.DOTALL
    )

    titles = [(m.start(), m.group(1).strip()) for m in title_pattern.finditer(content)]
    links = [(m.start(), m.group(1).strip()) for m in link_pattern.finditer(content)]

    li = 0
    for ti in range(len(titles)):
        tpos, ttitle = titles[ti]
        next_tpos = titles[ti + 1][0] if ti + 1 < len(titles) else len(content)

        url = ""
        while li < len(links) and links[li][0] < tpos:
            li += 1
        if li < len(links) and links[li][0] < next_tpos:
            url = links[li][1]
            li += 1

        ttitle = re.sub(r"<[^>]+>", "", ttitle).strip()
        if ttitle.endswith("..."):
            ttitle = ttitle[:-3].strip()

        if not ttitle:
            continue

        entries[ttitle] = _normalize_entry(
            {
                "type": "INPROCEEDINGS",
                "key": "",
                "author": "",
                "booktitle": venue,
                "title": ttitle,
                "year": year or "",
                "abstract": "",  # NDSS abstracts need web fetch
                "url": url,
                "venue": venue,
            },
            venue,
        )

    return entries


def _normalize_entry(entry, venue):
    template = {
        "type": "",
        "key": "",
        "author": "",
        "booktitle": "",
        "title": "",
        "year": "",
        "volume": "",
        "number": "",
        "pages": "",
        "abstract": "",
        "keywords": "",
        "url": "",
        "doi": "",
        "ISSN": "",
        "month": "",
        "venue": venue,
    }
    for k in template:
        if k in entry:
            template[k] = entry[k]
    # Auto-construct URL from DOI if URL is empty
    if not template["url"].strip() and template["doi"].strip():
        doi = template["doi"].strip()
        if not doi.startswith("http"):
            doi = "https://doi.org/" + doi
        template["url"] = doi
    return template


def detect_format(filepath):
    if filepath.endswith(".bib"):
        return "bib"
    if filepath.endswith(".html"):
        with open(filepath, "r", errors="ignore") as f:
            content = f.read()
        fname_lower = os.path.basename(filepath).lower()
        if "ndss" in fname_lower or "ndss-symposium" in content[:50000].lower():
            if "paper-link-abs" in content or "blog-post-title" in content or "pt-cv-title" in content:
                return "ndss"
        if "aclanthology" in content[:10000].lower() or "acl anthology" in content[:10000].lower():
            return "acl"
        if "align-middle" in content[:50000] and "card-body p-3 small" in content[:50000]:
            return "acl"
        return "unknown"
    return "unknown"


def main():
    parser = argparse.ArgumentParser(description="Extract papers from rawdata files")
    parser.add_argument("input", help="Path to .bib or .html file")
    parser.add_argument("--venue", help="Venue name override")
    parser.add_argument("--year", help="Year override")
    parser.add_argument("--format", choices=["bib", "acl", "ndss", "auto"], default="auto",
                        help="Input format (default: auto-detect)")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: {args.input} not found", file=sys.stderr)
        sys.exit(1)

    fmt = args.format
    if fmt == "auto":
        fmt = detect_format(args.input)
        if fmt == "unknown":
            print(f"Error: cannot detect format of {args.input}", file=sys.stderr)
            sys.exit(1)

    if fmt == "bib":
        entries = parse_bib(args.input, venue=args.venue, year=args.year)
    elif fmt == "acl":
        entries = parse_acl_html(args.input, venue=args.venue, year=args.year)
    elif fmt == "ndss":
        entries = parse_ndss_html(args.input, venue=args.venue, year=args.year)
    else:
        print(f"Error: unsupported format {fmt}", file=sys.stderr)
        sys.exit(1)

    print(f"Extracted {len(entries)} papers from {args.input} (format: {fmt})", file=sys.stderr)
    json.dump(entries, sys.stdout, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
