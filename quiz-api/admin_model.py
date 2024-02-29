"""This module handles Admin back office"""


class Admin:
    """Serves as an ORM layer to load and save this model into the DB"""

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def to_dict(self):
        """Serialize object

        Returns:
            dict: serialized
        """
        return {
            "username": self.username,
            "password": self.password,
        }

    def persist_to_db(self, cursor):
        """Persist to database

        Args:
            cursor (_type_): sqlite3 cursor
        """
        query = """INSERT INTO admins (username, password)
                    VALUES (%s, %s)"""
        parameters = (self.username, self.password)
        cursor.execute(query, parameters)
        cursor.connection.commit()
        return self
