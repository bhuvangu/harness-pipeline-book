# Test Intelligence

Test Intelligence (TI) reduces unit test time by running only the tests that
are relevant to the code changes that triggered the build, instead of the
whole suite.

TI selects tests using three signals: code that changed (queried from Git),
tests that changed, and tests that are new. Changes to files with broad
impact, such as `pom.xml` or `build.gradle`, cause TI to select all tests.
After the build, the build details page shows which tests were selected and
why, including a call-graph visualization.

## How it works

TI has three parts: a Harness-side TI service that maintains call graphs and
commit data, a Test Runner Agent that runs on your build infrastructure, and
the Test step that ties them together. When a Test step starts, the agent
asks the TI service for the selected tests, runs them, and uploads results
plus the updated call graph.

## Requirements and limits

- Unit tests only. Use Run steps for other test types.
- Supported languages: Python, Java, Ruby, C#, Kotlin, Scala. JavaScript
  (Jest) and Kotest are in beta.
- Your Git webhook triggers must include the Synchronize and merge and/or
  close events, or TI's call graph goes stale after merges.
- With parallelism (test splitting), each shard must write a uniquely named
  JUnit file — for example `result_<+strategy.iteration>.xml` — and the
  report path should glob-match all of them.
- To exclude files or tests, add a `.ticonfig.yaml` file to the repository.

---
**Sources:** docs/continuous-integration/use-ci/run-tests/ti-overview.md
(all behavior described).
