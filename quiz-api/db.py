"""Handles database connection"""
import psycopg2


def get_cursor():
    """Creates cursor to database

    Returns:
        psycopg2.extensions.cursor: cursor
    """
    # create a connection
    db_connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="base_database",
        user="user",
        password="root"
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
