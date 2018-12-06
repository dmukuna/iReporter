"""
red-flags model
"""

RED_FLAGS_LIST = [
    {
            'id': 1,
            'created_by': 'Daniel',
            'created_on': '1/2/2018',
            'comment': 'description is ...',
            'incident_type': 'red-flag',
            'image': 'image',
            'video': 'video',
            'location': '1.34532, 36.1552',
            'status': 'resolved',
    }
]

class RedFlagsModel():
    """
    red-flags class
    """
    def __init__(self):

        self.database = RED_FLAGS_LIST

    def save(self, data):
        """
        save method
        """
        self.database.append(data)

        return self.database

    def get_red_flags(self):
        """
        get_red_flags method
        """
        return self.database
