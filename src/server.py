from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class CurrentTime(Resource):
    def get(self):
        return {'currentTime':'Hello World'}

api.add_resource(CurrentTime, '/')

if __name__ == '__main__':
    app.run(debug=True)