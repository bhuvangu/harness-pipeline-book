# Harness Pipeline Corpus (frozen 2026-07-16)

Pre-fetched, pruned learning corpus for the Harness Pipeline Book agent.
All sources local; the agent needs no network access for Phases 1+.

Contents:
- docs/                  Markdown docs, text only: continuous-integration/,
                         continuous-delivery/, platform/ (pipeline-relevant
                         subtrees). From github.com/harness/developer-hub.
- doc_index.csv          Index of every doc: path, title, description, words.
                         START HERE. Never bulk-read docs/; query this index.
- openapi_pipeline.yaml  Harness OpenAPI 3.0 spec filtered to 476
                         pipeline-relevant paths. Schema/field ground truth.
- entity_schemas.md      Digest of 1381 schemas: required fields, identifier
                         regexes, enums. Quote regexes from here verbatim.
- path_tree.txt          Sorted API path list. URL nesting = ownership evidence.
- yaml_examples/         1582 fenced YAML blocks extracted from the docs, one
                         file per source doc, citation header included. Use
                         these as the annotated examples inside book chapters.

Citation convention: cite docs as their path under docs/ (each maps to
https://developer.harness.io/docs/<path-without-extension>), spec claims as
openapi_pipeline.yaml plus the path or schema name, examples as the
yaml_examples/ filename.
