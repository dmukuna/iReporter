"""
app package
"""
from flask import Flask, Blueprint

#local imports
from instance.config import APP_CONFIG
from .api.v1.incidents import VERSION_ONE as v1

def create_app(config_name):
    """
    create app function
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('../instance/config.py')
    app.register_blueprint(v1)
    return app
