from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)

class CurrentTime(Resource):
    def get(self):
        return { 'currentTime': str(datetime.now()) }

api.add_resource(CurrentTime, '/current-time')

if __name__ == '__main__':
    app.run(debug=True)