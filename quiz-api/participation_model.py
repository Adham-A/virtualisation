"""This module handles participations and possible answers"""


class Participation:
    """This class handles participations for the quizz
    """

    def __init__(self, nom: str, score: str):
        self.nom = nom
        self.score = score

    def to_dict(self):
        """Serialize object

        Returns:
            dict: serialized question
        """
        return {
            "playerName": self.nom,
            "score": self.score,
        }

    def persist_to_db(self, cursor):
        """Persist to database

        Args:
            cursor (_type_): sqlite3 cursor
        """
        query = '''INSERT INTO participations (nom, score)
                    VALUES (?, ?)'''
        parameters = (self.nom, self.score)
        cursor.execute(query, parameters)

        return self
