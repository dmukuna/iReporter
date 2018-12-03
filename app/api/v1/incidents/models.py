"""
red-flags model
"""

RED_FLAGS_LIST = []

class RedFlagsModel():
    """
    red-flags class
    """
    def __init__(self):
        self.database = RED_FLAGS_LIST

    def save(self, *args):
        """
        save method
        """
        created_by = args[0]
        created_on = args[1]
        incident_type = args[2]
        location = args[3]
        status = args[4]
        image = args[5]
        video = args[6]
        comment = args[7]
        data = {
            "id": len(self.database)+1,
            "created_by": created_by,
            "created_on": created_on,
            "incident_type": incident_type,
            "location": location,
            "status": status,
            "image": image,
            "video": video,
            "comment": comment
        }
        self.database.append(data)

        return self.database

    def get_red_flags(self):
        """
        get_red_flags method
        """
        return self.database
