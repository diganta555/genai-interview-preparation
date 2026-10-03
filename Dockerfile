FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md ./
# Learning compatibility ranges. Replace with a tested lock for production.
RUN pip install --no-cache-dir "fastapi>=0.115,<1" "uvicorn>=0.30,<1" "pydantic>=2,<3"
COPY examples ./examples
COPY app ./app
RUN useradd --create-home --uid 10001 learner
USER learner
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
