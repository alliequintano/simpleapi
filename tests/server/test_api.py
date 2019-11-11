import pytest, json

from datetime import datetime

from src.server import create_app

@pytest.fixture
def test_client():
    server = create_app()
    testing_client = server.test_client()

    yield testing_client

def test_get_current_time_status_code(test_client):
    response = test_client.get('http://127.0.0.1:5000/current-time')

    assert response.status_code == 200

def test_get_current_time_json_schema(test_client):
    response = test_client.get('http://127.0.0.1:5000/current-time')
    data = json.loads(response.data)
    
    assert 'currentTime' in data
    assert datetime.strptime(data['currentTime'], '%Y-%m-%d %H:%M:%S.%f')

#def test_get_current_time_value(test_client):



