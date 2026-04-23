#!/usr/bin/env python3
"""
Import papers from original.json that are missing from labeldata.json.

Maps old-style labels from original.json to the current two-level taxonomy,
then uses Claude via Bedrock to refine labels using both the abstract and
the old labels as hints.

Usage:
    # Dry-run: show what would be imported
    python import_original.py --dry-run

    # Import with Claude relabeling
    python import_original.py -o /tmp/original_relabeled.json

    # Skip Claude and just use label mapping
    python import_original.py -o /tmp/original_relabeled.json --map-only
"""

import argparse
import json
import os
import sys
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR))))
ORIGINAL_PATH = os.path.join(REPO_ROOT, "data", "rawdata", "original.json")
LABELDATA_PATH = os.path.join(REPO_ROOT, "data", "labeldata", "labeldata.json")

sys.path.insert(0, SCRIPT_DIR)
from label_papers import TAXONOMY, ALL_LABELS, SYSTEM_PROMPT

# Mapping from old labels to new taxonomy labels
OLD_TO_NEW = {
    "code generation": "Code Generation",
    "program synthesis": "Program Synthesis",
    "code completion": "Code Completion",
    "program repair": "Program Repair",
    "program transformation": "Code Translation",
    "program decompilation": "Decompilation",
    "program optimization": "Refactoring",
    "static analysis": "Static Analysis",
    "bug detection": "Bug Detection",
    "program verification": "Program Verification",
    "specification inference": "Specification Inference",
    "pointer analysis": "Pointer Analysis",
    "call graph analysis": "Call Graph Analysis",
    "type inference": "Type Inference",
    "data-flow analysis": "Data-flow Analysis",
    "symbolic execution": "Symbolic Execution",
    "abstract interpretation": "Abstract Interpretation",
    "code summarization": "Code Summarization",
    "code search": "Code Search",
    "code similarity analysis": "Clone Detection",
    "syntactic analysis": "Clone Detection",
    "program testing": "Dynamic Analysis",
    "general testing": "Dynamic Analysis",
    "unit testing": "Test Case Generation",
    "fuzzing": "Fuzzing",
    "protocol fuzzing": "Fuzzing",
    "debugging": "Debugging",
    "mutation testing": "Mutation Testing",
    "bug reproduction": "Bug Reproduction",
    "DBMS testing": "Domain-Specific Testing",
    "GUI testing": "Domain-Specific Testing",
    "compiler testing": "Domain-Specific Testing",
    "library testing": "Domain-Specific Testing",
    "differential testing": "Domain-Specific Testing",
    "vulnerability exploitation": "PoC and Exploit Generation",
    "code model": "Code Model",
    "code model training": "Model Training",
    "source code model": "Model Training",
    "binary code model": "Binary and IR Model",
    "IR code model": "Binary and IR Model",
    "code model security": "Model Safety and Security",
    "code model robustness": "Adversarial Attack",
    "agent security": "Agent Safety and Security",
    "agent design": "Agent Design",
    "planning": "Planning",
    "retrieval-augmented generation": "Memory Management",
    "prompt strategy": "Agent Design",
    "sampling and ranking": "Agent Design",
    "code review": "Code Review",
    "commit message generation": "Doc/Comment/Commit Message Generation",
    "documentation generation": "Doc/Comment/Commit Message Generation",
    "system log analysis": "Log Analysis",
    "benchmark": "Benchmark",
    "empirical study": "Empirical Study",
    "survey": "Survey",
    "equivalence checking": "Program Verification",
    "software composition analysis": "Bug Detection",
    "software maintenance and deployment": "Other SE Tasks",
    "software configuration": "Other SE Tasks",
    "general coding task": None,
    "hallucination in reasoning": None,
    "PL design for LLMs": None,
    "reason with code": None,
}

# Labels that are top-level in the new taxonomy
TOP_LABELS = set(TAXONOMY.keys())
# Labels that are sub-level
SUB_LABELS = {}
for top, subs in TAXONOMY.items():
    for sub in subs:
        SUB_LABELS[sub] = top


def map_labels(old_labels):
    """Map old-style labels to new taxonomy labels."""
    new_labels = set()
    for old in old_labels:
        mapped = OLD_TO_NEW.get(old)
        if mapped is None:
            continue
        new_labels.add(mapped)

    # Ensure top-level labels are included for each sub-level
    final = set()
    for label in new_labels:
        if label in SUB_LABELS:
            final.add(SUB_LABELS[label])
            final.add(label)
        elif label in TOP_LABELS:
            final.add(label)

    return list(final)


