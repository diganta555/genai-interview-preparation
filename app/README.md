# Development API

This is an in-memory lexical/extractive reference. It is not production authentication, persistent storage, or a live LLM service.

```bash
uv sync --extra api
```

Set DEMO_API_KEY to a locally chosen development credential, then run:

```bash
uv run uvicorn app.main:app --host 127.0.0.1 --port 8000
```

In PowerShell use `$env:DEMO_API_KEY = "your-local-development-value"`. In Bash use `export DEMO_API_KEY='your-local-development-value'`. Do not commit real credentials. The Python app reads process environment; it does not automatically load .env.

Open http://127.0.0.1:8000/docs. Query requests need `Authorization: Bearer YOUR_LOCAL_VALUE`. POST /query accepts `{ "question": "refund receipt" }`. POST /sources accepts source_id, version, and text. Tenant identity is fixed by the development credential, not request arguments. Source data resets on restart and vocabulary remains fixed from the initial synthetic corpus.

## Compose

Copy .env.example to .env, fill DEMO_API_KEY and a local POSTGRES_PASSWORD, then run `docker compose up --build`. The frontend is at http://127.0.0.1:8080. Enter your local development key there; it is not stored in JavaScript. PostgreSQL, Redis, and Qdrant are companion integration exercises; the default API does not connect to them. Image tags are development examples, not claims of latest versions or production hardening.

## Production integration

Follow the capstone to add real identity verification, permissions, durable stores, real embeddings, model adapters, shared rate control, deadlines, streaming, tracing, and measured evaluations. Optional dependency installation and Docker execution were not available in the authoring environment; test them locally before using those integrations.
