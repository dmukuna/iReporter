"""
users model
"""
from flask import request
import psycopg2
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from app.api.db_con import Database


class UsersModel(Database):
    """
    red-flags class
    """
    def __init__(self):
        super().__init__('main')

    def save(self, data):
        """
        save method
        """
        query = """INSERT INTO users (fname, lname, onames, email, tel_no, password, user_name, is_admin)
                   VALUES (%(fname)s, %(lname)s, %(onames)s, %(email)s, %(tel_no)s, %(password)s, %(user_name)s, %(is_admin)s);
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


    def get_users(self):
        """
        get_red_flags method
        """
        query = """SELECT * FROM users"""
        self.cur.execute(query)
        data = self.findAll()
        resp = []

        for i, record in enumerate(data):
            user_id, fname, lname, onames, email, tel_no, password, user_name, date_created, is_admin = record
            data_res = dict(
                user_id =int(user_id),
                fname=fname,
                lname=lname,
                onames=onames,
                email=email,
                tel_no=tel_no,
                password=password,
                user_name=user_name,
                date_created=str(date_created),
                is_admin=is_admin
            )
            resp.append(data_res)
        return resp


