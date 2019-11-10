from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)

class CurrentTime(Resource):
    def get(self):
        current_time = datetime.now()
        return {'currentTime': str(current_time)}

api.add_resource(CurrentTime, '/current-time')

if __name__ == '__main__':
    app.run(debug=True)