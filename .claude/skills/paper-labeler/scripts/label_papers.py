#!/usr/bin/env python3
"""
Label extracted papers using the two-level taxonomy defined in SKILL.md.

Two-phase pipeline:
  Phase 1 — Keyword-based relevance filter (conservative, high-recall):
            keeps papers mentioning LLM/AI + code/program/software.
  Phase 2 — Claude-based labeling via AWS Bedrock:
            reads abstract, assigns hierarchical labels from the taxonomy.

Usage:
    # Phase 1 only (keyword filter, no API needed):
    python label_papers.py extracted.json --phase filter --output filtered.json

    # Phase 2 (label with Claude via Bedrock, requires AWS credentials):
    python label_papers.py filtered.json --phase label --output labeled.json

    # Both phases:
    python label_papers.py extracted.json --phase all --output labeled.json

    # Dry-run (show what would be labeled, no API calls):
    python label_papers.py extracted.json --phase all --dry-run

Environment:
    AWS credentials (via ~/.aws/credentials, env vars, or IAM role)
"""

import argparse
import json
import os
import sys
import time

TAXONOMY = {
    "Code Generation": [
        "Program Synthesis",
        "Code Completion",
        "Program Repair",
        "Code Translation",
        "Decompilation",
        "Refactoring",
    ],
    "Static Analysis": [
        "Bug Detection",
        "Program Verification",
        "Specification Inference",
        "Pointer Analysis",
        "Call Graph Analysis",
        "Type Inference",
        "Data-flow Analysis",
        "Taint Analysis",
        "Symbolic Execution",
        "Abstract Interpretation",
        "Code Summarization",
        "Code Search",
        "Clone Detection",
    ],
    "Dynamic Analysis": [
        "Test Case Generation",
        "Test Oracle",
        "Fuzzing",
        "Debugging",
        "Mutation Testing",
        "Bug Reproduction",
        "Domain-Specific Testing",
        "PoC and Exploit Generation",
    ],
    "Model Safety and Security": [
        "Adversarial Attack",
        "Backdoor Detection",
        "Memorization",
        "Secure Code Generation",
        "Watermarking",
        "Jailbreaking",
    ],
    "Agent Safety and Security": [
        "Prompt Injection",
        "Agent Defense",
        "Access Control",
    ],
    "Agent Design": [
        "Planning",
        "Memory Management",
        "Tool Use",
        "Multi-Agent",
    ],
    "Code Model": [
        "Model Training",
        "Binary and IR Model",
    ],
    "Other SE Tasks": [
        "Code Review",
        "Doc/Comment/Commit Message Generation",
        "Log Analysis",
    ],
    "Evaluation": [
        "Benchmark",
        "Empirical Study",
        "Survey",
    ],
}

ALL_LABELS = []
for top, subs in TAXONOMY.items():
    for sub in subs:
        ALL_LABELS.append(f"{top}, {sub}")

TAXONOMY_STR = json.dumps(TAXONOMY, indent=2)

# ── Phase 1: keyword-based relevance filter ──────────────────────────────────

LLM_KEYWORDS = [
    "large language model", "llm",
    "gpt", "chatgpt", "copilot", "codex", "codebert", "codet5",
    "code llama", "deepseek", "starcoder", "incoder",
    "codegen", "codegemma", "qwen-coder", "wizardcoder",
    "generative ai", "genai", "foundation model",
    "prompt", "in-context learning", "few-shot", "zero-shot",
    "chain-of-thought", "chain of thought",
    "reinforcement learning from human", "rlhf",
    "code model", "language model for code",
    "ai agent", "llm agent", "llm-based", "llm-powered",
    "ai-assisted", "ai-driven",
]

CODE_KEYWORDS = [
    "code", "program", "software", "compiler", "compilation",
    "bug", "vulnerabilit", "exploit", "malware",
    "static analysis", "dynamic analysis", "fuzzing", "fuzz",
    "testing", "test generation", "debugging", "fault",
    "verification", "proof", "invariant", "assertion",
    "type inference", "type check", "type system",
    "decompil", "disassembl", "binary analysis", "reverse engineer",
    "patch", "repair", "fix",
    "refactor", "code review", "code search", "code summar",
    "code generat", "code complet", "code translat",
    "program synthe", "program repair", "program analy",
    "smart contract", "solidity",
    "api", "library", "dependency", "supply chain",
    "repository", "commit", "pull request",
    "source code", "abstract syntax tree", "ast",
    "control flow", "data flow", "call graph", "pointer analysis",
    "agent", "tool use", "autonomous",
    "security", "attack", "adversarial", "backdoor", "poison",
    "jailbreak", "injection", "red team",
    "watermark", "memoriz", "contamina",
    "benchmark", "evaluat",
    "IDE", "developer",
]


