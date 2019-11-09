from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def current_time():
    response = requests.get('http://127.0.0.1:5001/')
    json_object = response.json()
    time = json_object['currentTime']
    return time

if __name__ == '__main__':
    app.run(debug=True)