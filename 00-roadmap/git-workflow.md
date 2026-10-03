# Git and GitHub workflow

## First upload

Extract the ZIP and open a terminal inside genai-interview-preparation. Python 3.12 and Git should be installed.

```bash
git init -b main
git add .
git status
git commit -m "docs: add GenAI learning reference and interview preparation"
```

If Git asks for identity, configure your own name and email with `git config user.name` and `git config user.email`. Create an empty repository named genai-interview-preparation on GitHub. Do not initialize that remote with another README. Copy its URL, then run:

```bash
git remote add origin https://github.com/YOUR_USERNAME/genai-interview-preparation.git
git push -u origin main
```

Replace YOUR_USERNAME with your actual account. Authenticate using GitHub’s supported credential flow; do not put a token in the remote URL or source code.

## Daily work

```bash
git switch main
git pull --ff-only
git switch -c feat/rag-evaluation
python -m unittest discover -s tests -v
git add 09-rag examples tests
git diff --cached
git commit -m "feat: add measured RAG evaluation experiment"
git push -u origin feat/rag-evaluation
```

Open a pull request describing the concrete change, validation, and limitations. Review and merge, then update local main. `git add .` has a space; `git add.` is not a Git command.

## Diverged branches

Read `git status` and `git log --oneline --graph --all -12`. Fetch first. If your unshared local commits should sit on the new remote history, use `git rebase origin/main` and resolve conflicts deliberately. If preserving both lines of shared history is required, merge instead. Do not force-push a shared branch casually. Create a backup branch before uncertain history edits.

## Commit suggestions

`docs: add transformer explanations`; `feat: add semantic search adapter`; `test: cover tenant isolation`; `feat: add bounded graph workflow`; `docs: record measured evaluation results`; `fix: preserve citation versions`; `chore: lock tested dependencies`.

## Secrets

Keep .env ignored and .env.example empty of secrets. Review staged content. If a real key was committed, rotate or revoke it promptly; deleting it from the latest file alone does not remove historical exposure.
