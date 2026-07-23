from fastapi.testclient import TestClient
from app.main import create_app

def get_client():
    # Create the app AFTER TESTING=1 is set
    app = create_app()
    return TestClient(app)

client = get_client()


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "message": "StructCalc API running"
    }


def test_create_member():
    payload = {
        "name": "Beam A",
        "length_m": 5.0
    }

    response = client.post("/members", json=payload)
    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "Beam A"
    assert data["length_m"] == 5.0
    assert "id" in data


def test_list_members():
    response = client.get("/members")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
