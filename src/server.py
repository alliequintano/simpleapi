from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)

class CurrentTime(Resource):
    def get(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        return {'currentTime': formatted_time }

api.add_resource(CurrentTime, '/current-time')

if __name__ == '__main__':
    app.run(debug=True)