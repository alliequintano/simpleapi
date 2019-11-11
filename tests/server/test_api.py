import pytest, json

from datetime import datetime, timedelta

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

def test_get_current_time_value(test_client):
    response = test_client.get('http://127.0.0.1:5000/current-time')
    data = json.loads(response.data)
    
    current_time_value = datetime.strptime(data['currentTime'], '%Y-%m-%d %H:%M:%S.%f')
    later_time = datetime.now()

    assert (later_time - current_time_value) < timedelta(seconds=1)