def is_relevant(title, abstract):
    text = (title + " " + abstract).lower()
    has_llm = any(kw in text for kw in LLM_KEYWORDS)
    has_code = any(kw in text for kw in CODE_KEYWORDS)
    return has_llm and has_code


def filter_papers(papers):
    filtered = {}
    for title, entry in papers.items():
        abstract = entry.get("abstract", "")
        if is_relevant(title, abstract):
            filtered[title] = entry
    return filtered


# ── Phase 2: Claude-based labeling via Bedrock ────────────────────────────────

SYSTEM_PROMPT = """You are a senior CS researcher specializing in large language models for code.
Your task is to determine whether a paper is centrally about LLMs/Agents for software engineering, and if so, classify it.

STRICT RELEVANCE CRITERIA — a paper is relevant ONLY if it meets ALL of the following:
1. The paper's OWN proposed method, system, or research subject must centrally involve Large Language Models (LLMs), pre-trained code models, or AI agents.
2. The application domain must be software engineering (code generation, program analysis, testing, repair, security, etc.) OR the paper must study properties of code LLMs/agents themselves (safety, security, benchmarking, training).

A paper is NOT relevant if:
- It only mentions LLMs/agents/neural networks in the background, related work, or motivation — but the paper's own contribution does NOT use or study LLMs/agents.
- It uses traditional ML (SVM, random forest, logistic regression), traditional deep learning (CNN, RNN, GNN), or non-LLM neural networks as its primary method — even if applied to SE tasks. Only include these if they specifically target code LLMs (e.g., adversarial attacks on code models, training code models).
- It is about general NLP, vision, speech, or other non-code tasks — even if it uses LLMs.
- It is about neural network verification, ML compilers, tensor optimization, quantum computing, or pure PL theory.
- It is a general software engineering paper that does not use LLMs/agents as a core component.

Examples of RELEVANT papers:
- "We use GPT-4 to generate unit tests..." → RELEVANT (LLM applied to SE)
- "We fine-tune CodeBERT for vulnerability detection..." → RELEVANT (code LLM applied to SE)
- "We study jailbreak attacks on code generation models..." → RELEVANT (studying code LLM properties)
- "We build an LLM-based agent for automated debugging..." → RELEVANT (LLM agent for SE)
- "We propose a benchmark for evaluating LLM code generation..." → RELEVANT (evaluating code LLMs)

Examples of NOT_RELEVANT papers:
- "We use GNN to detect bugs in programs..." → NOT_RELEVANT (traditional DL, not LLM)
- "We propose a fuzzing technique... we compare with ChatGPT as baseline..." → NOT_RELEVANT (LLM only as baseline comparison)
- "We train a CNN for malware detection..." → NOT_RELEVANT (traditional DL)
- "Automated program repair using genetic programming..." → NOT_RELEVANT (not LLM-based)
- "We use machine learning to predict software defects..." → NOT_RELEVANT (traditional ML)
- "Our method uses reinforcement learning for test generation..." → NOT_RELEVANT (RL, not LLM) unless the RL is applied to fine-tune an LLM

If the abstract does NOT clearly show that LLMs or AI agents are a CENTRAL part of the paper's own contribution, respond with exactly: NOT_RELEVANT

LABELING RULES (only if the paper IS relevant):
1. Assign labels as "TopLevel, SubLevel" pairs. A paper can have multiple labels.
2. Only use labels from the provided taxonomy. Do not invent new labels.
3. Always include the most specific applicable sub-level labels.
4. Be precise: only assign a label if the paper clearly fits that category.

TAXONOMY:
""" + TAXONOMY_STR

USER_PROMPT_TEMPLATE = """Classify this paper. Return ONLY a JSON array of label strings, or "NOT_RELEVANT".
Each label string must be in the format "TopLevel, SubLevel" from the taxonomy.

Title: {title}

Abstract: {abstract}

Output (JSON array or NOT_RELEVANT):"""


