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
