# Running the examples

Use Python 3.12 or newer. Run all commands from the repository root.

## Offline core

`python -m examples.rag` runs lexical retrieval plus an extractive answer fixture. It demonstrates contracts, provenance, abstention, and tenant filtering. It is **not** a semantic embedding model or generative LLM. Unknown vocabulary is ignored; low-overlap questions can retrieve weak matches. Do not use it as a production answer system.

`python -m examples.evaluate --output outputs/evaluation.json` runs structural and retrieval checks on four synthetic cases. Citation availability does not prove that a citation supports a claim. Semantic review is explicitly unperformed.

`python -m unittest discover -s tests -v` runs offline tests without credentials. Most numbered module examples use only the standard library. Async examples use Python 3.12 TaskGroup and timeout.

## Optional integrations

| Command | Install | External requirement |
|---|---|---|
| `python -m examples.langchain_example` | `uv sync --extra frameworks` | None; fake model |
| `python -m examples.langgraph_example` | `uv sync --extra frameworks` | None; in-memory checkpointer |
| `python -m examples.chroma_crud` | `uv sync --extra vectors` | None; explicit vectors |
| `python -m examples.semantic_search` | `uv sync --extra embeddings` | Model download on first run |
| `python -m examples.live_models` | frameworks + provider package | Your configured model credentials; charges may apply |
| `python -m examples.llamaindex_example` | `uv sync --extra llamaindex` | Downloaded embedding model and a running Ollama model |
| `python -m examples.bedrock_example` | `uv sync --extra aws` | Your authorized AWS identity, region, model ID |
| `uvicorn app.main:app --reload` | `uv sync --extra api` | Local development API key |

Provider packages: `langchain-openai`, `langchain-anthropic`, `langchain-google-genai`, `langchain-groq`, `langchain-ollama`, or `langchain-huggingface`. Configure GENAI_PROVIDER and GENAI_MODEL with a model available in your account. Supported parameter names and capabilities vary. Use provider documentation and contract tests.

Real local embeddings are an additional lab; they are not silently enabled in the default API. LlamaIndex uses explicit model and embedding objects to avoid accidental default-provider calls. Optional integrations were authored against official references; see VALIDATION.md for actual execution status.

## Reproducibility

The starter pyproject specifies compatibility ranges rather than claiming a fabricated resolved lock. Run `uv lock`, test your chosen extras, and commit the generated uv.lock before deploying. Keep the default offline suite independent of external calls. Record Python and installed package versions with experiment results.
