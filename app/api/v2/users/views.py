from flask import jsonify, make_response, request
from flask_restful import Resource, reqparse

from .models import UsersModel

class Users(Resource):
    def __init__(self):
        self.object = UsersModel()

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('fname', type=str, nullable=False, required=True, location='json',
                            help="First name is required")
        parser.add_argument('lname', type=str, nullable=False, required=True,
                            location='json', help="Enter your last name")
        parser.add_argument('onames', type=str, nullable=False, required=True, location='json',
                            help="Enter your other names")
        parser.add_argument('email', type=str, nullable=False, required=True, location='json',
                            help="Email field cannot be blank")
        parser.add_argument('tel', type=str, nullable=False, required=True, location='json',
                            help="Telephone field cannot be blank")
        parser.add_argument('user_name', type=str, nullable=False, required=True, location='json',
                            help="Enter your user name")
        parser.add_argument('is_admin', type=int, nullable=False, required=True, location='json',
                            help="video cannot be blank")

        args = parser.parse_args()
        arg_list = []
        arg_list.append(args)

        for arg in arg_list:
            if len(arg['fname']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "First name field is required"
                    }]
                }))
            elif len(arg['lname']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "Last name field is required"
                    }]
                }))
            elif len(arg['oname']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "Other name field field is required"
                    }]
                }))
            elif len(arg['email']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "Email field is required"
                    }]
                }))
            elif len(arg['tel']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "Telephone field is required"
                    }]
                }))
            elif len(arg['user_name']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "Username field is required"
                    }]
                }))
            elif len(arg['is_admin']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "Is_admin field is required"
                    }]
                }))
            else:
                data = {
                    "id": len(self.object.database) + 1,
                    "fname": arg['fname'],
                    "lname": arg['lname'],
                    "oname": arg['oname'],
                    "email": arg['email'],
                    "tel": arg['tel'],
                    "user_name": arg['user_name'],
                    "is_admin": arg['is_admin']
                }
                rec_id = len(self.object.get_users()) + 1
                self.object.save(data)
                return make_response(jsonify({
                    "status": 201,
                    "data": [{
                        "id": rec_id,
                        "message": "Created incident record"
                    }]
                }), 201)

    def get(self):
        users = self.object.get_users()
        return make_response(jsonify({
            "status": 200,
            "data": [{
                "Red-flags": users
            }]
        }), 200)


class User(Users):
    def __init__(self):
        super().__init__()

    def get(self, user_id):
        user = [record for record in self.object.database if record['id'] == user_id]
        if len(user) == 0:
            return make_response(jsonify({
                "status": 404,
                "error": "The specified red-flag does not exist"
            }), 404)
        return make_response(jsonify({
            "Red-flag": user[0]
        }), 200)

    def delete(self, user_id):
        pass


class UserAttr(User):
    def __init__(self):
        super().__init__()

    def patch(self, user_id, attr):
        pass
