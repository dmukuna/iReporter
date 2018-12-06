"""
app package
"""
from flask import Flask, Blueprint
#local imports
from instance.config import APP_CONFIG
from app.api.db_con import create_tables
from app.api.v2.incidents import VERSION_TWO as v2

def create_app(config_name):
    """
    create app function
    """
    app = Flask(__name__, instance_relative_config=True)
    create_tables()
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('../instance/config.py')
    app.register_blueprint(v2)
    return app