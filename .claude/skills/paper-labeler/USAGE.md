# Paper Labeler — User Guide

## Overview

Paper Labeler is a multi-step pipeline that extracts papers from conference rawdata files, filters for LLM-for-code relevance, and classifies them using a two-level label taxonomy.

```
rawdata (.bib / .html)
    │
    ▼  extract_papers.py
extracted.json (all papers with title + abstract + metadata)
    │
    ▼  label_papers.py --phase filter
filtered.json (candidate papers after keyword filtering)
    │
    ▼  label_papers.py --phase label
labeled.json (papers labeled by Claude API, with labels field)
    │
    ▼  merge_labeldata.py
data/labeldata/labeldata.json (merged into main database)
    │
    ▼  build_site.py
web/index.html (website regenerated)
```

## Prerequisites

- Python 3.9+
- `boto3` Python package (required for Phase 2): `pip install boto3`
- `requests` Python package (required for NDSS abstract fetching): `pip install requests`
- AWS credentials configured (required for Phase 2): `~/.aws/credentials`, env vars, or IAM role

## Supported Input Formats

| Format | File Type | Example Venues | Has Abstract |
|--------|-----------|----------------|--------------|
| BibTeX | `.bib` | ASE, ICSE, FSE, ISSTA, CCS, S&P, OOPSLA, PLDI, POPL, TOSEM, TSE, USENIXSec, NAACL | Yes |
| ACL Anthology HTML | `.html` | ACL, EMNLP, NAACL (some years) | Yes (inline in HTML) |
| NDSS HTML | `.html` | NDSS | No (titles and links only) |

## Quick Start: Batch Mode

The simplest way to process new data — scan a folder, skip already-processed venues, and
run the full pipeline for each new one:

```bash
# See what's new
python .claude/skills/paper-labeler/scripts/process_folder.py --dry-run

# Process all new venues in data/rawdata/
python .claude/skills/paper-labeler/scripts/process_folder.py

# Process a specific year only
python .claude/skills/paper-labeler/scripts/process_folder.py data/rawdata/2025/
```

The script checks `data/venues.json` to know which venues have been processed. After each
successful venue, it updates `venues.json` and at the end rebuilds the website.

Options:
- `--dry-run` — list new vs. already-processed venues
- `--filter-only` — keyword filter only, no API calls or merge
- `--model`, `--region`, `--delay` — Bedrock API options
- `--no-rebuild` — skip website rebuild

## Manual Steps (per-venue)

### 1. Extract Papers

```bash
# BibTeX files (most common)
python .claude/skills/paper-labeler/scripts/extract_papers.py \
    data/rawdata/2025/ASE2025.bib > /tmp/extracted.json

# ACL Anthology HTML
python .claude/skills/paper-labeler/scripts/extract_papers.py \
    data/rawdata/2025/ACL2025.html > /tmp/extracted.json

# NDSS HTML (titles only, abstracts are empty)
python .claude/skills/paper-labeler/scripts/extract_papers.py \
    data/rawdata/2025/NDSS2025.html > /tmp/extracted.json
```

**Options:**
- `--venue NAME` — manually specify venue name (default: inferred from filename)
- `--year YEAR` — manually specify year (default: inferred from path)
- `--format bib|acl|ndss` — manually specify format (default: auto-detect)

**NDSS special handling:** NDSS HTML pages only contain titles and paper links, no inline abstracts. After extraction, use `fetch_ndss_abstracts.py` to scrape abstracts from individual paper pages:

```bash
python .claude/skills/paper-labeler/scripts/extract_papers.py \
    data/rawdata/2025/NDSS2025.html > /tmp/ndss_extracted.json
python .claude/skills/paper-labeler/scripts/fetch_ndss_abstracts.py \
    /tmp/ndss_extracted.json -o /tmp/extracted.json
```

Options:
- `--delay SECONDS` — delay between HTTP requests (default: 1.0s, to avoid rate limiting)
- `--resume` — resume mode, skip papers already in the output file (for resuming after interruption)

### 2. Filter and Label

**Phase 1 — Keyword filter (no API needed):**

```bash
python .claude/skills/paper-labeler/scripts/label_papers.py \
    /tmp/extracted.json --phase filter -o /tmp/filtered.json
```

Filter logic: a paper's title + abstract must contain both:
- **LLM-related keywords**: large language model, llm, gpt, codex, prompt, few-shot, ...
- **Code-related keywords**: code, program, software, bug, vulnerability, testing, verification, ...

This filter is conservative (high recall) — it prefers false positives over missed papers.

**Phase 2 — Claude labeling (via AWS Bedrock, requires AWS credentials):**

```bash
python .claude/skills/paper-labeler/scripts/label_papers.py \
    /tmp/filtered.json --phase label -o /tmp/labeled.json
```

**Run both phases together:**

```bash
python .claude/skills/paper-labeler/scripts/label_papers.py \
    /tmp/extracted.json --phase all -o /tmp/labeled.json
```

**Options:**
- `--phase filter|label|all` — which phase to run (default: all)
- `--model MODEL` — Bedrock model ID (default: us.anthropic.claude-sonnet-4-6)
- `--region REGION` — AWS region (default: us-east-1)
- `--delay SECONDS` — delay between API calls (default: 0.5s)
- `--dry-run` — preview mode, no API calls

**API usage estimate:** ~1 API call per paper, ~500-1500 input tokens, ~50-100 output tokens.

### 3. Merge into labeldata

