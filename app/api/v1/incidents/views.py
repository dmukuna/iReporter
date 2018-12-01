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