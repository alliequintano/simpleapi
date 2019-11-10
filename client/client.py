import requests, time
from datetime import datetime

def current_time():
    response = requests.get('http://127.0.0.1:5000/current-time')
    json_object = response.json()
    current_time = datetime.strptime(json_object['currentTime'], '%Y-%m-%d %H:%M:%S.%f')
    return current_time

def display_current_time():
    while True:
        formatted_time = current_time().strftime('%b %d %Y %H:%M:%S %p')
        print('The current local time is: ' + formatted_time, end="", flush=True)
        print("\r", end="", flush=True)
        time.sleep(1)

if __name__ == '__main__':
    display_current_time()