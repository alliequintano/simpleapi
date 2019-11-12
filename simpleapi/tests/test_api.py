import pytest, json

from simpleapi.server import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

def test_get_current_time(app):
    response = app.get('http://127.0.0.1:5000/current-time')
    assert response.status_code == 200

