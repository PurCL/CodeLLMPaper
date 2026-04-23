#!/usr/bin/env python3
"""
Build the single-page paper browser website.

Reads data/labeldata/labeldata.json and produces web/index.html
with all paper data embedded inline.

Usage:
    python src/build_site.py
"""

import json
import os
import html

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
DATA_PATH = os.path.join(REPO_ROOT, "data", "labeldata", "labeldata.json")
OUTPUT_PATH = os.path.join(REPO_ROOT, "web", "index.html")

# The two-level taxonomy
TAXONOMY = {
    "Code Generation": [
        "Program Synthesis", "Code Completion", "Program Repair",
        "Code Translation", "Decompilation", "Refactoring"
    ],
    "Static Analysis": [
        "Bug Detection", "Program Verification", "Specification Inference",
        "Pointer Analysis", "Call Graph Analysis", "Type Inference",
        "Data-flow Analysis", "Taint Analysis", "Symbolic Execution",
        "Abstract Interpretation", "Code Summarization", "Code Search",
        "Clone Detection"
    ],
    "Dynamic Analysis": [
        "Test Case Generation", "Test Oracle", "Fuzzing",
        "Debugging", "Mutation Testing", "Bug Reproduction",
        "Domain-Specific Testing", "PoC and Exploit Generation"
    ],
    "Model Safety and Security": [
        "Adversarial Attack", "Backdoor Detection", "Memorization",
        "Secure Code Generation", "Watermarking", "Jailbreaking"
    ],
    "Agent Safety and Security": [
        "Prompt Injection", "Agent Defense", "Access Control"
    ],
    "Agent Design": [
        "Planning", "Memory Management", "Tool Use", "Multi-Agent"
    ],
    "Code Model": [
        "Model Training", "Binary and IR Model"
    ],
    "Other SE Tasks": [
        "Code Review", "Doc/Comment/Commit Message Generation", "Log Analysis"
    ],
    "Evaluation": [
        "Benchmark", "Empirical Study", "Survey"
    ],
}

SUPER_GROUPS = [
    ("Agent for SE", [
        "Code Generation", "Static Analysis", "Dynamic Analysis",
        "Code Model", "Other SE Tasks"
    ]),
    ("Agent Design and Analysis", [
        "Model Safety and Security", "Agent Safety and Security", "Agent Design"
    ]),
    ("Evaluation", ["Evaluation"]),
]


def build_compact_papers(data):
    """Build a compact array of paper objects for embedding."""
    papers = []
    for title, entry in data.items():
        paper = {
            "t": entry.get("title", title),
            "a": entry.get("abstract", ""),
            "au": entry.get("author", ""),
            "y": entry.get("year", ""),
            "v": entry.get("venue", ""),
            "u": entry.get("url", ""),
            "l": entry.get("labels", []),
        }
        papers.append(paper)
    return papers


def compute_stats(papers):
    """Compute counts for categories, venues, and years."""
    cat_counts = {}  # label -> count
    venue_counts = {}
    year_counts = {}

    for p in papers:
        for label in p["l"]:
            cat_counts[label] = cat_counts.get(label, 0) + 1
        v = p["v"]
        venue_counts[v] = venue_counts.get(v, 0) + 1
        y = p["y"]
        year_counts[y] = year_counts.get(y, 0) + 1

    return cat_counts, venue_counts, year_counts


def _venue_base(v):
    """Strip year and track suffixes, e.g. 'EMNLP-findings2024' -> 'EMNLP'."""
    import re
    v = re.sub(r'\d{4}$', '', v)          # strip trailing year
    v = re.sub(r'-(findings|main)$', '', v, flags=re.IGNORECASE)
    return v


def generate_html(papers, cat_counts, venue_counts, year_counts):
    import re
    total = len(papers)
    venues_sorted = sorted(venue_counts.keys())
    years_sorted = sorted(year_counts.keys())

    # Build unique base venue names sorted, with aggregate counts
    base_venue_counts = {}
    for v, cnt in venue_counts.items():
        base = _venue_base(v)
        base_venue_counts[base] = base_venue_counts.get(base, 0) + cnt
    base_venues_sorted = sorted(base_venue_counts.keys())

    taxonomy_json = json.dumps(TAXONOMY)
    cat_counts_json = json.dumps(cat_counts)
    papers_json = json.dumps(papers, ensure_ascii=False)
    super_groups_json = json.dumps(SUPER_GROUPS)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Agentic Software Engineering (ASE)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
