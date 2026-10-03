# GenAI Interview Preparation

A written, practical reference for GenAI, LLM, RAG, agent, backend, and applied AI engineering interviews. Read any topic when you need it; study the sequence when building foundations.

**30 modules · 530 interview-bank entries · 200 mock prompts · 10 project guides · 6 take-home assignments · 8 worked system designs**

The material starts with simple explanations and continues through mechanisms, scenarios, code, interview answers, exercises, and production trade-offs. It is designed to help you answer: **“How would you build and debug this in a real system?”**

## Start here

1. Read the [learning roadmap](00-roadmap/learning-roadmap.md), then choose the [30/60/90-day plan](00-roadmap/daily-plans.md).
2. Open the module below. Read the concepts, run its example, and solve the exercise.
3. Answer the module case before reading the expected answer.
4. Build one [portfolio project](projects/README.md), record actual evidence, and practice [mock interviews](mock-interviews/README.md).
5. Use the [checklist](00-roadmap/checklist.md) to record confidence and implementation progress.

## Complete module index

| Module | Topic | Example |
|---|---|---|
| 01 | [Python for GenAI](01-python/README.md) | async_batch.py |
| 02 | [Machine Learning Fundamentals](02-ml-fundamentals/README.md) | metrics.py |
| 03 | [Deep Learning Fundamentals](03-deep-learning/README.md) | gradient.py |
| 04 | [Transformers](04-transformers/README.md) | attention.py |
| 05 | [LLM Fundamentals](05-llm-fundamentals/README.md) | cost.py |
| 06 | [Prompt Engineering](06-prompt-engineering/README.md) | prompts.py |
| 07 | [Embeddings and Similarity](07-embeddings/README.md) | vectors.py |
| 08 | [Vector Databases](08-vector-databases/README.md) | vector_crud.py |
| 09 | [Retrieval-Augmented Generation](09-rag/README.md) | rag.py |
| 10 | [Advanced RAG and Scale](10-advanced-rag/README.md) | hybrid.py |
| 11 | [LangChain](11-langchain/README.md) | langchain_example.py |
| 12 | [Custom Tools](12-tools/README.md) | tools.py |
| 13 | [Function Calling and Tool Calling](13-function-calling/README.md) | tool_loop.py |
| 14 | [LangGraph](14-langgraph/README.md) | langgraph_example.py |
| 15 | [AI Agents](15-agents/README.md) | agent.py |
| 16 | [Memory](16-memory/README.md) | memory.py |
| 17 | [Multi-Agent Systems](17-multi-agent/README.md) | multi_agent.py |
| 18 | [Fine-Tuning](18-fine-tuning/README.md) | dataset.py |
| 19 | [LLM and Agent Evaluation](19-llm-evaluation/README.md) | evaluate.py |
| 20 | [LLM Observability](20-observability/README.md) | trace.py |
| 21 | [Guardrails and Security](21-security/README.md) | security.py |
| 22 | [LLM Cost Optimization](22-cost-optimization/README.md) | router.py |
| 23 | [LLM System Design](23-system-design/README.md) | capacity.py |
| 24 | [Production GenAI Services](24-production/README.md) | reliability.py |
| 25 | [Docker and Deployment](25-docker/README.md) | deployment_check.py |
| 26 | [AWS for GenAI](26-aws/README.md) | bedrock_example.py |
| 27 | [Databases and GenAI](27-database/README.md) | sql.py |
| 28 | [Real-World Debugging](28-debugging/README.md) | debug.py |
| 29 | [GenAI Coding Interviews](29-coding-interview/README.md) | coding.py |
| 30 | [Project-Based Interview Preparation](30-projects/README.md) | portfolio.py |

## Read by goal

- **RAG interviews:** modules 07–10, 19, 21, 23, and 28.
- **Agent interviews:** modules 12–17, 19, 21, and 24.
- **Production and AWS:** modules 20–28 and the [capstone](capstone/README.md).
- **Hands-on coding:** [examples](examples/README.md), [challenges](coding-challenges/README.md), and [tests](tests/test_core.py).
- **Fast review:** [cheat sheets](cheat-sheets/README.md), [glossary](resources/glossary.md), and [question banks](interview-questions/README.md).

## Quick run without API keys

```bash
python -m examples.rag
python -m examples.evaluate
python -m unittest discover -s tests -v
python scripts/mock_interview.py --round 1
```

The offline implementation uses **lexical vectors and extractive fixture answers**. It demonstrates software boundaries without model downloads or API charges. Real embedding, model, LangChain, LangGraph, Chroma, LlamaIndex, and Bedrock examples are separate optional integrations.

## Technologies

Python, SQL, Bash, FastAPI, Pydantic, async programming, LangChain, LangGraph, LlamaIndex, hosted and local models, embeddings, FAISS, Chroma, Pinecone, Qdrant, Weaviate, PostgreSQL, MySQL, Redis, Docker, AWS, evaluation, tracing, and CI concepts. Coverage is explained in [coverage.md](resources/coverage.md); not every discussed service has an implemented live adapter.

## Portfolio and capstone

Ten project guides include requirements, architecture, schema, APIs, implementation milestones, test criteria, evaluation, deployment, interview discussion, and honest resume-bullet templates. The [Enterprise AI Knowledge Platform](capstone/README.md) combines them through explicit integration milestones.

Project demo scripts are runnable learning references, not ten fully deployed production systems. The Compose stack provisions companion services for integration exercises. The default API uses the offline reference and does not claim those services are already integrated.

## Interview methodology

Use concise first answers, then explain WHY, WHEN, HOW, trade-offs, failure modes, and production considerations. Question banks organize the concepts through deployment, incident, evaluation, trade-off, and security lenses. Related entries intentionally revisit a concept from different angles; they are a study reference, not an empirical list of employer questions.

The CLI asks one mock question at a time and hides the answer until you respond. It provides an answer key and a human self-scoring rubric; it does not pretend keyword matching can grade professional competence. [Chat mock protocol](mock-interviews/chat-protocol.md) lets a human or assistant conduct a deeper session.

## Git and GitHub

See [Git workflow](00-roadmap/git-workflow.md) to upload this repository. No remote GitHub repository has been created automatically.

## Validation and source maintenance

See [VALIDATION.md](VALIDATION.md) for executed checks and optional integration limits. Reference links are in [official sources](resources/official-sources.md). Model names, pricing, cloud limits, and SDK APIs change; configure model IDs and check official references before deployment. Original explanations are provided here so the repository can be read offline.

License: [MIT](LICENSE). Contributing: [CONTRIBUTING.md](CONTRIBUTING.md).
