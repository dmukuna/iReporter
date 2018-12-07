""" This module holds the database migrations """
import os
import psycopg2

DATABASE_URL = 'postgresql://localhost/ireporter?user=postgres&password=postgres'
TEST_DATABASE_URL = 'postgresql://localhost/test_ireporter?user=postgres&password=postgres'
CONNECTION_CREDS = {
    "host": os.getenv('DB_HOST'),
    "database": os.getenv('DB_NAME'),
    "user": os.getenv('DB_USER'),
    "password": os.getenv('DB_PASSWORD')
}
TEST_CONNECTION_CREDS = {
    "host": os.getenv('TEST_DB_HOST'),
    "database": os.getenv('TEST_DB_NAME'),
    "user": os.getenv('TEST_DB_USER'),
    "password": os.getenv('TEST_DB_PASSWORD')
}


class Database():
    """
        consists of methods to connect and query from db
    """

    def __init__(self, db):
        self.db_url = DATABASE_URL
        self.db_test_url = TEST_DATABASE_URL
        self.db_con_creds = CONNECTION_CREDS
        self.db_test_con_creds = TEST_CONNECTION_CREDS
        self.conn = self.choose_db(db)
        self.cur = self.conn.cursor()

    def connection(self, *arg, **url):
        """
            connect to postgres database
        """
        conn = psycopg2.connect(url)
        return conn

    def init_db(self):
        """
            connect to ireporter database
        """
        try:
            print("connecting to db...\n")
            try:
                conn = self.connection(self.db_url)
                print('connected to db\n')
                return conn
            except:
                conn = psycopg2.connect(
                    'postgresql://localhost/ireporter?user=postgres&password=postgres')
                print('connected to db\n')
                return conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('error connecting to db\n')

    def init_test_db(self):
        """
            connect to test db
        """
        try:
            print("connecting to test db...\n")
            try:
                conn = self.connection(self.db_test_url)
                print('connected to test db\n')
                return conn
            except:
                conn = psycopg2.connect(
                    'postgresql://localhost/test_ireporter?user=postgres&password=postgres')
                print('connected to test db\n')
                return conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('error connecting to test db\n')

    def choose_db(self, db):
        """ choose database to connect to """
        if db == "main":
            conn = self.init_db()
        elif db == "test":
            conn = self.init_test_db()
        else:
            return None
        return conn

    def create_tables(self):
        """
            create tables in the database
        """
        commands = (
            """
                CREATE TABLE IF NOT EXISTS users (
                    user_id SERIAL PRIMARY KEY,
                    fname VARCHAR(255) NOT NULL,
                    lname VARCHAR(255),
                    onames VARCHAR(255),
                    email VARCHAR(255) NOT NULL,
                    tel_no VARCHAR(20) NOT NULL,
                    password VARCHAR(100) NOT NULL,
                    user_name VARCHAR(255) NOT NULL,
                    date_created DATE NOT NULL DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    is_admin BOOLEAN NOT NULL DEFAULT FALSE
                )
            """,
            """
                CREATE TABLE IF NOT EXISTS incidents (
                    incident_id serial PRIMARY KEY,
                    created_on DATE NOT NULL NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    created_by INT NOT NULL REFERENCES users(user_id),
                    incident_type VARCHAR(25) NOT NULL,
                    location VARCHAR(255) NOT NULL,
                    status VARCHAR(50) NOT NULL DEFAULT 'pending',
                    image VARCHAR(500),
                    video VARCHAR (500),
                    comment VARCHAR (1000)
                )
            """
        )

        try:
            for command in commands:
                self.cur.execute(command)
            self.commit()
            self.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('could not create tables\n')
        finally:
            if self.conn is not None:
                self.conn.close()

    def drop_tables(self, table):
        """ drop existing tables """
        try:
            self.cur.execute("DROP TABLE IF EXISTS" + table)
            self.commit()
            self.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print('could not drop tables\n')
        finally:
            if self.conn is not None:
                self.close()

    def commit(self):
        """
        commit changes to the db
        """
        self.conn.commit()

    def close(self):
        """
            close the cursor and the connection
        """
        self.cur.close()
        self.conn.close()

    def findOne(self):
        """ return one item from query"""
        return self.cur.fetchone()

    def findAll(self):
        """ return all items from query"""
        return self.cur.fetchall()