---
name: paper-labeler
description: >
  Extract, filter, and label research papers from rawdata files (.bib, .html) using the two-level
  taxonomy defined in SKILL.md. Use this skill when the
  user wants to process new venue data, label papers, add new conferences to the database, run the
  paper classification pipeline, rebuild the website, or batch-process a folder of rawdata.
  Triggers: "label papers", "process rawdata", "process folder", "batch process",
  "add venue", "classify papers", "extract papers from", "run the labeling pipeline", "process .bib",
  "process .html", "rebuild website", "update website".
---

# Paper Labeler

Classify LLM-for-code research papers from conference proceedings into a two-level label taxonomy.

## Pipeline Overview

Four steps, run in sequence:

1. **extract_papers.py** — Parse raw venue files into a uniform JSON format
   - For NDSS: also run **fetch_ndss_abstracts.py** to scrape abstracts from paper pages
2. **label_papers.py** — Filter by relevance keywords, then label with Claude API
3. **merge_labeldata.py** — Merge results into `data/labeldata/labeldata.json`
4. **build_site.py** — Rebuild the website from updated labeldata

Batch mode:
- **process_folder.py** — Scan a rawdata folder, skip venues already in `data/venues.json`,
  and run the full pipeline (extract → label → merge → rebuild) for new venues only.

Additionally:
- **import_original.py** — Import papers from `data/rawdata/original.json` that are missing from
  labeldata, mapping old-style labels to the current taxonomy via Claude API. Avoids duplicates.

All scripts are in `.claude/skills/paper-labeler/scripts/`.

## Step-by-Step Workflow

### Batch Mode: Process a Folder

Scan a rawdata folder, skip venues already in `data/venues.json`, and run the full pipeline
for each new venue. This is the simplest way to process new data.

```bash
# Process all unprocessed venues under data/rawdata/
python .claude/skills/paper-labeler/scripts/process_folder.py

# Process a specific year folder
python .claude/skills/paper-labeler/scripts/process_folder.py data/rawdata/2025/

# Dry-run: show which venues would be processed
python .claude/skills/paper-labeler/scripts/process_folder.py --dry-run

# Filter only (no API calls, no merge)
python .claude/skills/paper-labeler/scripts/process_folder.py --filter-only
```

Options:
- `--dry-run` — show which venues are new vs already processed, no action
- `--filter-only` — keyword filter only, no Claude API calls or merge
- `--model MODEL` — Bedrock model ID (default: us.anthropic.claude-sonnet-4-6)
- `--region REGION` — AWS region (default: us-east-1)
- `--delay SECONDS` — delay between API calls (default: 0.5)
- `--no-rebuild` — skip website rebuild after processing

The script:
1. Reads `data/venues.json` to get already-processed venues
2. Scans the folder for `.bib` and `.html` files, groups them by canonical venue name
3. Skips venues already in `venues.json`
4. For each new venue: extract → (fetch NDSS abstracts if needed) → filter+label → merge
5. Updates `venues.json` after each successful venue
6. Rebuilds the website once at the end

Venue names are derived from filenames: `EMNLP-findings2024.html` and `EMNLP-main2024.html`
both map to `EMNLP2024`, so multiple track files for the same venue are processed together.

### Step 1: Extract Papers

Determine the input format and run the extractor.

```bash
# BibTeX files (SE/PL/Security venues — most common)
python .claude/skills/paper-labeler/scripts/extract_papers.py data/rawdata/2025/ASE2025.bib > /tmp/extracted.json

# ACL Anthology HTML files (ACL, EMNLP, NAACL)
python .claude/skills/paper-labeler/scripts/extract_papers.py data/rawdata/2025/ACL2025.html > /tmp/extracted.json

# NDSS HTML files (titles only — abstracts need individual page fetching)
python .claude/skills/paper-labeler/scripts/extract_papers.py data/rawdata/2025/NDSS2025.html > /tmp/extracted.json
```

