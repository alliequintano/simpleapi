import pytest

from src.server import create_app

@pytest.fixture
def test_client():
    flask_app = create_app()
    testing_client = flask_app.test_client()

    yield testing_client

def test_get_current_time(test_client):
    response = test_client.get('http://127.0.0.1:5000/current-time')

    assert response.status_code == 200