```bash
# Preview first
python .claude/skills/paper-labeler/scripts/merge_labeldata.py \
    /tmp/labeled.json --dry-run

# Merge
python .claude/skills/paper-labeler/scripts/merge_labeldata.py \
    /tmp/labeled.json
```

**Options:**
- `--dry-run` — show merge stats without writing
- `--no-overwrite` — skip papers already in labeldata.json
- `--labeldata PATH` — write to a different JSON file

### 4. Rebuild Website

After merging, rebuild the website:

```bash
python .claude/skills/paper-labeler/scripts/build_site.py
```

Output: `web/index.html` — a single-page app with category sidebar (grouped into three super-groups: Agent for SE, Agent Design and Analysis, Evaluation), search, year/venue filters, clickable label pills, and expandable abstracts.

## Label Taxonomy

Two-level taxonomy. A paper can belong to multiple categories.

### Top-Level Categories

| # | Category | Description |
|---|----------|-------------|
| 1 | Code Generation | Synthesis, completion, repair, translation, decompilation, refactoring |
| 2 | Static Analysis | Bug detection, verification, type inference, data-flow analysis, etc. |
| 3 | Dynamic Analysis | Test generation, fuzzing, debugging, mutation testing, etc. |
| 4 | Model Safety and Security | Adversarial attacks, backdoors, memorization, watermarking, jailbreaking |
| 5 | Agent Safety and Security | Prompt injection, agent defense, access control |
| 6 | Agent Design | Planning, memory management, tool use, multi-agent |
| 7 | Code Model | Model training, binary/IR models |
| 8 | Other SE Tasks | Code review, documentation generation, log analysis |
| 9 | Evaluation | Benchmarks, empirical studies, surveys |

### Sub-Level Categories

See the taxonomy section in `.claude/skills/paper-labeler/SKILL.md` for the full sub-level definitions.

### Labels Field Format

Each paper's `labels` field is a flat list containing both top-level and sub-level labels:

```json
"labels": ["Static Analysis", "Bug Detection", "Evaluation", "Benchmark"]
```

## Full Example

### Process ASE 2025

```bash
# Step 1: Extract
python .claude/skills/paper-labeler/scripts/extract_papers.py \
    data/rawdata/2025/ASE2025.bib > /tmp/ase2025_extracted.json

# Step 2: Filter + Label (requires AWS credentials)
python .claude/skills/paper-labeler/scripts/label_papers.py \
    /tmp/ase2025_extracted.json --phase all -o /tmp/ase2025_labeled.json

# Step 3: Preview merge
python .claude/skills/paper-labeler/scripts/merge_labeldata.py \
    /tmp/ase2025_labeled.json --dry-run

# Step 4: Merge
python .claude/skills/paper-labeler/scripts/merge_labeldata.py \
    /tmp/ase2025_labeled.json

# Step 5: Rebuild website
python .claude/skills/paper-labeler/scripts/build_site.py
```

### Keyword Filter Only (no API calls)

```bash
python .claude/skills/paper-labeler/scripts/extract_papers.py \
    data/rawdata/2025/CCS2025.bib > /tmp/ccs_extracted.json

python .claude/skills/paper-labeler/scripts/label_papers.py \
    /tmp/ccs_extracted.json --phase filter -o /tmp/ccs_filtered.json

# Check how many candidate papers
python -c "import json; d=json.load(open('/tmp/ccs_filtered.json')); print(len(d))"
```

### Using via Claude Code

In Claude Code, simply say:

- "process the ASE2025 rawdata"
- "label the papers in data/rawdata/2025/CCS2025.bib"
- "extract and classify EMNLP2025 papers"
- "process the 2025 folder" — runs batch mode for data/rawdata/2025/
- "process all new venues" — runs batch mode for all of data/rawdata/

Claude Code will automatically invoke the paper-labeler skill to run the pipeline.

## File Structure

```
.claude/skills/paper-labeler/
├── SKILL.md                          # Skill definition (read by Claude Code)
├── USAGE.md                          # This user guide
└── scripts/
    ├── process_folder.py             # Batch mode: process all new venues in a folder
    ├── extract_papers.py             # Step 1: Extract papers
    ├── fetch_ndss_abstracts.py       # Step 1b: Fetch NDSS paper abstracts
    ├── label_papers.py               # Step 2: Filter + Label
    ├── merge_labeldata.py            # Step 3: Merge into labeldata
    ├── build_site.py                 # Step 4: Rebuild website
    └── import_original.py            # Import legacy papers from original.json
```

## FAQ

**Q: NLP venues (ACL/EMNLP) produce too many irrelevant papers?**
A: NLP venue papers almost all mention "language model", so keyword filtering has high recall but lower precision. Phase 2 Claude labeling further filters out irrelevant papers — if a paper is not about LLM-for-code, Claude returns NOT_RELEVANT.

**Q: NDSS papers have no abstract?**
A: NDSS HTML pages only list titles and links. Run `fetch_ndss_abstracts.py` to automatically scrape abstracts from individual paper pages. Supports `--resume` for resuming after interruption.

**Q: Approximate API cost?**
A: Example with ASE2025: 388 raw papers -> 229 after filtering -> ~229 API calls. Uses Claude Sonnet 4.6 via Bedrock; cost depends on AWS pricing.

**Q: How to modify the label taxonomy?**
A: Update the `TAXONOMY` dict in both `label_papers.py` and `build_site.py`, update the taxonomy section in `SKILL.md`, then run `python .claude/skills/paper-labeler/scripts/build_site.py` to rebuild the website.
