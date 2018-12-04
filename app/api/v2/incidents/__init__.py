"""v2 package"""
from flask import Blueprint
#pylint: disable=import-error
from flask_restful import Api, Resource
from .views import RedFlags, RedFlag, RedFlagAttr


VERSION_TWO = Blueprint('api_v2', __name__, url_prefix='/api/v2')
API = Api(VERSION_TWO)

API.add_resource(RedFlags, '/red-flags')
API.add_resource(RedFlag, '/red-flags/<int:flag_id>')
API.add_resource(RedFlagAttr, '/red-flags/<int:flag_id>/<string:attr>')
