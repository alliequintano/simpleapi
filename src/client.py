import requests, time
from datetime import datetime

def current_time():
    response = requests.get('http://127.0.0.1:5000/current-time')
    json_object = response.json()
    datetime_object = json_object['currentTime']
    unformatted_time = datetime.strptime(datetime_object, '%Y-%m-%d %H:%M:%S')
    formatted_time = unformatted_time.strftime('The current time is %I:%M:%S %p on %B %d, %Y.')
    return formatted_time

while True:
    print(current_time(), end="", flush=True)
    print("\r", end="", flush=True)
    time.sleep(1)