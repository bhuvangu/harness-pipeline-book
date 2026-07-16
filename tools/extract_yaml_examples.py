#!/usr/bin/env python3
"""extract_yaml_examples.py: pull fenced ```yaml blocks from in-scope docs into
corpus/yaml_examples/, one file per source doc, with citation headers.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "corpus" / "developer-hub" / "docs"
OUT = ROOT / "corpus" / "yaml_examples"
FENCE = re.compile(r"```ya?ml\s*\n(.*?)```", re.DOTALL)

def main() -> int:
    OUT.mkdir(exist_ok=True)
    n_files = n_blocks = 0
    for p in sorted(DOCS.rglob("*")):
        if p.suffix not in (".md", ".mdx"):
            continue
        blocks = FENCE.findall(p.read_text(encoding="utf-8", errors="replace"))
        blocks = [b for b in blocks if len(b.strip()) > 40]  # skip trivial snippets
        if not blocks:
            continue
        rel = p.relative_to(DOCS)
        dest = OUT / (str(rel).replace("/", "__") + ".yaml")
        parts = [f"# source: docs/{rel}  (https://developer.harness.io/docs/{rel.with_suffix('')})"]
        for i, b in enumerate(blocks, 1):
            parts.append(f"# --- example {i} ---\n{b.rstrip()}")
        dest.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
        n_files += 1
        n_blocks += len(blocks)
    print(f"extracted {n_blocks} yaml blocks from {n_files} docs -> {OUT}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