Format auto-detection works by file extension and content. Override with `--format bib|acl|ndss`.

URL handling:
- BibTeX: uses `url` field if present; otherwise auto-constructs from `doi` field (`https://doi.org/{doi}`)
- ACL Anthology HTML: extracts URLs from `<a href=...>` in title links (e.g., `https://aclanthology.org/2025.acl-long.1/`)
- NDSS HTML: extracts URLs from paper links
- If a paper's key is a DOI (e.g., `10.5555/...`), it can be used as a fallback URL via `https://doi.org/{key}`

For NDSS: the HTML only contains titles and links (no inline abstracts). After extraction,
use `fetch_ndss_abstracts.py` to scrape abstracts from individual paper pages:

```bash
python .claude/skills/paper-labeler/scripts/extract_papers.py data/rawdata/2025/NDSS2025.html > /tmp/ndss_extracted.json
python .claude/skills/paper-labeler/scripts/fetch_ndss_abstracts.py /tmp/ndss_extracted.json -o /tmp/extracted.json
```

Options for `fetch_ndss_abstracts.py`:
- `--delay SECONDS` — delay between HTTP requests (default: 1.0)
- `--resume` — skip papers already in the output file (for resuming after interruption)

### Step 2: Filter and Label

**Phase 1 — Keyword filter (no API needed):**

```bash
python .claude/skills/paper-labeler/scripts/label_papers.py /tmp/extracted.json --phase filter -o /tmp/filtered.json
```

This keeps papers whose title+abstract mention both LLM-related AND code-related terms.
It is deliberately conservative (high recall) to avoid missing relevant papers.

**Phase 2 — Claude labeling via AWS Bedrock (requires AWS credentials):**

```bash
python .claude/skills/paper-labeler/scripts/label_papers.py /tmp/filtered.json --phase label -o /tmp/labeled.json
```

Or run both phases at once:

```bash
python .claude/skills/paper-labeler/scripts/label_papers.py /tmp/extracted.json --phase all -o /tmp/labeled.json
```

Options:
- `--model MODEL` — Bedrock model ID (default: us.anthropic.claude-sonnet-4-6)
- `--region REGION` — AWS region (default: us-east-1)
- `--delay SECONDS` — delay between API calls (default: 0.5)
- `--dry-run` — preview what would be labeled, no API calls

### Step 3: Merge into labeldata

```bash
python .claude/skills/paper-labeler/scripts/merge_labeldata.py /tmp/labeled.json
```

Options:
- `--dry-run` — show merge stats without writing
- `--no-overwrite` — skip papers already in labeldata.json
- `--labeldata PATH` — write to a different file

### Step 4: Rebuild Website

After merging new papers into labeldata.json, rebuild the website:

```bash
python .claude/skills/paper-labeler/scripts/build_site.py
```

This reads `data/labeldata/labeldata.json` and generates `web/index.html` — a single-page app
with category sidebar (grouped into three super-groups: Agent for SE, Agent Design and Analysis,
Evaluation), search, year/venue filters, and expandable abstracts.

## Label Taxonomy

The complete two-level taxonomy is hardcoded below. A paper can belong to multiple categories.

### 1. Code Generation
- **Program Synthesis** — generating code from natural language descriptions, formal specifications, or input-output examples; includes NL2Code, text-to-SQL, text-to-code, sketch-based synthesis, inductive synthesis, competition programming, code infilling
- **Code Completion** — token-level, line-level, or block-level prediction in editing context; next-token prediction, fill-in-the-middle, IDE autocompletion, inline suggestion, code recommendation
- **Program Repair** — automated bug fixing, patch generation, vulnerability remediation, error correction, program healing, fault repair, security patch, hotfix generation
- **Code Translation** — cross-language migration, transpilation, language porting, API migration, framework migration, legacy modernization, parallel code translation
- **Decompilation** — recovering high-level source code from binary, bytecode, IR, or WebAssembly; lifting, binary-to-source, disassembly-to-C, neural decompilation
- **Refactoring** — code transformation, extract method, rename, move method, code cleanup, style improvement, dead code removal, design pattern application, technical debt reduction

