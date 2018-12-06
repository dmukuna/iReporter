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
        parser.add_argument('tel_no', type=str, nullable=False, required=True, location='json',
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
            elif len(arg['onames']) == 0:
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
            elif len(arg['tel_no']) == 0:
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
            else:
                data = {
                    "fname": arg['fname'],
                    "lname": arg['lname'],
                    "onames": arg['onames'],
                    "email": arg['email'],
                    "tel_no": arg['tel_no'],
                    "user_name": arg['user_name'],
                    "is_admin": arg['is_admin']
                }
                rec_id = len(self.object.get_users()) + 1
                self.object.save(data)
                return make_response(jsonify({
                    "status": 201,
                    "data": [{
                        "id": rec_id,
                        "message": "Created user record"
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
                "error": "The specified user does not exist"
            }), 404)
        return make_response(jsonify({
            "User": user[0]
        }), 200)

    def delete(self, user_id):
        """Delete a specific User"""
        try:
            user = [record for record in self.object.database if record['id'] == user_id]
            u_id = user[0]['id']

            self.object.database.remove(user[0])

        except IndexError:
            return make_response(jsonify({
                "status": 404,
                "data": [{
                    "message": "The specified user does not exist"
                }]
            }), 404)
        return make_response(jsonify({
            "status": 200,
            "data": [{
                "Id": u_id,
                "message": "User has been deleted"
            }]
        }), 200)


class UserAttr(User):
    def __init__(self):
        super().__init__()

    def patch(self, user_id, attr):
        """Method for patching a specific red-flag"""
        user = [record for record in self.object.database if record['id'] == user_id]
        u_id = user[0]['id']

        attr = str(attr)
        parser = reqparse.RequestParser()
        parser.add_argument(attr, type=str, nullable=False, required=True, location='json',
                            help="Input the required text")
        args = parser.parse_args()

        if len(args[attr]) != 0:
            change = args[attr]
            allowed = ['fname', 'lname', 'onames', 'email', 'tel_no', 'user_name', 'is_admin']


            if len(user) != 0:
                if attr in allowed:
                    user[0][str(attr)] = change
                    return make_response(jsonify({
                        "status": 200,
                        "data": [{
                            "id": u_id,
                            "message": "updated red-flag record " + str(attr)
                        }]
                    }), 200)
                return make_response(jsonify({
                    "status": 403,
                    "error": "The specified attribute cannot be edited"
                }), 403)
            return make_response(jsonify({
                "status": 404,
                "error": "The specified user does not exist"
            }), 404)
        return make_response(jsonify({
            "error": "You need to input some text"
        }))
