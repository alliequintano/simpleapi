import requests, time, sys, socket, datetime

def get_current_time():
    try:
        response = requests.get('http://127.0.0.1:5000/current-time')
        response.raise_for_status()
    except requests.exceptions.ConnectionError as error:
        return error
    except requests.exceptions.HTTPError as error:
        return error
    else:
        json_object = response.json()
        current_time = datetime.datetime.strptime(json_object['currentTime'], '%Y-%m-%d %H:%M:%S.%f')
        return current_time

def display_current_time():
    while True:
        unformatted_time = get_current_time()
        if isinstance(unformatted_time, datetime.datetime):
            formatted_time = unformatted_time.strftime('%b %d %Y %I:%M:%S %p')
            print('The current local time is: ' + formatted_time, end='', flush=True)
            print('\r', end='', flush=True)
            time.sleep(1)
        else:
            print('sad times')
            sys.exit(1)

