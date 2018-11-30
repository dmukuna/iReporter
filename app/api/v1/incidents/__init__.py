"""v1 package"""
from flask import Blueprint
#pylint: disable=import-error
from flask_restful import Api, Resource
from .views import RedFlags #RedFlag, RedFlagAttr


VERSION_ONE = Blueprint('api_v1', __name__, url_prefix='/api/v1')
API = Api(VERSION_ONE)

API.add_resource(RedFlags, '/red-flags')
# API.add_resource(RedFlag, '/red-flags/<int:flag_id>')
# API.add_resource(RedFlagAttr, '/red-flags/<int:flag_id>/<string:attr>')
