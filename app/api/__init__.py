from flask import Blueprint
from flask_restful import Api

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

from . import auth_resource
from . import agent_resource
from . import ticket_resource