RELABEL_USER_PROMPT = """Classify this paper. The paper was previously labeled with these old labels: {old_labels}
Use these old labels as hints, but assign labels strictly from the current taxonomy.
Return ONLY a JSON array of "TopLevel, SubLevel" label strings, or "NOT_RELEVANT".

Title: {title}

Abstract: {abstract}

Output (JSON array or NOT_RELEVANT):"""


def relabel_with_claude(papers, model="us.anthropic.claude-sonnet-4-6", region="us-east-1", delay=0.3):
    try:
        import boto3
    except ImportError:
        print("Error: pip install boto3", file=sys.stderr)
        sys.exit(1)

    client = boto3.client("bedrock-runtime", region_name=region)
    labeled = {}
    total = len(papers)

    for i, (title, entry) in enumerate(papers.items()):
        abstract = entry.get("abstract", "")
        old_labels = entry.get("labels", [])

        if not abstract.strip():
            print(f"  [{i+1}/{total}] SKIP (no abstract): {title[:60]}", file=sys.stderr)
            continue

        user_msg = RELABEL_USER_PROMPT.format(
            title=title, abstract=abstract,
            old_labels=", ".join(old_labels)
        )

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
                # Fall back to mapped labels
                mapped = map_labels(old_labels)
                if mapped:
                    entry_copy = dict(entry)
                    entry_copy["labels"] = mapped
                    labeled[title] = entry_copy
                    print(f"  [{i+1}/{total}] MAPPED: {title[:60]} -> {mapped}", file=sys.stderr)
                else:
                    print(f"  [{i+1}/{total}] NO_VALID_LABELS: {title[:60]}", file=sys.stderr)
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

        except (json.JSONDecodeError, ValueError):
            mapped = map_labels(old_labels)
            if mapped:
                entry_copy = dict(entry)
                entry_copy["labels"] = mapped
                labeled[title] = entry_copy
                print(f"  [{i+1}/{total}] PARSE_ERR->MAPPED: {title[:60]} -> {mapped}", file=sys.stderr)
            else:
                print(f"  [{i+1}/{total}] PARSE_ERROR: {title[:60]}", file=sys.stderr)
            continue

        if delay > 0:
            time.sleep(delay)

    return labeled


def main():
    parser = argparse.ArgumentParser(description="Import papers from original.json")
    parser.add_argument("-o", "--output", help="Output JSON path")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be imported")
    parser.add_argument("--map-only", action="store_true", help="Only use label mapping, no Claude API")
    parser.add_argument("--model", default="us.anthropic.claude-sonnet-4-6")
    parser.add_argument("--region", default="us-east-1")
    parser.add_argument("--delay", type=float, default=0.3)
    args = parser.parse_args()

    with open(ORIGINAL_PATH) as f:
        original = json.load(f)
    with open(LABELDATA_PATH) as f:
        labeldata = json.load(f)

    # Find papers only in original
    missing = {t: original[t] for t in original if t not in labeldata}
    print(f"Original: {len(original)}, Labeldata: {len(labeldata)}, Missing: {len(missing)}", file=sys.stderr)

    if args.dry_run:
        print(f"\n=== DRY RUN: {len(missing)} papers to import ===", file=sys.stderr)
        for title in list(missing.keys())[:20]:
            old_labels = missing[title].get("labels", [])
            mapped = map_labels(old_labels)
            print(f"  {title[:60]}", file=sys.stderr)
            print(f"    old: {old_labels}", file=sys.stderr)
            print(f"    mapped: {mapped}", file=sys.stderr)
        if len(missing) > 20:
            print(f"  ... and {len(missing) - 20} more", file=sys.stderr)
        return

    if args.map_only:
        result = {}
        for title, entry in missing.items():
            mapped = map_labels(entry.get("labels", []))
            if mapped:
                entry_copy = dict(entry)
                entry_copy["labels"] = mapped
                result[title] = entry_copy
        print(f"Mapped {len(result)} papers (of {len(missing)} missing)", file=sys.stderr)
    else:
        result = relabel_with_claude(missing, model=args.model, region=args.region, delay=args.delay)
        print(f"\nLabeled {len(result)} papers (of {len(missing)} missing)", file=sys.stderr)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"Written to {args.output}", file=sys.stderr)
    else:
        json.dump(result, sys.stdout, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
