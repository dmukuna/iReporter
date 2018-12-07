"""v2 package"""
from flask import Blueprint
#pylint: disable=import-error
from flask_restful import Api, Resource

from app.api.v2.incidents.views import Incidents, Incident, IncidentAttr
from app.api.v2.users.views import Users, User, UserAttr


VERSION_TWO = Blueprint('api_v2', __name__, url_prefix='/api/v2')
API = Api(VERSION_TWO)

API.add_resource(Incidents, '/incidents')
API.add_resource(Incident, '/incidents/<int:flag_id>')
API.add_resource(IncidentAttr, '/incidents/<int:flag_id>/<string:attr>')
API.add_resource(Users, '/users')
API.add_resource(User, '/users/<int:u_id>')
API.add_resource(UserAttr, '/users/<int:u_id>/<string:attr>')
