# Solution guidance: Multi-Agent Research

This is a reference solution path, not a claim that all live service integrations are already implemented.

1. Define the request, response, and error contracts from the assignment.
2. Use the [Multi-Agent Research project guide](../../projects/08-multi-agent/README.md) for schema, API, and implementation milestones.
3. Run `python projects/08-multi-agent/demo.py` from the repository root to inspect the implemented core mechanism.
4. Validate inputs and derive identity from trusted authentication. Add permissions before live data.
5. Implement the proposed persistence and external adapters; keep fake adapters for deterministic tests.
6. Enforce deadlines and budgets, preserve provenance or operation IDs, and classify failures.
7. Test: Try unavailable worker, conflicting claims, duplicate sources, circular validation, delegation loop, and exhausted budget.
8. Compare the complete result with expected authoritative outcomes. Explain any semantic checks requiring human review.
9. Package and test the deployment separately from pure Python code. Record what was actually run.

## Acceptance review

A solution passes only if the stated tests and permissions work, the data and action outcomes match expectations, and the documented scope matches the implementation. A fluent final response alone is insufficient. See the project guide for a complete breakdown of architecture, tests, evaluation, and deployment decisions.
