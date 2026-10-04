# Multi-Model LLM Gateway

Level: 13 — LLMOps

Skills: Python, allowlist and token budget

Pass when model is on the allowlist and tokens <= budget. Distinct from llm-api-gateway by using /check.

```bash
pip install -r requirements.txt
pytest -q
```

This is a local laptop proof. It does not call a hosted model and it does not apply production changes.
