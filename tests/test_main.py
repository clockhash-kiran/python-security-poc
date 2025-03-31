# tests/test_main.py
from fastapi.testclient import TestClient
from src.main import app  # Ensure 'src' is a valid module

client = TestClient(app)

def test_webhook():
    response = client.post("/webhook", json={"test": "data"})
    assert response.status_code == 200
    assert response.json() == {"status": "received"}
