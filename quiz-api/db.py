"""Handles database connection"""
import sqlite3


def get_cursor():
    """Creates cursor to dabatase

    Returns:
        sqlite3.Cursor: cursor
    """
    # create a connection
    db_connection = sqlite3.connect("quiz.db")
    # Ajoutes les foreign keys sinon cringe
    db_connection.execute("PRAGMA foreign_keys = 1")

    # set the sqlite connection in "manual transaction mode"
    # (by default, all execute calls are performed in their own transactions, not what we want)
    db_connection.isolation_level = None

    return db_connection.cursor()


def get_one_from_db(query, params):
    """Get one element from db

    Args:
        query (_type_): _description_
        params (_type_): _description_

    Returns:
        dict: nom_colomne → valeur
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
        query (_type_): _description_
        params (_type_): _description_

    Returns:
        Tuple: rows, column_names
    """
    cursor = get_cursor()
    cursor.execute(query, params)

    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    return rows, column_names
