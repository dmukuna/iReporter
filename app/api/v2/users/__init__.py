"""v2 package"""
from flask import Blueprint
#pylint: disable=import-error
from flask_restful import Api, Resource
from .views import Users, User, UserAttr


VERSION_TWO = Blueprint('api_v2', __name__, url_prefix='/api/v2')
API = Api(VERSION_TWO)

API.add_resource(Users, '/users')
API.add_resource(User, '/users/<int:flag_id>')
API.add_resource(UserAttr, '/users/<int:flag_id>/<string:attr>')