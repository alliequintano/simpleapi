from flask_restful import Resource
from datetime import datetime

class CurrentTime(Resource):
    def get(self):
        return { 'currentTime': str(datetime.now()) }
