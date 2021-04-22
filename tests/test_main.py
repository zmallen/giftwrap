from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 404


def test_get_simple_blip():
    response = client.get("/simple/blip/")
    assert response.status_code == 200