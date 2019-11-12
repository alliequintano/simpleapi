import pytest, requests, json, datetime

from src.client.client import get_current_time

def test_get_current_time_returns_datetime(requests_mock):
    requests_mock.get('http://127.0.0.1:5000/current-time', json={'currentTime':'2019-1-1 02:00:00.01'})
    result = get_current_time()
    
    assert isinstance(result, datetime.datetime)