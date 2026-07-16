#!/usr/bin/env python3
"""filter_openapi.py: reduce the full Harness OpenAPI spec to pipeline-domain paths.
Outputs:
  corpus/openapi_pipeline.yaml  filtered spec (paths only, plus info)
  corpus/entity_schemas.md      identifier regexes, required fields, enums for key schemas
  corpus/path_tree.txt          nested URL structure (ownership evidence)
"""
import re, sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pip install pyyaml first", file=sys.stderr); sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "corpus" / "openapi" / "index.yaml"
CORPUS = ROOT / "corpus"

KEEP = re.compile(
    r"pipeline|input.?set|trigger|execut|approval|service|environment|"
    r"infrastructure|connector|secret|delegate|template|variable|webhook|freeze|rollback",
    re.IGNORECASE,
)
DROP = re.compile(  # noise that matches KEEP words but is out of scope
    r"ccm|chaos|sto/|/sei|gitops|idp|cf/|feature.?flag|har/api|dbops|dbschema|ssca|cet",
    re.IGNORECASE,
)

def main() -> int:
    print(f"loading {SPEC} ...")
    spec = yaml.safe_load(SPEC.read_text(encoding="utf-8", errors="replace"))
    paths = spec.get("paths", {})
    kept = {p: ops for p, ops in paths.items() if KEEP.search(p) and not DROP.search(p)}
    print(f"paths: {len(paths)} total -> {len(kept)} kept")

    out = {"openapi": spec.get("openapi", "3.0.0"), "info": spec.get("info", {}), "paths": kept}
    (CORPUS / "openapi_pipeline.yaml").write_text(
        yaml.safe_dump(out, sort_keys=False, width=100), encoding="utf-8")

    # path tree: nesting is ownership evidence
    lines = []
    for p in sorted(kept):
        depth = p.count("/") - 1
        lines.append("  " * max(depth, 0) + p)
    (CORPUS / "path_tree.txt").write_text("\n".join(sorted(kept)), encoding="utf-8")

    # schema digest for key entities
    schemas = (spec.get("components") or {}).get("schemas") or {}
    wanted = {n: s for n, s in schemas.items() if KEEP.search(n) and not DROP.search(n)}
    md = ["# Entity schema digest (from OpenAPI spec)\n"]
    for name in sorted(wanted):
        s = wanted[name] or {}
        props = s.get("properties") or {}
        md.append(f"## {name}")
        if s.get("description"):
            md.append(f"> {s['description']}")
        req = s.get("required") or []
        if req:
            md.append(f"- required: {', '.join(req)}")
        for pname, pdef in props.items():
            if not isinstance(pdef, dict):
                continue
            bits = [pdef.get("type", "obj")]
            if "pattern" in pdef: bits.append(f"pattern `{pdef['pattern']}`")
            if "enum" in pdef: bits.append("enum: " + ", ".join(map(str, pdef["enum"][:12])))
            if "maxLength" in pdef: bits.append(f"maxLen {pdef['maxLength']}")
            md.append(f"- `{pname}`: " + "; ".join(bits))
        md.append("")
    (CORPUS / "entity_schemas.md").write_text("\n".join(md), encoding="utf-8")
    print(f"schemas: {len(schemas)} total -> {len(wanted)} kept -> corpus/entity_schemas.md")
    return 0

if __name__ == "__main__":
    sys.exit(main())
