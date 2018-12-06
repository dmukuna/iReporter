"""
red-flags model
"""
from ...db_con import init_db

RED_FLAGS_LIST = []


class IncidentsModel():
    """
    red-flags class
    """
    def __init__(self):

        self.database = init_db()

    def save(self, data):
        """
        save method
        """
        query = """INSERT INTO incidents (incident_type, location, status, image, video, comment) 
        VALUES (%(incident_type)s, %(location)s, %(status)s, %(image)s, %(video)s, %(comment)s);
        """
        curr = self.database.cursor()
        curr.execute(query, data)
        self.database.commit()

        return data

    def get_incidents(self):
        """
        get_red_flags method
        """
        query = """SELECT * FROM incidents;"""
        curr = self.database.cursor()
        curr = curr.execute(query)
        data = curr.fetchall()
        resp = []

        for i, record in enumerate(data):
            incident_id, created_on, created_by, incident_type, location, status, image, video, comment = record
            data_res = dict(
                incident_id=int(incident_id),
                created_on=created_on,
                created_by=int(created_by),
                incident_type=incident_type,
                location=location,
                status=status,
                image=image,
                video=video,
                comment=comment
            )
            resp.append(data_res)
        return resp
