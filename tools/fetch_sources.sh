#!/usr/bin/env bash
# fetch_sources.sh: sparse-clone Harness developer-hub docs and download the OpenAPI spec.
# Idempotent: safe to rerun; refreshes both sources.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CORPUS="$ROOT/corpus"
CLONE_DIR="$CORPUS/developer-hub"
OPENAPI_DIR="$CORPUS/openapi"
mkdir -p "$OPENAPI_DIR"

# --- 1. Sparse clone of the docs repo (blobless + sparse checkout = small) ---
if [ ! -d "$CLONE_DIR/.git" ]; then
  git clone --depth 1 --filter=blob:none --sparse \
    https://github.com/harness/developer-hub.git "$CLONE_DIR"
fi
cd "$CLONE_DIR"
git sparse-checkout set \
  docs/continuous-integration \
  docs/continuous-delivery \
  docs/platform/pipelines \
  docs/platform/triggers \
  docs/platform/connectors \
  docs/platform/secrets \
  docs/platform/delegates \
  docs/platform/templates \
  docs/platform/variables-and-expressions

echo "--- clone stats ---"
find docs -name '*.md' -o -name '*.mdx' | wc -l | xargs echo "markdown files:"
du -sh "$CLONE_DIR"

# --- 2. OpenAPI spec download (try known locations, keep the first that parses) ---
cd "$ROOT"
CANDIDATES=(
  "https://apidocs.harness.io/index.yaml"
  "https://apidocs.harness.io/index.json"
  "https://apidocs.harness.io/_spec/index.yaml"
  "https://apidocs.harness.io/openapi.yaml"
)
GOT=""
for url in "${CANDIDATES[@]}"; do
  echo "trying: $url"
  ext="${url##*.}"
  out="$OPENAPI_DIR/index.$ext"
  if curl -fsSL --max-time 120 "$url" -o "$out"; then
    # sanity check: must mention openapi and paths
    if head -c 2000 "$out" | grep -qi "openapi"; then
      GOT="$out"
      echo "OK -> $out ($(du -h "$out" | cut -f1))"
      break
    else
      echo "downloaded but does not look like an OpenAPI spec, discarding"
      rm -f "$out"
    fi
  else
    echo "failed"
  fi
done

if [ -z "$GOT" ]; then
  echo "ERROR: no OpenAPI spec found at known URLs. Record in open questions." >&2
  exit 1
fi
echo "--- done ---"
