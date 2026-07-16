#!/usr/bin/env python3
"""build_doc_index.py: index every in-scope markdown file into corpus/doc_index.csv.
Columns: path, title, description, words. Browse this index; open files on demand.
"""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "corpus" / "developer-hub" / "docs"
OUT = ROOT / "corpus" / "doc_index.csv"

FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

def field(fm: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.MULTILINE)
    return m.group(1).strip().strip("'\"") if m else ""

def main() -> int:
    if not DOCS.is_dir():
        print(f"ERROR: {DOCS} missing; run fetch_sources.sh first", file=sys.stderr)
        return 1
    rows = []
    for p in sorted(DOCS.rglob("*")):
        if p.suffix not in (".md", ".mdx"):
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        fm_match = FRONTMATTER.match(text)
        fm = fm_match.group(1) if fm_match else ""
        title = field(fm, "title")
        if not title:
            h1 = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
            title = h1.group(1).strip() if h1 else p.stem
        rows.append({
            "path": str(p.relative_to(ROOT / "corpus")),
            "title": title,
            "description": field(fm, "description"),
            "words": len(text.split()),
        })
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["path", "title", "description", "words"])
        w.writeheader()
        w.writerows(rows)
    print(f"indexed {len(rows)} files -> {OUT}")
    by_area = {}
    for r in rows:
        area = "/".join(Path(r["path"]).parts[1:3])
        by_area[area] = by_area.get(area, 0) + 1
    for area, n in sorted(by_area.items(), key=lambda kv: -kv[1])[:12]:
        print(f"  {n:5d}  {area}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
