"""
app v2 views
"""
import json
from flask import jsonify, make_response, request
#pylint: disable=import-error
from flask_restful import Resource, reqparse
from datetime import date

from .models import IncidentsModel


class Incidents(Resource):
    """
    Incidents class
    """
    def __init__(self):
        self.object = IncidentsModel()

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
                rec_id = len(self.object.get_incidents()) + 1
                self.object.save(data)
                return make_response(jsonify({
                    "status": 201,
                    "data": [{
                        "id": rec_id,
                        "message": "Created incident record"
                    }]
                }), 201)

    def get(self):
        incidents = self.object.get_incidents()
        return make_response(jsonify({
            "status": 200,
            "data": [{
                "Red-flags": incidents
            }]
        }), 200)


class Incident(Incidents):
    """class for PUT, delete and GETTING A SPECIFIC RECORD"""
    def __init__(self):
        super().__init__()

    #pylint: disable=arguments-differ
    def get(self, flag_id):
        incident = [record for record in self.object.database if record['id'] == flag_id]
        if len(incident) == 0:
            return make_response(jsonify({
                "status": 404,
                "error": "The specified red-flag does not exist"
            }), 404)
        return make_response(jsonify({
            "Red-flag": incident[0]
        }), 200)

    def put(self, flag_id):
        """Update a incident record"""
        incident = [record for record in self.object.database if record['id'] == flag_id]
        if len(incident) == 0:
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
                incident[0]['created_by'] = args['created_by']
                incident[0]['created_on'] = date.today()
                incident[0]['incident_type'] = args['incident_type']
                incident[0]['location'] = args['location']
                incident[0]['status'] = args['status']
                incident[0]['image'] = args['image']
                incident[0]['video'] = args['video']
                incident[0]['comment'] = args['comment']
                return make_response(jsonify({
                    "Red-flag": incident[0],
                    "message": "Redflag updated successfully!"
                }), 200)


    def delete(self, flag_id):
        """Delete a specific Incident"""
        try:
            incident = [record for record in self.object.database if record['id'] == flag_id]
            inc_id = incident[0]['id']

            self.object.database.remove(incident[0])

        except IndexError:
            return make_response(jsonify({
                "status": 404,
                "data": [{
                    "message": "The specified red-flag does not exist"
                }]
            }), 404)
        return make_response(jsonify({
            "status": 200,
            "data": [{
                "Id": inc_id,
                "message": "Red-flag has been deleted"
            }]
        }), 200)


class IncidentAttr(Incident):
    """class for patching a specific record attribute"""
    def __init__(self):
        super().__init__()

    def patch(self, flag_id, attr):
        """Method for patching a specific red-flag"""
        incident = [record for record in self.object.database if record['id'] == flag_id]
        rec_id = incident[0]['id']

        attr = str(attr)
        parser = reqparse.RequestParser()
        parser.add_argument(attr, type=str, nullable=False, required=True, location='json',
                            help="Input the required text")
        args = parser.parse_args()
        if len(args[attr]) != 0:
            change = args[attr]
            allowed = ['video', 'comment', 'status', "incident_type", "location"]
            allowed_media = ['image', 'video']

            if len(incident) != 0:
                if attr in allowed:
                    incident[0][str(attr)] = change
                    return make_response(jsonify({
                        "status": 200,
                        "data": [{
                            "id": rec_id,
                            "message": "updated red-flag record " + str(attr)
                        }]
                    }), 200)
                elif attr in allowed_media and attr == 'image':
                    incident[0]['image'] = change
                    return make_response(jsonify({
                        "status": 200,
                        "data": [{
                            "id": rec_id,
                            "message": "updated red-flag's record image"
                        }]
                    }), 200)
                elif attr in allowed_media and attr == 'video':
                    incident[0]['video'] = change
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