"""This module handles questions and possible answers"""

from typing import List, Type


class Question:
    """This class handles questions for the quizz
    """

    def __init__(
            self,
            text: str,
            title: str,
            image: str,
            position: int,
            id_: int = -1,
            possible_answers: List[Type['PossibleAnswer']] = None
    ):
        self.id_ = id_
        self.text = text
        self.title = title
        self.image = image
        self.position = position
        self.possible_answers = possible_answers

    def to_dict(self):
        """Serialize object

        Returns:
            dict: serialized question
        """
        return {
            "id": self.id_,
            "text": self.text,
            "title": self.title,
            "image": self.image,
            "position": self.position,
            "possibleAnswers": self.possible_answers
        }

    def persist_to_db(self, cursor, id_=None):
        """Persist to database

        Args:
            cursor (_type_): sqlite3 cursor
        """
        if id_ is None:
            query = '''INSERT INTO questions (text, title, image, position)
                    VALUES (?, ?, ?, ?)'''
            parameters = (self.text, self.title, self.image, self.position)
        else:
            query = '''INSERT INTO questions (id, text, title, image, position)
                    VALUES (?, ?, ?, ?, ?)'''
            parameters = (id_, self.text, self.title,
                          self.image, self.position)

        cursor.execute(query, parameters)

        self.id_ = cursor.lastrowid
        for possible_answer in self.possible_answers:
            possible_answer.question_id = self.id_
            possible_answer.persist_to_db(cursor)

        return self


class PossibleAnswer:
    """This class handles possible answers for a question
    """

    def __init__(self, text: str, is_correct: bool, id_: int = -1, question_id: int = -1):
        self.id_ = id_
        self.question_id = question_id
        self.text = text
        self.is_correct = is_correct

    def to_dict(self):
        """Serialize object

        Returns:
            dict: serialized question
        """
        return {
            "id": self.id_,
            "question_id": self.question_id,
            "text": self.text,
            "isCorrect": True if self.is_correct else False
        }

    def persist_to_db(self, cursor):
        """Persist to database

        Args:
            cursor (_type_): sqlite3 cursor
        """
        query = '''INSERT INTO possible_answers (question_id, text, is_correct)
                   VALUES (?, ?, ?)'''
        cursor.execute(query, (self.question_id,
                       self.text, self.is_correct))
