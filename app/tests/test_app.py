import pytest
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as c:
        yield c

def test_home(client):
    assert client.get("/").status_code == 200

def test_health(client):
    assert client.get("/health").get_json()["status"] == "healthy"