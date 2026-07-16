# Harness Pipeline Book

Onboarding project: a Claude Code agent that writes a chaptered, AWS-docs-style
book teaching the Harness pipeline offering (CI/CD) domain model.

- PROMPT.md: the agent prompt. Open Claude Code in this directory and paste it.
- corpus/: frozen learning corpus (docs, filtered OpenAPI spec, schema digest,
  YAML examples, index). Snapshot: 2026-07-16. See corpus/README.md.
- tools/: regeneration scripts. Rerun to refresh the corpus from live sources.
- book/: agent output lands here (gitignored until reviewed, or commit as you go).

Optional: export HARNESS_API_KEY (viewer-role token) before starting to enable
the read-only live API exploration phase. Never commit the key.
