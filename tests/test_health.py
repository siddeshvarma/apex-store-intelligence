# PROMPT:
# Generate FastAPI health endpoint tests.

# CHANGES MADE:
# Simplified assertions and adapted to project structure.

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"