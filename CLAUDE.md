# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Repository Purpose

A curated literature database of ~1,663 research papers on Agentic Software Engineering (LLMs/AI agents for code), systematically collected from top-tier venues in SE, PL, Security, and NLP. Hosted at [PurCL/ASE](https://github.com/PurCL/ASE).

There is no build system. All processing is handled by the **paper-labeler** skill in `.claude/skills/paper-labeler/`.

## Repository Structure

```
data/
  labeldata/labeldata.json   — canonical paper database (~1,663 entries)
  venues.json                — sorted array of processed venue names
  rawdata/<year>/<VENUE>.ext — raw proceedings files (.bib, .html)
  rawdata/original.json      — legacy data, already migrated
web/
  index.html                 — generated single-page website
  image.png                  — website demo screenshot
.claude/skills/paper-labeler/
  SKILL.md                   — skill definition with full taxonomy
  USAGE.md                   — user guide
  scripts/                   — all pipeline scripts
.gitignore
CLAUDE.md
README.md
```

Legacy files (`src/`, `data/papers/`, `data/category.json`, `data/template.txt`, `data/labeldata/patch/`, `data/labeldata/extract.py`) are still tracked in git history but deleted from disk. They will be removed from tracking in a future commit.

## Data Schema

Each paper in `data/labeldata/labeldata.json`:

```json
{
  "Paper Title": {
    "type": "INPROCEEDINGS",
    "key": "unique-id",
    "author": "...",
    "booktitle": "...",
    "title": "Paper Title",
    "year": "2025",
    "abstract": "...",
    "url": "https://doi.org/...",
    "labels": ["Static Analysis", "Bug Detection"],
    "venue": "ASE2025"
  }
}
```

## Label Taxonomy

Two-level taxonomy, 9 top-level categories, 47 sub-categories. Labels stored as a flat list. Three super-groups on the website:

**Agent for SE** — Code Generation, Static Analysis, Dynamic Analysis, Code Model, Other SE Tasks

**Agent Design and Analysis** — Agent Design, Model Safety and Security, Agent Safety and Security

**Evaluation** — Evaluation (Benchmark, Empirical Study, Survey)

Full taxonomy with sub-level definitions: `.claude/skills/paper-labeler/SKILL.md`.

## Paper-Labeler Pipeline

All scripts in `.claude/skills/paper-labeler/scripts/`:

| Script | Purpose |
|--------|---------|
| `process_folder.py` | Batch mode: scan folder, skip processed venues, run full pipeline |
| `extract_papers.py` | Parse .bib/.html into uniform JSON |
| `fetch_ndss_abstracts.py` | Scrape abstracts from NDSS paper pages |
| `label_papers.py` | Keyword filter + Claude API labeling via AWS Bedrock |
| `merge_labeldata.py` | Merge labeled JSON into labeldata.json |
| `build_site.py` | Regenerate web/index.html from labeldata.json |
| `import_original.py` | One-time import of legacy papers from original.json |

### Batch Mode (recommended)

```bash
python .claude/skills/paper-labeler/scripts/process_folder.py --dry-run
python .claude/skills/paper-labeler/scripts/process_folder.py
python .claude/skills/paper-labeler/scripts/process_folder.py data/rawdata/2025/
```

### Manual Per-Venue Pipeline

```bash
# 1. Extract
python .claude/skills/paper-labeler/scripts/extract_papers.py data/rawdata/2025/ASE2025.bib > /tmp/extracted.json
# 1b. NDSS only: fetch abstracts
python .claude/skills/paper-labeler/scripts/fetch_ndss_abstracts.py /tmp/ndss_raw.json -o /tmp/extracted.json
# 2. Filter + label (requires AWS credentials)
python .claude/skills/paper-labeler/scripts/label_papers.py /tmp/extracted.json --phase all -o /tmp/labeled.json
# 3. Merge
python .claude/skills/paper-labeler/scripts/merge_labeldata.py /tmp/labeled.json
# 4. Rebuild website
python .claude/skills/paper-labeler/scripts/build_site.py
```

### Prerequisites

- Python 3.9+
- `boto3` (Claude API labeling via AWS Bedrock)
- `requests` (NDSS abstract fetching)
- AWS credentials configured

### Supported Input Formats

| Format | Extension | Abstracts |
|--------|-----------|-----------|
| BibTeX | `.bib` | Inline |
| ACL Anthology HTML | `.html` | Inline |
| NDSS HTML | `.html` | Scraped via `fetch_ndss_abstracts.py` |

## Contribution Workflow

To add a new venue:
1. Place `.bib` or `.html` file into `data/rawdata/<year>/`
2. Run `python .claude/skills/paper-labeler/scripts/process_folder.py`
3. Verify on website, then commit

To add individual papers: append to `data/labeldata/labeldata.json`, then run `build_site.py`.

To extend the taxonomy: edit `TAXONOMY` in `label_papers.py` and `build_site.py`, update `.claude/skills/paper-labeler/SKILL.md`, then rebuild.
