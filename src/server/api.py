from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime

class CurrentTime(Resource):
    def get(self):
        return { 'currentTime': str(datetime.now()) }
