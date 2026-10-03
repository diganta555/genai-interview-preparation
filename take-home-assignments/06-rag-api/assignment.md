# Assignment: Production-Style RAG API

Read this first and implement before opening solution.md.

## Requirements

Add real identity, permissions, durable ingestion, deadlines, shared rate control, tracing, evaluation, and deployment recovery to a RAG service.

## Constraints

Python 3.12; synthetic data first; no credentials in Git; hard permissions in code; bounded tool/model calls. The offline baseline is allowed, but clearly distinguish it from live integrations. State your time and deployment assumptions.

## Expected APIs

POST /sources; GET /jobs/{id}; POST /query; GET /health/ready.

## Expected architecture

Gateway → identity → retrieval/model/tools → validation → safe telemetry; separate ingestion queue.

## Test cases

Try restart, partial ingestion, revoked ACL, malformed token, provider outage, rate limits, canceled stream, and restore.

## Evaluation criteria

Correctness 30%; validation and security 25%; failure handling 15%; tests and evaluation 15%; architecture explanation and documentation 15%. These are exercise grading weights, not an employer’s official rubric.

## Production considerations

Explain data lifecycle, identity, deadlines, quotas, telemetry, deployment, and rollback. Show at least one measured result with the exact configuration and one remaining limitation.

## Submission

README, runnable baseline, meaningful tests, example requests, per-case report, architecture decisions, and no real secrets. Commit your attempt before reading the separate solution guidance.
