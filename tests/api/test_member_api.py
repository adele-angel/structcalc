from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "StructCalc API is running"}

def test_create_member():
    payload = {
        "id": 1,
        "name": "Beam A",
        "length_m": 5.0
    }

    response = client.post("/members", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Beam A"

def test_list_members():
    response = client.get("/members")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
