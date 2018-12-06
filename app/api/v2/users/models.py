"""
red-flags model
"""
from ...db_con import init_db


class UsersModel():
    """
    red-flags class
    """
    def __init__(self):

        self.database = init_db()

    def save(self, data):
        """
        save method
        """
        query = """INSERT INTO users (fname, lname, onames, email, tel_no, user_name, is_admin) 
        VALUES (%(fname)s, %(lanme)s, %(oname)s, %(email)s, %(tel_no)s, %(user_name)s, %(is_admin)s);
        """
        curr = self.database.cursor()
        curr.execute(query, data)
        self.database.commit()

        return data

    def get_users(self):
        """
        get_red_flags method
        """
        query = """SELECT * FROM users"""
        curr = self.database.cursor()
        curr = curr.execute(query)
        data = curr.fetchall()
        resp = []

        for i, record in enumerate(data):
            user_id, fname, lname, onames, email, tel_no, user_name, date_created, is_admin = record
            data_res = dict(
                user_id = user_id,
                fname=fname,
                lname=lname,
                onames=onames,
                email=email,
                tel_no=tel_no,
                user_name=user_name,
                date_created=date_created,
                is_admin=is_admin
            )
            resp.append(data_res)
        return resp
