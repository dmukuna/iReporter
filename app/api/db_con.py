import os
import psycopg2


url = "db_name='ireporter' host='localhost' port=5432 user='dante' password=DANTE123"
db_url = os.getenv('DATABSE_URL')


def connection(url):
    con = psycopg2.connect(url)
    return con


def init_db():
    con =connection(url)
    return con


def create_tables():
    conn = connection(url)
    curr = conn.cursor()
    queries = tables()


def destroy_tables():
    pass


def tables():
    users = """CREATE TABLE IF NOT EXISTS users (
    user_id serial PRIMARY KEY NOT NULL,
    fname CHARACTER VARYING(255) NOT NULL,
    lname CHARACTER VARYING(255),
    onames CHARACTER VARYING(255),
    email CHARACTER VARYING(255) NOT NULL,
    tel_no CHARACTER VARYING(20) NOT NULL,
    user_nm CHARACTER VARYING(255) NOT NULL,
    date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
    is_admin INTEGER NOT NULL,
    )"""
    incidents = """CREATE TABLE IF NOT EXISTS incidents (
    incident_id serial PRIMARY KEY NOT NULL,
    created_on timestamp with the time zone DEFAULT ('now'::tetx)::date NOT NULL,
    created_by FOREIGN KEY REFERENCES users(user_id),
    incident_type CHARACTER  varying (25) NOT NULL,
    location CHARACTER VARYING(255) NOT NULL,
    status CHARACTER VARYING(50) NOT NULL,
    image CHARACTER VARYING(500),
    video CHARACTER VARYING(500),
    comment CHARACTER VARYING(1000)
    )"""

    queries = [users, incidents]
    return queries
