# Solution guidance: Production-Style RAG API

This is a reference solution path, not a claim that all live service integrations are already implemented.

1. Define the request, response, and error contracts from the assignment.
2. Use the [Production-Style RAG API project guide](../../projects/09-enterprise-rag/README.md) for schema, API, and implementation milestones.
3. Run `python projects/09-enterprise-rag/demo.py` from the repository root to inspect the implemented core mechanism.
4. Validate inputs and derive identity from trusted authentication. Add permissions before live data.
5. Implement the proposed persistence and external adapters; keep fake adapters for deterministic tests.
6. Enforce deadlines and budgets, preserve provenance or operation IDs, and classify failures.
7. Test: Try restart, partial ingestion, revoked ACL, malformed token, provider outage, rate limits, canceled stream, and restore.
8. Compare the complete result with expected authoritative outcomes. Explain any semantic checks requiring human review.
9. Package and test the deployment separately from pure Python code. Record what was actually run.

## Acceptance review

A solution passes only if the stated tests and permissions work, the data and action outcomes match expectations, and the documented scope matches the implementation. A fluent final response alone is insufficient. See the project guide for a complete breakdown of architecture, tests, evaluation, and deployment decisions.
