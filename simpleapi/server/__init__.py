from flask import Flask
from flask_restful import Api

from simpleapi.server.api import CurrentTime

def create_app():
    server = Flask(__name__)
    api = Api(server)

    api.add_resource(CurrentTime, '/current-time')

    return server