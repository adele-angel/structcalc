from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_bending_api():
    payload = {
        "wy_cm3": 85.7,
        "fy_mpa": 235
    }

    response = client.post("/calc/bending", json=payload)
    assert response.status_code == 200
    assert "moment_capacity_kNm" in response.json()

def test_deflection_api():
    payload = {
        "load_kN": 5,
        "length_m": 4,
        "e_mpa": 210000,
        "iy_cm4": 857
    }

    response = client.post("/calc/deflection", json=payload)
    assert response.status_code == 200
    assert "deflection_mm" in response.json()
