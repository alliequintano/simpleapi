import pytest, requests, json, datetime

from src.client.clock.current_time import get_current_time

def test_get_current_time_returns_datetime(requests_mock):
    requests_mock.get('http://127.0.0.1:5000/current-time', json={'currentTime':'2019-1-1 02:00:00.01'})
    current_time = get_current_time()
    
    assert isinstance(current_time, datetime.datetime)

def test_http_error_response(requests_mock):
    requests_mock.get('http://127.0.0.1:5000/current-time', status_code=400)
    error = get_current_time()

    assert isinstance(error, requests.exceptions.HTTPError)

def test_connection_error(requests_mock):
    requests_mock.get('http://127.0.0.1:5000/current-time', exc=requests.exceptions.ConnectionError)
    error = get_current_time()

    assert isinstance(error, requests.exceptions.ConnectionError)

def test_timeout_error(requests_mock):
    requests_mock.get('http://127.0.0.1:5000/current-time', exc=requests.exceptions.ConnectTimeout)
    error = get_current_time()

    assert isinstance(error, requests.exceptions.ConnectTimeout)

