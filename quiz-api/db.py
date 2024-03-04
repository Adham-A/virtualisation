"""Handles database connection"""

import psycopg2
from psycopg2 import sql


def init_db():
    cursor = get_cursor()

    # Execute a query to check if the database is empty
    cursor.execute(
        "SELECT COUNT(*) FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';"
    )
    rows = cursor.fetchone()

    # If the database is empty
    if rows[0] == 0:
        print("Database empty");
        # Open and read the file
        with open("south_park.sql", "r", encoding="utf-8") as f:
            sql_script = f.read()
        
        # Execute the SQL script
        cursor.execute(sql.SQL(sql_script))
        cursor.connection.commit()

def get_cursor():
    """Creates cursor to database

    Returns:
        psycopg2.extensions.cursor: cursor
    """
    # create a connection
    db_connection = psycopg2.connect(
        host="postgresql-service.my-quiz-namespace.svc.cluster.local",
        # host="localhost",
        port="5432",
        database="base_database",
        user="user",
        password="root",
    )

    return db_connection.cursor()


def get_one_from_db(query, params):
    """Get one element from db

    Args:
        query (str): SQL query
        params (tuple): query parameters

    Returns:
        dict: column_name -> value
    """
    cursor = get_cursor()
    cursor.execute(query, params)

    row = cursor.fetchone()
    if row is None:
        return {}

    column_names = [description[0] for description in cursor.description]
    return dict(zip(column_names, row))


def get_multiple_from_db(query, params):
    """Get multiple from db

    Args:
        query (str): SQL query
        params (tuple): query parameters

    Returns:
        Tuple: rows, column_names
    """
    cursor = get_cursor()
    cursor.execute(query, params)

    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    return rows, column_names
