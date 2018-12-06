import os
import psycopg2


url = "dbname='ireporter' host='localhost' port=5432 user='postgres' password='postgres'"
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

    for query in queries:
        curr.execute(query)
    conn.commit()

def destroy_tables():
    pass


def tables():
    users = """CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    fname VARCHAR(255) NOT NULL,
    lname VARCHAR(255),
    onames VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    tel_no VARCHAR(20) NOT NULL,
    user_nm VARCHAR(255) NOT NULL,
    date_created DATE NOT NULL DEFAULT CURRENT_TIMESTAMP NOT NULL,
    is_admin INTEGER NOT NULL
    );"""
    incidents = """CREATE TABLE IF NOT EXISTS incidents (
    incident_id serial PRIMARY KEY,
    created_on DATE NOT NULL NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by INT NOT NULL REFERENCES users(user_id),
    incident_type VARCHAR(25) NOT NULL,
    location VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    image VARCHAR(500),
    video VARCHAR (500),
    comment VARCHAR (1000)
    );"""

    queries = [users, incidents]
    return queries
