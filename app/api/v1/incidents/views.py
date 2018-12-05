"""
app v1 views
"""
import json
from flask import jsonify, make_response, request
#pylint: disable=import-error
from flask_restful import Resource, reqparse
from datetime import date

from .models import RedFlagsModel


class RedFlags(Resource):
    """
    Red-flags class
    """
    def __init__(self):
        self.object = RedFlagsModel()

    def post(self):
        """
        Method to post data
        """
        parser = reqparse.RequestParser()

        parser.add_argument('created_by', type=int, nullable=False, required=True, location='json')
        parser.add_argument('incident_type', type=str,nullable=False, required=True,location='json',
                            help="incident_type cannot be blank")
        parser.add_argument('location', type=str, nullable=False, required=True, location='json',
                            help="location cannot be blank")
        parser.add_argument('status', type=str, nullable=False, required=True, location='json',
                            help="status cannot be blank")
        parser.add_argument('image', type=str, nullable=False, required=True, location='json',
                            help="image cannot be blank")
        parser.add_argument('video', type=str, nullable=False, required=True, location='json',
                            help="video cannot be blank")
        parser.add_argument('comment', type=str, nullable=False, required=True, location='json',
                            help="comment cannot be blank")

        args = parser.parse_args()
        args_list = []
        args_list.append(args)

        for arg in args_list:
            if len(arg['incident_type']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "Incident type field is required"
                    }]
                }))
            elif len(arg['location']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "Location field is required"
                    }]
                }))
            elif len(arg['status']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "Incident status field is required"
                    }]
                }))
            elif len(arg['image']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "Image field is required"
                    }]
                }))
            elif len(arg['video']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "video field is required"
                    }]
                }))
            elif len(arg['comment']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "comment field is required"
                    }]
                }))
            else:
                data = {
                    "id": len(self.object.database) + 1,
                    "created_by": args['created_by'],
                    "created_on": date.today(),
                    "incident_type": args['incident_type'],
                    "location": args['location'],
                    "status": args['status'],
                    "image": args['image'],
                    "video": args['video'],
                    "comment": args['comment']
                }
                rec_id = len(self.object.get_red_flags()) + 1
                self.object.save(data)
                return make_response(jsonify({
                    "status": 201,
                    "data": [{
                        "id": rec_id,
                        "message": "Created red-flag record"
                    }]
                }), 201)

    def get(self):
        r_flag = self.object.get_red_flags()
        return make_response(jsonify({
            "status": 200,
            "data": [{
                "Red-flags": r_flag
            }]
        }), 200)


class RedFlag(RedFlags):
    """class for PUT, delete and GETTING A SPECIFIC RECORD"""
    def __init__(self):
        super().__init__()

    #pylint: disable=arguments-differ
    def get(self, flag_id):
        red_flag = [record for record in self.object.database if record['id'] == flag_id]
        if len(red_flag) == 0:
            return make_response(jsonify({
                "status": 404,
                "error": "The specified red-flag does not exist"
            }), 404)
        return make_response(jsonify({
            "Red-flag": red_flag[0]
        }), 200)

    def put(self, flag_id):
        """Update a red-flag record"""
        red_flag = [record for record in self.object.database if record['id'] == flag_id]
        if len(red_flag) == 0:
            return make_response(jsonify({
                "status": 404,
                "error": "The specified red-flag does not exist"
            }), 404)
        parser = reqparse.RequestParser()

        parser.add_argument('created_by', type=int, nullable=False, required=True, location='json')
        parser.add_argument('incident_type', type=str, nullable=False, required=True,
                            location='json',
                            help="incident_type cannot be blank")
        parser.add_argument('location', type=str, nullable=False, required=True, location='json',
                            help="location cannot be blank")
        parser.add_argument('status', type=str, nullable=False, required=True, location='json',
                            help="status cannot be blank")
        parser.add_argument('image', type=str, nullable=False, required=True, location='json',
                            help="image cannot be blank")
        parser.add_argument('video', type=str, nullable=False, required=True, location='json',
                            help="video cannot be blank")
        parser.add_argument('comment', type=str, nullable=False, required=True, location='json',
                            help="comment cannot be blank")

        args = parser.parse_args()
        args_list = []
        args_list.append(args)

        for arg in args_list:
            if len(arg['incident_type']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "Incident type field is required"
                    }]
                }))
            elif len(arg['location']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "Location field is required"
                    }]
                }))
            elif len(arg['status']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "Incident status field is required"
                    }]
                }))
            elif len(arg['image']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "Image field is required"
                    }]
                }))
            elif len(arg['video']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "video field is required"
                    }]
                }))
            elif len(arg['comment']) == 0:
                return make_response(jsonify({
                    "data": [{
                        "message": "comment field is required"
                    }]
                }))
            else:
                red_flag[0]['created_by'] = args['created_by']
                red_flag[0]['created_on'] = date.today()
                red_flag[0]['incident_type'] = args['incident_type']
                red_flag[0]['location'] = args['location']
                red_flag[0]['status'] = args['status']
                red_flag[0]['image'] = args['image']
                red_flag[0]['video'] = args['video']
                red_flag[0]['comment'] = args['comment']
                return make_response(jsonify({
                    "Red-flag": red_flag[0],
                    "message": "Redflag updated successfully!"
                }), 200)


    def delete(self, flag_id):
        """Delete a specific red-flag"""
        red_flag = [record for record in self.object.database if record['id'] == flag_id]
        rec_id = red_flag[0]['id']
        if red_flag == []:
            return make_response(jsonify({
                "status": 204,
                "data":[{
                    "message": "The specified red-flag does not exist"
                }]
            }), 204)
        self.object.database.remove(red_flag[0])
        return make_response(jsonify({
            "status": 200,
            "data":[{
                "Id": rec_id,
                "message": "Red-flag has been deleted"
            }]
        }), 200)


class RedFlagAttr(RedFlag):
    """class for patching a specific record attribute"""
    def __init__(self):
        super().__init__()

    def patch(self, flag_id, attr):
        """Method for patching a specific red-flag"""
        red_flag = [record for record in self.object.database if record['id'] == flag_id]
        rec_id = red_flag[0]['id']

        parser = reqparse.RequestParser()
        parser.add_argument('change', type=str, nullable=False, required=True, location='json',
                            help="Input the required text")
        args = parser.parse_args()
        if len(args['change']) != 0:
            change = request.get_json()['change']
            allowed = ['video', 'comment', 'status', "incident_type", "location"]
            allowed_media = ['image', 'video']

            if len(red_flag) != 0:
                if attr in allowed:
                    red_flag[0][str(attr)] = change
                    return make_response(jsonify({
                        "status": 200,
                        "data": [{
                            "id": rec_id,
                            "message": "updated red-flag record " + str(attr)
                        }]
                    }), 200)
                elif attr in allowed_media and attr == 'image':
                    red_flag[0]['image'] = change
                    return make_response(jsonify({
                        "status": 200,
                        "data": [{
                            "id": rec_id,
                            "message": "updated red-flag's record image"
                        }]
                    }), 200)
                elif attr in allowed_media and attr == 'video':
                    red_flag[0]['video'] = change
                    return make_response(jsonify({
                        "status": 200,
                        "data": [{
                            "id": rec_id,
                            "message": "updated red-flag's record video"
                        }]
                    }), 200)
                return make_response(jsonify({
                    "status": 403,
                    "error": "The specified attribute cannot be edited"
                }), 403)
            return make_response(jsonify({
                "status": 404,
                "error": "The specified red-flag does not exist"
            }), 404)
        else:
            return make_response(jsonify({
                "error": "You cannot input an empty string"
            }))