/* ============ RESET & BASE ============ */
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ font-size: 15px; }}
body {{
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: #f5f6f8;
  color: #1a1a2e;
  line-height: 1.55;
  overflow-x: hidden;
}}
a {{ color: inherit; text-decoration: none; }}

/* ============ COLOR PALETTE ============ */
:root {{
  --c0: #3b82f6; /* Code Generation - blue */
  --c1: #8b5cf6; /* Static Analysis - purple */
  --c2: #06b6d4; /* Dynamic Analysis - cyan */
  --c3: #ef4444; /* Model Safety - red */
  --c4: #f97316; /* Agent Safety - orange */
  --c5: #10b981; /* Agent Design - green */
  --c6: #6366f1; /* Code Model - indigo */
  --c7: #ec4899; /* Other SE Tasks - pink */
  --c8: #eab308; /* Evaluation - yellow */
  --sidebar-w: 290px;
  --header-h: 64px;
}}

/* ============ HEADER ============ */
.header {{
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  height: var(--header-h);
  background: #fff;
  border-bottom: 1px solid #e2e4e9;
  display: flex; align-items: center;
  padding: 0 24px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}}
.header-title {{
  font-size: 1.25rem; font-weight: 700; color: #1a1a2e;
  white-space: nowrap;
}}
.header-title span {{ color: #3b82f6; }}
.header-count {{
  margin-left: 14px;
  font-size: 0.82rem; color: #6b7280; font-weight: 400;
}}
.header-desc {{
  margin-left: auto;
  font-size: 0.78rem; color: #9ca3af;
  display: none;
}}
.mobile-toggle {{
  display: none;
  background: none; border: none; cursor: pointer;
  margin-right: 12px; padding: 4px;
}}
.mobile-toggle span {{
  display: block; width: 20px; height: 2px;
  background: #374151; margin: 4px 0;
  transition: 0.2s;
}}

@media (min-width: 900px) {{
  .header-desc {{ display: block; }}
}}

/* ============ LAYOUT ============ */
.layout {{
  display: flex;
  margin-top: var(--header-h);
  min-height: calc(100vh - var(--header-h));
}}

/* ============ SIDEBAR ============ */
.sidebar {{
  width: var(--sidebar-w);
  min-width: var(--sidebar-w);
  background: #fff;
  border-right: 1px solid #e2e4e9;
  position: fixed;
  top: var(--header-h);
  bottom: 0;
  left: 0;
  overflow-y: auto;
  padding: 16px 0;
  z-index: 90;
  transition: transform 0.25s ease;
}}
.sidebar::-webkit-scrollbar {{ width: 5px; }}
.sidebar::-webkit-scrollbar-thumb {{ background: #d1d5db; border-radius: 3px; }}

.sidebar-section {{
  padding: 0 12px;
  margin-bottom: 4px;
}}
.sidebar-heading {{
  font-size: 0.68rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.06em;
  color: #9ca3af; padding: 8px 12px 6px;
}}
.super-group-heading {{
  font-size: 0.72rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.05em;
  color: #6b7280; padding: 14px 12px 4px;
  border-top: 1px solid #e5e7eb;
  margin-top: 6px;
}}
.super-group-heading.sg-first {{
  border-top: none;
  margin-top: 0;
  padding-top: 4px;
}}

/* Top-level category */
.cat-top {{
  display: flex; align-items: center;
  padding: 7px 10px 7px 12px;
  border-radius: 6px;
  cursor: pointer;
  border-left: 3px solid transparent;
  transition: background 0.15s;
  user-select: none;
  margin: 1px 0;
}}
.cat-top:hover {{ background: #f3f4f6; }}
.cat-top.active {{ background: #eef2ff; }}
.cat-top .chevron {{
  width: 16px; height: 16px; flex-shrink: 0;
  transition: transform 0.2s;
  margin-right: 6px;
}}
.cat-top .chevron::before {{
  content: '';
  display: block;
  width: 6px; height: 6px;
  border-right: 1.5px solid #6b7280;
  border-bottom: 1.5px solid #6b7280;
  transform: rotate(-45deg);
  margin: 4px 0 0 4px;
}}
.cat-top.expanded .chevron::before {{
  transform: rotate(45deg);
  margin: 2px 0 0 4px;
}}
.cat-top .cat-name {{
  flex: 1; font-size: 0.84rem; font-weight: 600; color: #374151;
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}}
.cat-top .cat-count {{
  font-size: 0.72rem; color: #9ca3af; font-weight: 500;
  margin-left: 6px; flex-shrink: 0;
}}

/* Sub-level category */
.cat-sub-list {{
  max-height: 0; overflow: hidden;
  transition: max-height 0.25s ease;
}}
.cat-sub-list.open {{ max-height: 600px; }}
.cat-sub {{
  display: flex; align-items: center;
  padding: 5px 10px 5px 37px;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.15s;
  user-select: none;
}}
.cat-sub:hover {{ background: #f3f4f6; }}
.cat-sub.active {{ background: #eef2ff; }}
.cat-sub .cat-name {{
  flex: 1; font-size: 0.79rem; color: #4b5563;
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}}
.cat-sub .cat-count {{
  font-size: 0.7rem; color: #9ca3af; margin-left: 6px; flex-shrink: 0;
}}

.cat-clear {{
  display: none;
  padding: 6px 12px;
  margin: 8px 12px;
  border-radius: 6px;
  font-size: 0.78rem; font-weight: 500;
  color: #6b7280; background: #f3f4f6;
  cursor: pointer; text-align: center;
  transition: background 0.15s;
  border: none; width: calc(100% - 24px);
}}
.cat-clear:hover {{ background: #e5e7eb; }}
.cat-clear.show {{ display: block; }}

/* ============ MAIN ============ */
.main {{
  flex: 1;
  margin-left: var(--sidebar-w);
  padding: 20px 24px 40px;
  max-width: 100%;
  min-width: 0;
}}

/* ============ TOOLBAR ============ */
.toolbar {{
  display: flex; flex-wrap: wrap; gap: 10px; align-items: center;
  margin-bottom: 16px;
  position: sticky; top: var(--header-h);
  background: #f5f6f8;
  padding: 12px 0;
  z-index: 50;
}}
.search-box {{
  flex: 1; min-width: 200px;
  position: relative;
}}
.search-box input {{
  width: 100%;
  padding: 9px 14px 9px 36px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 0.88rem;
  background: #fff;
  outline: none;
  transition: border-color 0.15s, box-shadow 0.15s;
  font-family: inherit;
}}
.search-box input:focus {{
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59,130,246,0.12);
}}
.search-box .search-icon {{
  position: absolute; left: 11px; top: 50%; transform: translateY(-50%);
  width: 16px; height: 16px;
  color: #9ca3af;
}}
.search-box .search-icon::before {{
  content: '';
  display: block; width: 11px; height: 11px;
  border: 2px solid #9ca3af; border-radius: 50%;
}}
.search-box .search-icon::after {{
  content: '';
  display: block; width: 5px; height: 2px;
  background: #9ca3af;
  transform: rotate(45deg);
  position: absolute; bottom: 1px; right: 1px;
}}

.select-filter {{
  padding: 8px 28px 8px 10px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 0.82rem;
  background: #fff;
  appearance: none;
  -webkit-appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='%236b7280'%3E%3Cpath d='M5.23 7.21a.75.75 0 011.06.02L10 11.17l3.71-3.94a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 8px center;
  background-size: 14px;
  cursor: pointer;
  font-family: inherit;
  color: #374151;
  outline: none;
  min-width: 110px;
  transition: border-color 0.15s, box-shadow 0.15s;
}}
.select-filter:focus {{
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59,130,246,0.12);
}}
.select-filter.has-value {{
  border-color: #3b82f6;
  color: #2563eb;
  font-weight: 500;
}}

/* ============ STATUS BAR ============ */
.status-bar {{
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 12px;
  font-size: 0.82rem; color: #6b7280;
}}
.active-filters {{
  display: flex; gap: 6px; flex-wrap: wrap; align-items: center;
}}
.filter-tag {{
  display: inline-flex; align-items: center; gap: 4px;
  padding: 3px 10px;
  border-radius: 12px;
  font-size: 0.74rem; font-weight: 500;
  background: #eef2ff; color: #4338ca;
}}
.filter-tag .remove {{
  cursor: pointer; font-size: 0.9rem; line-height: 1;
  opacity: 0.6;
}}
.filter-tag .remove:hover {{ opacity: 1; }}

/* ============ PAPER CARDS ============ */
.paper-list {{
  display: flex; flex-direction: column; gap: 8px;
}}
.paper-card {{
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  padding: 14px 18px;
  transition: box-shadow 0.15s, border-color 0.15s;
}}
.paper-card:hover {{
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  border-color: #d1d5db;
}}
.paper-header {{
  display: flex; align-items: flex-start; gap: 10px;
  cursor: pointer;
}}
.paper-expand {{
  flex-shrink: 0;
  width: 18px; height: 18px;
  margin-top: 2px;
  position: relative;
}}
.paper-expand::before,
.paper-expand::after {{
  content: '';
  position: absolute;
  background: #9ca3af;
  transition: transform 0.2s;
}}
.paper-expand::before {{
  width: 10px; height: 1.5px;
  top: 8px; left: 4px;
}}
.paper-expand::after {{
  width: 1.5px; height: 10px;
  top: 4px; left: 8px;
}}
.paper-card.open .paper-expand::after {{
  transform: rotate(90deg);
}}
.paper-title-wrap {{ flex: 1; min-width: 0; }}
.paper-title {{
  font-size: 0.94rem; font-weight: 600; color: #1a1a2e;
  line-height: 1.4;
  display: inline;
}}
.paper-title a {{
  color: inherit;
  text-decoration: none;
}}
.paper-title a:hover {{
  color: #3b82f6;
  text-decoration: underline;
}}
.paper-meta {{
  display: flex; flex-wrap: wrap; gap: 5px;
  margin-top: 7px;
}}
.badge {{
  display: inline-block;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 0.7rem; font-weight: 600;
  letter-spacing: 0.02em;
}}
.badge-venue {{
  background: #f0f0f5; color: #4b5563;
}}
.badge-year {{
  background: #dbeafe; color: #1d4ed8;
}}
.label-pill {{
  display: inline-block;
  padding: 2px 7px;
  border-radius: 4px;
  font-size: 0.68rem; font-weight: 500;
  max-width: 180px;
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  cursor: pointer;
  transition: opacity 0.15s;
}}
.label-pill:hover {{ opacity: 0.75; }}
.paper-abstract {{
  max-height: 0; overflow: hidden;
  transition: max-height 0.3s ease, margin 0.2s ease;
  font-size: 0.84rem; color: #4b5563; line-height: 1.6;
  margin-top: 0;
}}
.paper-card.open .paper-abstract {{
  max-height: 600px;
  margin-top: 12px;
}}

/* ============ VIRTUAL SCROLL SENTINEL ============ */
.load-more-sentinel {{
  height: 1px;
}}
.no-results {{
  text-align: center;
  padding: 60px 20px;
  color: #9ca3af;
  font-size: 0.95rem;
}}

/* ============ SCROLLBAR ============ */
.main::-webkit-scrollbar {{ width: 6px; }}
.main::-webkit-scrollbar-thumb {{ background: #d1d5db; border-radius: 3px; }}

/* ============ RESPONSIVE ============ */
@media (max-width: 768px) {{
  .mobile-toggle {{ display: flex; flex-direction: column; }}
  .sidebar {{
    transform: translateX(-100%);
    z-index: 200;
    box-shadow: 4px 0 16px rgba(0,0,0,0.1);
  }}
  .sidebar.open {{ transform: translateX(0); }}
  .main {{ margin-left: 0; padding: 16px 14px 40px; }}
  .header {{ padding: 0 14px; }}
  .toolbar {{ gap: 8px; }}
  .select-filter {{ min-width: 90px; }}
  .overlay {{
    display: none;
    position: fixed; inset: 0;
    background: rgba(0,0,0,0.3);
    z-index: 150;
  }}
  .overlay.show {{ display: block; }}
}}

/* ============ LABEL PILL COLORS ============ */
.lp-0 {{ background: rgba(59,130,246,0.1); color: #2563eb; }}
.lp-1 {{ background: rgba(139,92,246,0.1); color: #7c3aed; }}
.lp-2 {{ background: rgba(6,182,212,0.1); color: #0891b2; }}
.lp-3 {{ background: rgba(239,68,68,0.1); color: #dc2626; }}
.lp-4 {{ background: rgba(249,115,22,0.1); color: #ea580c; }}
.lp-5 {{ background: rgba(16,185,129,0.1); color: #059669; }}
.lp-6 {{ background: rgba(99,102,241,0.1); color: #4f46e5; }}
.lp-7 {{ background: rgba(236,72,153,0.1); color: #db2777; }}
.lp-8 {{ background: rgba(234,179,8,0.12); color: #a16207; }}

/* Border colors for top cats */
.bc-0 {{ border-left-color: var(--c0); }}
.bc-1 {{ border-left-color: var(--c1); }}
.bc-2 {{ border-left-color: var(--c2); }}
.bc-3 {{ border-left-color: var(--c3); }}
.bc-4 {{ border-left-color: var(--c4); }}
.bc-5 {{ border-left-color: var(--c5); }}
.bc-6 {{ border-left-color: var(--c6); }}
.bc-7 {{ border-left-color: var(--c7); }}
.bc-8 {{ border-left-color: var(--c8); }}

/* ============ BACK-TO-TOP ============ */
.back-to-top {{
  position: fixed; bottom: 24px; right: 24px;
  width: 40px; height: 40px;
  border-radius: 50%;
  background: #3b82f6; color: #fff;
  border: none; cursor: pointer;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  font-size: 1.2rem;
  display: none;
  align-items: center; justify-content: center;
  transition: opacity 0.2s;
  z-index: 80;
}}
.back-to-top.show {{ display: flex; }}
</style>
</head>
<body>

<div class="overlay" id="overlay"></div>

<header class="header">
  <button class="mobile-toggle" id="mobileToggle" aria-label="Toggle sidebar">
    <span></span><span></span><span></span>
  </button>
  <div class="header-title"><span>Agentic Software Engineering</span> (ASE)</div>
  <div class="header-count" id="headerCount">{total} papers from {len(venues_sorted)} venues</div>
  <div class="header-desc">A curated database of Agentic SE from top-tier venues</div>
</header>

<div class="layout">
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-heading">Categories</div>
    <button class="cat-clear" id="catClear">Clear category filter</button>
    <div id="catTree"></div>
  </aside>
  <div class="main" id="mainArea">
    <div class="toolbar">
      <div class="search-box">
        <div class="search-icon"></div>
        <input type="text" id="searchInput" placeholder="Search papers by title or abstract..." autocomplete="off">
      </div>
      <select class="select-filter" id="yearSelect">
        <option value="">All Years</option>
        {"".join(f'<option value="{y}">{y}</option>' for y in years_sorted)}
      </select>
      <select class="select-filter" id="venueSelect">
        <option value="">All Venues</option>
        {"".join(f'<option value="{html.escape(b)}">{html.escape(b)}</option>' for b in base_venues_sorted)}
      </select>
    </div>
    <div class="status-bar">
      <div id="statusText">Showing {total} of {total} papers</div>
      <div class="active-filters" id="activeFilters"></div>
    </div>
    <div class="paper-list" id="paperList"></div>
    <div class="load-more-sentinel" id="sentinel"></div>
    <div class="no-results" id="noResults" style="display:none">No papers match your current filters.</div>
  </div>
</div>

<button class="back-to-top" id="backToTop" title="Back to top">&#8593;</button>

<script>
const PAPERS = {papers_json};
const TAXONOMY = {taxonomy_json};
const CAT_COUNTS = {cat_counts_json};
const TOTAL = {total};
const TOP_CATS = Object.keys(TAXONOMY);
const SUPER_GROUPS = {super_groups_json};

/* ---- label -> color index map ---- */
const labelColorMap = {{}};
TOP_CATS.forEach((tc, i) => {{
  labelColorMap[tc] = i;
  TAXONOMY[tc].forEach(sc => {{ labelColorMap[sc] = i; }});
}});

/* ---- Build category tree ---- */
const catTree = document.getElementById('catTree');
const catClear = document.getElementById('catClear');
let activeCats = new Set(); // set of label names (multi-select)

function buildCatTree() {{
  let h = '';
  SUPER_GROUPS.forEach((sg, gi) => {{
    const [groupName, groupCats] = sg;
    h += `<div class="super-group-heading${{gi === 0 ? ' sg-first' : ''}}">${{groupName}}</div>`;
    groupCats.forEach(tc => {{
      const i = TOP_CATS.indexOf(tc);
      if (i === -1) return;
      const cnt = CAT_COUNTS[tc] || 0;
      h += `<div class="sidebar-section">`;
      h += `<div class="cat-top bc-${{i}}" data-cat="${{tc}}" data-idx="${{i}}">`;
      h += `<div class="chevron"></div>`;
      h += `<span class="cat-name">${{tc}}</span>`;
      h += `<span class="cat-count">${{cnt}}</span>`;
      h += `</div>`;
      h += `<div class="cat-sub-list" data-parent="${{tc}}">`;
      TAXONOMY[tc].forEach(sc => {{
        const scnt = CAT_COUNTS[sc] || 0;
        if (scnt > 0) {{
          h += `<div class="cat-sub" data-cat="${{sc}}" data-parent="${{tc}}">`;
          h += `<span class="cat-name">${{sc}}</span>`;
          h += `<span class="cat-count">${{scnt}}</span>`;
          h += `</div>`;
        }}
      }});
      h += `</div></div>`;
    }});
  }});
  catTree.innerHTML = h;
}}
buildCatTree();

function syncCatActiveState() {{
  catTree.querySelectorAll('.cat-top, .cat-sub').forEach(el => {{
    el.classList.toggle('active', activeCats.has(el.dataset.cat));
  }});
  catClear.classList.toggle('show', activeCats.size > 0);
}}

catTree.addEventListener('click', e => {{
  const topEl = e.target.closest('.cat-top');
  const subEl = e.target.closest('.cat-sub');

  if (subEl) {{
    const name = subEl.dataset.cat;
    if (activeCats.has(name)) {{
      activeCats.delete(name);
    }} else {{
      activeCats.add(name);
      // ensure parent is expanded
      const parent = subEl.dataset.parent;
      const pEl = catTree.querySelector(`.cat-top[data-cat="${{parent}}"]`);
      if (pEl) pEl.classList.add('expanded');
      const subList = catTree.querySelector(`.cat-sub-list[data-parent="${{parent}}"]`);
      if (subList) subList.classList.add('open');
    }}
    syncCatActiveState();
    applyFilters();
    return;
  }}
  if (topEl) {{
    const name = topEl.dataset.cat;
    const subList = catTree.querySelector(`.cat-sub-list[data-parent="${{name}}"]`);
    const isExpanded = topEl.classList.contains('expanded');
    if (!isExpanded) {{
      topEl.classList.add('expanded');
      subList.classList.add('open');
    }} else {{
      topEl.classList.remove('expanded');
      subList.classList.remove('open');
    }}
    // toggle top-level cat in selection
    if (activeCats.has(name)) {{
      activeCats.delete(name);
    }} else {{
      activeCats.add(name);
    }}
    syncCatActiveState();
    applyFilters();
  }}
}});

function clearCat() {{
  activeCats.clear();
  syncCatActiveState();
  applyFilters();
}}
catClear.addEventListener('click', clearCat);

/* ---- Search, Year, Venue filters ---- */
const searchInput = document.getElementById('searchInput');
const yearSelect = document.getElementById('yearSelect');
const venueSelect = document.getElementById('venueSelect');
let searchTerm = '';
let activeYear = '';
let activeVenue = '';

/* strip year and track suffixes, e.g. 'EMNLP-findings2024' -> 'EMNLP' */
function venueBase(v) {{ return v.replace(/\d{{4}}$/, '').replace(/-(findings|main)$/i, ''); }}

searchInput.addEventListener('input', () => {{
  searchTerm = searchInput.value.trim().toLowerCase();
  applyFilters();
}});

yearSelect.addEventListener('change', () => {{
  activeYear = yearSelect.value;
  yearSelect.classList.toggle('has-value', !!activeYear);
  applyFilters();
}});

venueSelect.addEventListener('change', () => {{
  activeVenue = venueSelect.value;
  venueSelect.classList.toggle('has-value', !!activeVenue);
  applyFilters();
}});

/* ---- Filtering ---- */
let filtered = PAPERS.slice();
const BATCH_SIZE = 60;
let renderedCount = 0;

function applyFilters() {{
  filtered = PAPERS.filter(p => {{
    if (activeYear && p.y !== activeYear) return false;
    if (activeVenue && venueBase(p.v) !== activeVenue) return false;
    if (activeCats.size > 0 && ![...activeCats].every(lb => p.l.includes(lb))) return false;
    if (searchTerm && !(p.t + ' ' + p.a).toLowerCase().includes(searchTerm)) return false;
    return true;
  }});

  // update status
  document.getElementById('statusText').textContent = `Showing ${{filtered.length}} of ${{TOTAL}} papers`;

  // update active filter tags
  updateFilterTags();

  // render
  renderedCount = 0;
  document.getElementById('paperList').innerHTML = '';
  document.getElementById('noResults').style.display = filtered.length === 0 ? 'block' : 'none';
  renderBatch();
}}

function updateFilterTags() {{
  const af = document.getElementById('activeFilters');
  let h = '';
  if (activeYear) {{
    h += `<span class="filter-tag" style="background:#dbeafe;color:#1d4ed8">Year: ${{activeYear}} <span class="remove" data-action="clearYear">&times;</span></span>`;
  }}
  if (activeVenue) {{
    h += `<span class="filter-tag" style="background:#ede9fe;color:#6d28d9">Venue: ${{activeVenue}} <span class="remove" data-action="clearVenue">&times;</span></span>`;
  }}
  activeCats.forEach(name => {{
    h += `<span class="filter-tag lp-${{labelColorMap[name] ?? 0}}">${{name}} <span class="remove" data-action="clearCat" data-name="${{name}}">&times;</span></span>`;
  }});
  if (searchTerm) {{
    h += `<span class="filter-tag" style="background:#fef3c7;color:#92400e">"${{searchTerm.length > 20 ? searchTerm.slice(0,20) + '...' : searchTerm}}" <span class="remove" data-action="clearSearch">&times;</span></span>`;
  }}
  af.innerHTML = h;
}}

document.getElementById('activeFilters').addEventListener('click', e => {{
  const rm = e.target.closest('.remove');
  if (!rm) return;
  const action = rm.dataset.action;
  if (action === 'clearYear') {{
    activeYear = '';
    yearSelect.value = '';
    yearSelect.classList.remove('has-value');
    applyFilters();
  }}
  if (action === 'clearVenue') {{
    activeVenue = '';
    venueSelect.value = '';
    venueSelect.classList.remove('has-value');
    applyFilters();
  }}
  if (action === 'clearCat') {{
    activeCats.delete(rm.dataset.name);
    syncCatActiveState();
    applyFilters();
  }}
  if (action === 'clearSearch') {{
    searchTerm = '';
    searchInput.value = '';
    applyFilters();
  }}
}});

/* ---- Rendering (lazy batches) ---- */
function escapeHtml(s) {{
  const el = document.createElement('span');
  el.textContent = s;
  return el.innerHTML;
}}

function renderBatch() {{
  const list = document.getElementById('paperList');
  const end = Math.min(renderedCount + BATCH_SIZE, filtered.length);
  const frag = document.createDocumentFragment();

  for (let i = renderedCount; i < end; i++) {{
    const p = filtered[i];
    const card = document.createElement('div');
    card.className = 'paper-card';

    // labels html
    let labelsHtml = '';
    for (const lb of p.l) {{
      const ci = labelColorMap[lb] ?? 0;
      labelsHtml += `<span class="label-pill lp-${{ci}}" title="${{escapeHtml(lb)}}" data-label="${{escapeHtml(lb)}}">${{escapeHtml(lb)}}</span>`;
    }}

    const titleLink = p.u
      ? `<a href="${{escapeHtml(p.u)}}" target="_blank" rel="noopener" onclick="event.stopPropagation()">${{escapeHtml(p.t)}}</a>`
      : escapeHtml(p.t);

    card.innerHTML = `<div class="paper-header">
      <div class="paper-expand"></div>
      <div class="paper-title-wrap">
        <div class="paper-title">${{titleLink}}</div>
        <div class="paper-meta">
          <span class="badge badge-venue">${{escapeHtml(p.v)}}</span>
          <span class="badge badge-year">${{escapeHtml(p.y)}}</span>
          ${{labelsHtml}}
        </div>
      </div>
    </div>
    <div class="paper-abstract">${{escapeHtml(p.a || 'No abstract available.')}}</div>`;

    card.querySelector('.paper-header').addEventListener('click', (e) => {{
      if (e.target.closest('.label-pill')) return;
      card.classList.toggle('open');
    }});

    card.querySelectorAll('.label-pill').forEach(pill => {{
      pill.addEventListener('click', (e) => {{
        e.stopPropagation();
        const label = pill.dataset.label;
        if (!label) return;
        if (activeCats.has(label)) {{
          activeCats.delete(label);
        }} else {{
          activeCats.add(label);
          // ensure parent top-cat is expanded in sidebar
          const parent = TOP_CATS.find(tc => TAXONOMY[tc].includes(label));
          if (parent) {{
            const pEl = catTree.querySelector(`.cat-top[data-cat="${{parent}}"]`);
            if (pEl) pEl.classList.add('expanded');
            const subList = catTree.querySelector(`.cat-sub-list[data-parent="${{parent}}"]`);
            if (subList) subList.classList.add('open');
          }}
        }}
        syncCatActiveState();
        applyFilters();
      }});
    }});

    frag.appendChild(card);
  }}

  list.appendChild(frag);
  renderedCount = end;
}}

/* ---- Intersection Observer for lazy loading ---- */
const sentinel = document.getElementById('sentinel');
const observer = new IntersectionObserver(entries => {{
  if (entries[0].isIntersecting && renderedCount < filtered.length) {{
    renderBatch();
  }}
}}, {{ rootMargin: '400px' }});
observer.observe(sentinel);

/* ---- Mobile sidebar toggle ---- */
const mobileToggle = document.getElementById('mobileToggle');
const sidebar = document.getElementById('sidebar');
const overlay = document.getElementById('overlay');

mobileToggle.addEventListener('click', () => {{
  sidebar.classList.toggle('open');
  overlay.classList.toggle('show');
}});
overlay.addEventListener('click', () => {{
  sidebar.classList.remove('open');
  overlay.classList.remove('show');
}});

/* ---- Back to top ---- */
const backToTop = document.getElementById('backToTop');
window.addEventListener('scroll', () => {{
  backToTop.classList.toggle('show', window.scrollY > 400);
}});
backToTop.addEventListener('click', () => {{
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
}});

/* ---- Initial render ---- */
applyFilters();
</script>
</body>
</html>"""
    return html_content


def main():
    print(f"Reading data from {DATA_PATH}...")
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    print(f"Found {len(raw_data)} papers")

    papers = build_compact_papers(raw_data)
    cat_counts, venue_counts, year_counts = compute_stats(papers)

    print("Generating HTML...")
    html_content = generate_html(papers, cat_counts, venue_counts, year_counts)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)

    size_mb = os.path.getsize(OUTPUT_PATH) / (1024 * 1024)
    print(f"Written to {OUTPUT_PATH}")
    print(f"File size: {size_mb:.2f} MB")

    if size_mb > 10:
        print("WARNING: File exceeds 10MB limit!")
    else:
        print("File size is within the 10MB limit.")


if __name__ == "__main__":
    main()
