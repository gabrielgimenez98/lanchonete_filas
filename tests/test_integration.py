from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_make_order():
    response = client.post("/make_order", json={"item": "carne"})
    assert response.status_code == 200

def test_check_order():
    response = client.get("/check_orders")
    assert response.status_code == 200