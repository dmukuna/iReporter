"""v2 package"""
from flask import Blueprint
#pylint: disable=import-error
from flask_restful import Api, Resource
from .views import Incidents, Incident, IncidentAttr


VERSION_TWO = Blueprint('api_v2', __name__, url_prefix='/api/v2')
API = Api(VERSION_TWO)

API.add_resource(Incidents, '/incidents')
API.add_resource(Incident, '/incidents/<int:flag_id>')
API.add_resource(IncidentAttr, '/Incidents/<int:flag_id>/<string:attr>')