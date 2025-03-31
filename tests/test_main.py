from fastapi.testclient import TestClient
from src.main import app  # Ensure this correctly imports your FastAPI app

client = TestClient(app)  # This should work

def test_webhook():
    response = client.post("/webhook", json={"test": "data"})
    assert response.status_code == 200
    assert response.json() == {"status": "received"}