### 2. Static Analysis
- **Bug Detection** — non-security defects, code smells, anti-patterns, defect prediction, error-prone pattern detection, anomaly detection in code, coding rule violation
- **Program Verification** — formal proof generation, loop invariant synthesis, model checking, theorem proving, Hoare logic, SMT-based verification, bounded model checking, safety property verification, correctness proof, program equivalence
- **Specification Inference** — precondition inference, postcondition inference, contract generation, API specification mining, behavioral specification, protocol inference, function summary generation
- **Pointer Analysis** — points-to analysis, alias analysis, heap modeling, shape analysis, pointer dereference safety, null pointer detection
- **Call Graph Analysis** — call graph construction, function call resolution, virtual dispatch resolution, dynamic dispatch analysis, indirect call analysis, call graph pruning, call graph completeness
- **Type Inference** — type prediction, type annotation generation, gradual typing, type migration, TypeScript/Python type inference, generic type instantiation, type error detection
- **Data-flow Analysis** — reaching definitions, def-use chains, live variable analysis, constant propagation, value-flow analysis, information flow analysis, data dependency analysis
- **Taint Analysis** — taint propagation, source-sink analysis, injection vulnerability detection, untrusted input tracking, sanitization checking, taint policy enforcement
- **Symbolic Execution** — path exploration, constraint solving, concolic execution, symbolic path analysis, path feasibility checking, automatic test input generation via symbolic methods
- **Abstract Interpretation** — numerical abstract domains, interval analysis, polyhedral analysis, widening/narrowing, semantic abstraction, fixpoint computation, over-approximation
- **Code Summarization** — function-level summary, module-level summary, code documentation generation, code explanation, natural language description of code, code narration, code captioning
- **Code Search** — semantic code search, natural language code query, code retrieval, code recommendation, API discovery, example-based code search, cross-lingual code search
- **Clone Detection** — code clone detection, near-miss clone, semantic clone, Type-1/2/3/4 clone, code plagiarism, code similarity measurement, code duplication

### 3. Dynamic Analysis
- **Test Case Generation** — unit test generation, integration test generation, system test generation, regression test generation, parameterized test, property-based test, boundary value test, test input generation
- **Test Oracle** — assertion generation, expected output inference, metamorphic relation, test oracle derivation, differential oracle, invariant-based oracle, specification-based oracle
- **Fuzzing** — coverage-guided fuzzing, grammar-based fuzzing, mutation-based fuzzing, protocol fuzzing, API fuzzing, kernel fuzzing, IoT fuzzing, seed generation, harness generation, directed fuzzing
- **Debugging** — root cause analysis, automated debugging, fault localization, spectrum-based fault localization, delta debugging, statistical debugging, interactive debugging, failure explanation
- **Mutation Testing** — mutant generation, equivalent mutant detection, mutation score, mutation operator, higher-order mutant, mutation-based test assessment
- **Bug Reproduction** — crash reproduction, bug report reproduction, failure-inducing input, crash deduplication, core dump analysis, reproducing field failures
- **Domain-Specific Testing** — DBMS testing, compiler testing, network protocol testing, kernel testing, GUI testing, mobile app testing, web application testing, embedded system testing, smart contract testing
- **PoC and Exploit Generation** — proof-of-concept generation, exploit synthesis, vulnerability triggering, attack payload construction, CVE reproduction, exploit chain construction

