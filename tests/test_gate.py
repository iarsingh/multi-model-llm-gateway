from fastapi.testclient import TestClient
from llmgw.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'model': 'local-small', 'tokens': 10, 'budget': 100}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'model': 'hosted-xl', 'tokens': 10, 'budget': 100}).json()
    assert bad["passed"] is False
    assert "model_not_allowed" in bad["failed"]
