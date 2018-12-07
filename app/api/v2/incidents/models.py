"""
Incidents model
"""
import psycopg2
from flask_jwt_extended import get_jwt_identity
from app.api.db_con import Database


class IncidentsModel(Database):
    """
    red-flags class
    """
    def __init__(self):
        super().__init__('main')

    def save(self, data):
        """
        save method
        """
        query = """INSERT INTO incidents (created_by, incident_type, location, status, image, video, comment) 
                   VALUES (%(created_by)s, %(incident_type)s, %(location)s, %(status)s, %(image)s, %(video)s, %(comment)s);
                   """
        try:

            self.cur.execute(query, data)
            self.commit()
            print('success')
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('could not save to db')
        return None

    def get_incidents(self):
        """
        get_red_flags method
        """
        query = """SELECT * FROM incidents;"""
        self.cur.execute(query)
        data = self.findAll()
        resp = []

        for i, record in enumerate(data):
            incident_id, created_on, created_by, incident_type, location, status, image, video, comment = record
            data_res = dict(
                id=int(incident_id),
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

    def current_user(self):
        """
            This method gets the logged in user from jwt token.
            It returns the username.
        """
        username = get_jwt_identity()
        return username