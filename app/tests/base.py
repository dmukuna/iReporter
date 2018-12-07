""" This is the base class for all the tests"""
import unittest
import json
import datetime
from unittest import TestCase
from flask import current_app
from app import create_app


class BaseTestCase(TestCase):
    """
        This class tests the entity modules
    """

    def setUp(self):
        """
            It initializes the app and app context.
        """
        self.app = create_app("testing")
        self.client = self.app.test_client
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.token = 0

        self.incident = {
            'created_by': 1,
            'created_on': '1/2/2018',
            'comment': 'description is ...',
            'incident_type': 'red-flag',
            'image': 'image',
            'video': 'video',
            'location': '1.34532, 36.1552',
            'status': 'resolved',
        }
        self.incident2 = {
            "created_by": 2,
            "created_on": "3/2/1994",
            "comment": "corruption has become rampant",
            "incident_type": "red-flag",
            "image": "image",
            "video": "video",
            "location": "10.53, -25.54",
            "status": "pending",
        }

        self.update_incident = {
            "type": "RedFlag",
            "title": "NCA site auth",
            "location": "37.12N, 3.7E",
            "images": "[Image, Image]",
            "video": "[Image, Image]",
            "description": "falling construction building"
        }
        self.incident_no_title = {
            "type": "RedFlag",
            "title": "",
            "location": "37.12N, 3.7E",
            "images": "[Image, Image]",
            "video": "[Image, Image]",
            "descrrption": "falling construction building"
        }
        self.incident_no_comment = {
            "type": "RedFlag",
            "title": "NCA site auth",
            "location": "37.12N, 3.7E",
            "images": "[Image, Image]",
            "video": "[Image, Image]",
            "description": ""
        }
        self.incident_invalid_video = {
            "type": "12345",
            "title": "NCA site auth",
            "location": "37.12N, 3.7E",
            "images": "[Image, Image]",
            "video": 1234,
            "description": "falling construction kapanga building"
        }
        self.status_Resolved = {
            "status": "Resolved"
        }
        self.status_Rejected = {
            "status": "Rejected"
        }
        self.comment = {
            "change": "Rise of crime in juja"
        }
        self.location = {
            "change": "40.689263, -74.044505"
        }
        self.user = {
            "fname": "carol",
            "lname": "mumbi",
            "onames": "kamau",
            "email": "carol@mumbi.com",
            "tel_no": "0708123123",
            "username": "carolmobic",
            "password": "mae12#embiliA",
            "is_admin": 0
        }
        self.user1 = {
            "fname": "mwaniki",
            "lname": "mumbi",
            "onames": "kamau",
            "email": "carolmumbi@gmail.com",
            "tel_no": "0123456789",
            "username": "carolnice",
            "password": "mae12#embiliA",
            "is_admin": 1
        }
        self.user_no_username = {
            "email": "bluish@gmail.com",
            "password": "mae12#embili"
        }
        self.user_no_email = {
            "username": "dante",
            "password": "mae12#embili"
        }
        self.user_no_password = {
            "username": "dante",
            "email": "mbuchez8@gmail.com",
        }
        self.user_invalid_email = {
            "username": "dante",
            "email": "mbuchez.com",
            "password": "mae12#embili"
        }
        self.user_invalid_username = {
            "username": "",
            "email": "mbuchez@gmail.com",
            "password": "mae12#embili"
        }
        self.user_invalid_password = {
            "username": "mama yao",
            "email": "mbuchez@gmail.com",
            "password": "maembe"
        }
        self.user_existing_user = {
            "firstname": "carolol",
            "lastname": "mumbi",
            "email": "carolmumbi@gmail.com",
            "phoneNumber": "0708123123",
            "username": "carolmobic",
            "password": "aswdeAWSE$WE"
        }

        self.correct_login = {
            "username": "carolmobic",
            "password": "mae12#embiliA"
        }
        self.correct_login1 = {
            "username": "carolmobic",
            "password": "aswdeAWSE$WE"
        }

        self.wrong_login = {"username": "carolmoboc",
                            "password": "mistubishi"}
        self.no_username = {"username": "",
                            "password": "maembembili"}
        self.no_password = {"username": "lawrence",
                            "password": ""}

    def tearDown(self):
        """
            It destroys the app context.
        """
        self.app_context.pop()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()