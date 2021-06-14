from flask import Flask
from flask_restful import Api
from .routes import Routes

app = Flask(__name__)
api = Api(app)
routes = Routes(api)
