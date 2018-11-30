"""
app v1 views
"""
from flask import jsonify, make_response, request
#pylint: disable=import-error
from flask_restful import Resource

from .models import RedFlagsModel, RED_FLAGS_LIST


class RedFlags(Resource, RedFlagsModel):
    """
    Red-flags class
    """
    def __init__(self):
        super(RedFlags, self).__init__()
        self.database = RedFlagsModel()

    def post(self):
        """
        Method to post data
        """
        rec_id = len(self.database.get_red_flags()) + 1
        data = request.get_json()
        created_by = data['created_by']
        created_on = data['created_on']
        incident_type = data['incident_type']
        location = data['location']
        status = data['status']
        image = data['image']
        video = data['video']
        comment = data['comment']
        self.database.save(created_by, created_on, incident_type, location, status, image, video,
                           comment)
        return make_response(jsonify({
            "status": 201,
            "data": [{
                "id": rec_id,
                "message": "Created red-flag record"
            }]
        }), 201)

    def get(self):
        """
        method to get data
        """
        resp = self.database.get_red_flags()
        return make_response(jsonify({
            "status": 200,
            "data": resp
        }), 200)

class RedFlag(RedFlags):
    """class for PUT, delete and GETTING A SPECIFIC RECORD"""
    def __init__(self):
        super(RedFlag, self).__init__()
        self.database = RED_FLAGS_LIST

    #pylint: disable=arguments-differ
    def get(self, flag_id):
        red_flag = [record for record in self.database if record['id'] == flag_id]
        if red_flag == []:
            return make_response(jsonify({
                "status": 404,
                "error": "The specified red-flag does not exist"
            }), 404)
        return make_response(jsonify({
            "Red-flag": red_flag[0]
        }), 200)

    def put(self, flag_id):
        """Update a red-flag record"""
        red_flag = [record for record in self.database if record['id'] == flag_id]
        if red_flag == []:
            return make_response(jsonify({
                "status": 404,
                "error": "The specified red-flag does not exist"
            }), 404)
        data = request.get_json()
        red_flag[0]['created_by'] = data['created_by']
        red_flag[0]['created_on'] = data['created_on']
        red_flag[0]['incident_type'] = data['incident_type']
        red_flag[0]['location'] = data['location']
        red_flag[0]['status'] = data['status']
        red_flag[0]['image'] = data['image']
        red_flag[0]['video'] = data['video']
        red_flag[0]['comment'] = data['comment']
        return make_response(jsonify({
            "Red-flag": red_flag[0],
            "message": "Redflag updated successfully!"
        }), 200)

    def delete(self, flag_id):
        """Delete a specific red-flag"""
        red_flag = [record for record in self.database if record['id'] == flag_id]
        rec_id = red_flag[0]['id']
        if red_flag == []:
            return make_response(jsonify({
                "status": 204,
                "data":[{
                    "message": "The specified red-flag does not exist"
                }]
            }), 204)
        self.database.remove(red_flag[0])
        return make_response(jsonify({
            "status": 200,
            "data":[{
                "Id": rec_id,
                "message": "Red-flag has been deleted"
            }]
        }), 200)