### 4. Model Safety and Security
- **Adversarial Attack** — adversarial examples against code models, evasion attacks, adversarial perturbation, identifier renaming attack, dead code insertion, semantic-preserving perturbation, adversarial robustness evaluation
- **Backdoor Detection** — trojan detection in code models, backdoor trigger identification, poisoned model detection, neural cleanse for code models, training data poisoning defense, supply chain attack on models, model integrity verification
- **Memorization** — training data extraction, membership inference attack, data contamination detection, benchmark contamination, verbatim memorization, privacy leakage, copyright infringement, data provenance
- **Secure Code Generation** — generating vulnerability-free code, security-aware code generation, CWE-free generation, constrained decoding for security, RLHF for safe code, security policy enforcement during generation
- **Watermarking** — code watermark embedding, watermark detection, AI-generated code identification, code authorship attribution, code provenance verification, model fingerprinting, intellectual property protection
- **Jailbreaking** — bypassing model safety alignment, automated red teaming, safety guardrail evasion, harmful code generation, misuse potential evaluation, safety benchmark, attack taxonomy for code LLMs

### 5. Agent Safety and Security
- **Prompt Injection** — direct prompt injection, indirect prompt injection, context manipulation, instruction override, data exfiltration via prompt, cross-plugin attack, prompt leaking, goal hijacking
- **Agent Defense** — runtime trace analysis, agent sandboxing, guardrail enforcement, output filtering, safety monitoring, anomaly detection in agent behavior, agent alignment, safe tool invocation
- **Access Control** — permission management, least privilege enforcement, capability restriction, resource access policy, file system access control, network access control, API scope limitation, privilege escalation prevention, credential handling

### 6. Agent Design
- **Planning** — task decomposition, hierarchical planning, multi-step reasoning, goal-directed planning, plan generation, plan refinement, backtracking, subgoal identification, workflow orchestration, chain-of-thought, tree-of-thought, graph-of-thought
- **Memory Management** — context window management, long-term memory, episodic memory, working memory, conversation history compression, retrieval-augmented generation, knowledge base grounding, repo-level context retrieval, codebase indexing
- **Tool Use** — function calling, API invocation, compiler interaction, debugger integration, test execution, shell command execution, code interpreter, web browsing, database query, external tool orchestration, MCP
- **Multi-Agent** — multi-agent collaboration, pair programming, role-based agent teams, agent communication protocol, task delegation, agent negotiation, debate-based verification, ensemble of agents, agent specialization

### 7. Code Model
- **Model Training** — pre-training objectives (MLM, CLM, denoising), code-specific pre-training, continual pre-training, parameter-efficient fine-tuning (LoRA, adapter, prefix tuning), instruction tuning, RLHF, DPO, data curation, synthetic data generation, curriculum learning, code tokenization
- **Binary and IR Model** — binary code representation learning, LLVM IR modeling, assembly language model, WebAssembly model, bytecode model, cross-architecture binary analysis, binary similarity, binary function embedding

### 8. Other SE Tasks
- **Code Review** — automated code review, review comment generation, review score prediction, code change assessment, reviewer recommendation, review quality evaluation, pull request analysis
- **Doc/Comment/Commit Message Generation** — docstring generation, inline comment generation, commit message generation, changelog generation, API documentation, README generation, release note generation, Javadoc
- **Log Analysis** — log parsing, log anomaly detection, logging statement generation, log template extraction, log-based failure diagnosis, log level recommendation, structured logging

### 9. Evaluation
- **Benchmark** — dataset construction, evaluation framework, leaderboard, test suite, code generation benchmark, analysis benchmark, security benchmark, multi-task benchmark, cross-lingual benchmark, execution-based evaluation, human evaluation protocol
- **Empirical Study** — large-scale evaluation, comparative study, user study, developer survey, ablation study, replication study, industrial case study, mixed-methods study, A/B testing of LLM tools
- **Survey** — literature review, systematic literature review, systematic mapping study, meta-analysis, research roadmap, taxonomy study, state-of-the-art review, tutorial overview

### Label Format

Each paper's `labels` field is a flat list containing both top-level and sub-level labels.
Example: `["Static Analysis", "Bug Detection", "Evaluation", "Benchmark"]`

## Relevance Criteria

