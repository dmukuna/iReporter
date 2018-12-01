"""
run app
"""
import os

from app import create_app

CONFIG_NAME = os.getenv('APP_CONFIG')
APP = create_app(CONFIG_NAME)

if __name__ == '__main__':
    APP.run()
