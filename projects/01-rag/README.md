# Production-Style RAG Application

## Problem statement

Employees need supported answers from a changing policy corpus.

## Requirements

Versioned text/PDF ingestion, caller-scoped retrieval, source-linked answers, and abstention. Start with synthetic non-sensitive data. Define caller roles, expected outputs, failure behavior, latency budget, and acceptable uncertainty before coding.

## Architecture

API receives query → authorized retriever → bounded context → configured model adapter → citation checks.

## Tech stack and implemented scope

Python 3.12 offline reference plus optional FastAPI, Pydantic, relational persistence, vector storage, and model adapters as appropriate. The included demo demonstrates a core mechanism; the milestones below specify the full project implementation. It is not a fully integrated live production application.

## Folder structure

`demo.py` runs the reference. `README.md` is the implementation guide. Shared primitives live in `examples/`; tests in `tests/`; the service reference in `app/`; Compose and Docker files live at the repository root. During development, create project-specific `service/`, `adapters/`, `migrations/`, `tests/`, `data/`, and `reports/` directories.

## Proposed database schema

documents(id, tenant_id, active_version, status); chunks(id, document_id, version, offset, index_revision); jobs(id, status, error_code).

Use explicit primary and foreign keys, tenant-aware indexes, timestamps, and retention rules. Keep source content in object storage when appropriate; derived records should retain source version and provenance.

## API design

POST /documents; GET /jobs/{id}; POST /query with question; response answer, citations, abstention reason.

Identity is supplied by verified authentication. Do not accept user-selected tenant context as proof of authorization. Return structured errors and request IDs. Long tasks use job status instead of blocking indefinitely.

## Run the implemented reference

```bash
python projects/01-rag/demo.py
python -m unittest discover -s tests -v
```

The demo is offline and labeled synthetic or fixture where applicable. For real models and stores, see [optional examples](../../examples/README.md).

## Implementation milestones

1. Define the task contract and seed at least ten normal, missing-data, and forbidden cases.
2. Run the reference, inspect each state transition, and record its limitations.
3. Implement project-specific request and response schemas with strict validation.
4. Add trusted identity and data/action permissions before integrating live data.
5. Implement persistent adapters matching the proposed schema, including migrations and lifecycle updates.
6. Integrate the required model or retrieval adapter with explicit configuration, deadlines, and usage accounting.
7. Preserve evidence and operation IDs through the complete result path.
8. Add integration tests for restart, partial failure, permission changes, and repeated requests.
9. Run the evaluation below and compare a controlled improvement against a fixed baseline.
10. Containerize, deploy to a development environment, load-test, and document rollback and restore.

## Testing

Unit-test pure transformations and validators. Contract-test adapters with recorded fixtures. Integration-test permitted and forbidden requests plus dependency outages. Test empty data, malformed input, oversized input, stale versions, and replayed operations. Avoid live provider calls in the default CI suite.

## Evaluation

Measure: Grounded answer rate, Recall@k, supported citations, ingestion lag, p95 and cost. Record dataset size, labels, configuration, and uncertainty. Evaluate critical slices separately. Do not publish a percentage improvement until you have measured it.

## Docker

Use the root image and Compose stack for the development service reference. Add project adapters and configuration deliberately; companion databases are provisioned but not integrated into the default offline API. Commit a tested dependency lock and use production image digests before release.

## Deployment

Use a reviewed dev environment first. Configure secrets at runtime, deploy with least-privilege workload identity, separate ingestion from interactive traffic, and observe quality and operational metrics. Confirm readiness, cancellation, backup restore, schema migration, and rollback behavior before increasing traffic.

## Failure and senior insight

Parsing quality and source lifecycle usually fail before model prompting. A polished final answer is not proof that the intended operation or evidence check succeeded. Use authoritative records and independent evaluation.

## Interview questions and expected points

**Why this architecture?** Explain the contract, workload, trusted boundaries, and simplest baseline, then justify the added component.

**What fails first under scale?** Estimate data, token, concurrency, and queue workloads; identify a measured bottleneck rather than guessing.

**How do you test it?** Show a representative case, a permission failure, an outage, and actual metrics from the evaluated implementation.

**What would you improve next?** Name a specific measured gap and the experiment that would test the proposed fix.

## Resume bullet templates

- Implemented [actual capability] using [actual stack], with tests for [specific failure and permission boundaries].
- Evaluated [N real or synthetic cases] and measured [actual metric], identifying and fixing [demonstrated cause].
- Designed [architecture decision] to meet [stated requirement], documenting [actual trade-off and limitation].

Replace brackets only with evidence from work you performed. Do not claim deployment, users, uptime, or savings that were not measured.