A paper is relevant if **LLMs or AI agents are a central part of the paper's own contribution** — either:
1. Using LLMs/agents to solve software engineering tasks (code generation, analysis, testing, repair, etc.), OR
2. Studying properties of code LLMs/agents themselves (safety, security, benchmarking, training)

NOT relevant:
- Papers that only mention LLMs/agents in background/related work but don't use or study them
- Traditional ML (SVM, random forest), traditional DL (CNN, RNN, GNN) applied to SE — unless specifically targeting code LLMs (e.g., adversarial attacks on code models)
- General NLP/vision/speech unrelated to code
- Neural network verification, ML compilers, quantum computing, pure PL theory
- General SE papers that don't use LLMs/agents as a core component

## Output Format

The output JSON matches `data/labeldata/labeldata.json` schema:

```json
{
  "Paper Title": {
    "type": "INPROCEEDINGS",
    "key": "...",
    "author": "...",
    "booktitle": "...",
    "title": "Paper Title",
    "year": "2025",
    "abstract": "...",
    "labels": ["Code Generation", "Program Synthesis"],
    "venue": "ASE2025",
    "url": "...",
    ...
  }
}
```

## Common Patterns

**Batch-process all new venues in a folder:**
```bash
# Dry-run first to see what's new
python .claude/skills/paper-labeler/scripts/process_folder.py data/rawdata/2025/ --dry-run

# Process all new venues (skips already-processed ones)
python .claude/skills/paper-labeler/scripts/process_folder.py data/rawdata/2025/
```

**Process a new SE venue (bib file):**
```bash
python .claude/skills/paper-labeler/scripts/extract_papers.py data/rawdata/2025/ASE2025.bib > /tmp/extracted.json
python .claude/skills/paper-labeler/scripts/label_papers.py /tmp/extracted.json --phase all -o /tmp/labeled_ASE2025.json
python .claude/skills/paper-labeler/scripts/merge_labeldata.py /tmp/labeled_ASE2025.json --dry-run
python .claude/skills/paper-labeler/scripts/merge_labeldata.py /tmp/labeled_ASE2025.json
python .claude/skills/paper-labeler/scripts/build_site.py
```

**Process a new NLP venue (ACL Anthology HTML):**
```bash
python .claude/skills/paper-labeler/scripts/extract_papers.py data/rawdata/2025/ACL2025.html > /tmp/extracted.json
python .claude/skills/paper-labeler/scripts/label_papers.py /tmp/extracted.json --phase all -o /tmp/labeled_ACL2025.json
python .claude/skills/paper-labeler/scripts/merge_labeldata.py /tmp/labeled_ACL2025.json
python .claude/skills/paper-labeler/scripts/build_site.py
```

**Process an NDSS venue (HTML — requires abstract fetching):**
```bash
python .claude/skills/paper-labeler/scripts/extract_papers.py data/rawdata/2025/NDSS2025.html > /tmp/ndss_extracted.json
python .claude/skills/paper-labeler/scripts/fetch_ndss_abstracts.py /tmp/ndss_extracted.json -o /tmp/extracted.json
python .claude/skills/paper-labeler/scripts/label_papers.py /tmp/extracted.json --phase all -o /tmp/labeled_NDSS2025.json
python .claude/skills/paper-labeler/scripts/merge_labeldata.py /tmp/labeled_NDSS2025.json
python .claude/skills/paper-labeler/scripts/build_site.py
```

**Preview without API calls:**
```bash
python .claude/skills/paper-labeler/scripts/extract_papers.py data/rawdata/2025/CCS2025.bib > /tmp/extracted.json
python .claude/skills/paper-labeler/scripts/label_papers.py /tmp/extracted.json --phase all --dry-run
```

**Note:** Phase 2 uses AWS Bedrock (boto3). Ensure AWS credentials are configured
(`~/.aws/credentials`, environment variables, or IAM role).
Abstract fetching (`fetch_ndss_abstracts.py`) requires `requests` (pip install requests).