def label_with_claude(papers, model="us.anthropic.claude-sonnet-4-6", region="us-east-1", delay=0.5):
    try:
        import boto3
    except ImportError:
        print("Error: pip install boto3  (required for Bedrock)", file=sys.stderr)
        sys.exit(1)

    client = boto3.client("bedrock-runtime", region_name=region)
    labeled = {}
    total = len(papers)

    for i, (title, entry) in enumerate(papers.items()):
        abstract = entry.get("abstract", "")
        if not abstract.strip():
            print(f"  [{i+1}/{total}] SKIP (no abstract): {title[:60]}", file=sys.stderr)
            continue

        user_msg = USER_PROMPT_TEMPLATE.format(title=title, abstract=abstract)

        try:
            response = client.converse(
                modelId=model,
                system=[{"text": SYSTEM_PROMPT}],
                messages=[{"role": "user", "content": [{"text": user_msg}]}],
                inferenceConfig={"maxTokens": 512, "temperature": 0.0},
            )
            output = response["output"]["message"]["content"][0]["text"].strip()
        except Exception as e:
            print(f"  [{i+1}/{total}] ERROR: {title[:60]} — {e}", file=sys.stderr)
            if "ThrottlingException" in str(e):
                time.sleep(5)
            continue

        if "NOT_RELEVANT" in output:
            print(f"  [{i+1}/{total}] NOT_RELEVANT: {title[:60]}", file=sys.stderr)
            continue

        try:
            raw = output
            if "```" in raw:
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]
            labels_raw = json.loads(raw)
            if not isinstance(labels_raw, list):
                labels_raw = [labels_raw]

            valid_labels = [l for l in labels_raw if l in ALL_LABELS]
            if not valid_labels:
                print(f"  [{i+1}/{total}] NO_VALID_LABELS: {title[:60]} — raw: {output[:100]}", file=sys.stderr)
                continue

            flat_labels = []
            seen = set()
            for label in valid_labels:
                top, sub = label.split(", ", 1)
                if top not in seen:
                    flat_labels.append(top)
                    seen.add(top)
                if sub not in seen:
                    flat_labels.append(sub)
                    seen.add(sub)

            entry_copy = dict(entry)
            entry_copy["labels"] = flat_labels
            labeled[title] = entry_copy
            print(f"  [{i+1}/{total}] OK: {title[:60]} -> {flat_labels}", file=sys.stderr)

        except (json.JSONDecodeError, ValueError) as e:
            print(f"  [{i+1}/{total}] PARSE_ERROR: {title[:60]} — {output[:100]}", file=sys.stderr)
            continue

        if delay > 0:
            time.sleep(delay)

    return labeled


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Label papers using taxonomy")
    parser.add_argument("input", help="Input JSON (from extract_papers.py)")
    parser.add_argument("--output", "-o", help="Output JSON path")
    parser.add_argument("--phase", choices=["filter", "label", "all"], default="all",
                        help="Pipeline phase (default: all)")
    parser.add_argument("--model", default="us.anthropic.claude-sonnet-4-6",
                        help="Bedrock model ID (default: us.anthropic.claude-sonnet-4-6)")
    parser.add_argument("--region", default="us-east-1",
                        help="AWS region for Bedrock (default: us-east-1)")
    parser.add_argument("--delay", type=float, default=0.5,
                        help="Delay between API calls in seconds")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be labeled without calling API")
    args = parser.parse_args()

    with open(args.input) as f:
        papers = json.load(f)
    print(f"Loaded {len(papers)} papers from {args.input}", file=sys.stderr)

    # Phase 1: filter
    if args.phase in ("filter", "all"):
        papers = filter_papers(papers)
        print(f"After keyword filter: {len(papers)} papers", file=sys.stderr)

    if args.phase == "filter" or args.dry_run:
        if args.dry_run:
            print(f"\n=== DRY RUN: {len(papers)} papers would be sent for labeling ===", file=sys.stderr)
            for title in list(papers.keys())[:20]:
                print(f"  - {title}", file=sys.stderr)
            if len(papers) > 20:
                print(f"  ... and {len(papers) - 20} more", file=sys.stderr)

        if args.output:
            with open(args.output, "w") as f:
                json.dump(papers, f, indent=2, ensure_ascii=False)
            print(f"Written to {args.output}", file=sys.stderr)
        else:
            json.dump(papers, sys.stdout, indent=2, ensure_ascii=False)
        return

    # Phase 2: label
    labeled = label_with_claude(papers, model=args.model, region=args.region, delay=args.delay)
    print(f"\nLabeled {len(labeled)} papers (of {len(papers)} filtered)", file=sys.stderr)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(labeled, f, indent=2, ensure_ascii=False)
        print(f"Written to {args.output}", file=sys.stderr)
    else:
        json.dump(labeled, sys.stdout, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
