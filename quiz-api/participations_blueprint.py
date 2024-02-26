"""This module handles participation related logic for quizz app"""
from flask import Blueprint, request
from auth import jwt_required
# from question_model import Question, PossibleAnswer
from db import get_cursor
from participation_model import Participation

participations_bp = Blueprint('participations', __name__)


@participations_bp.route('/participations/all', methods=['DELETE'])
@jwt_required
def delete_all_participations():
    """Deletes all participations

    Returns:
        _type_: _description_
    """
    cursor = get_cursor()
    cursor.execute("begin")
    cursor.execute("DELETE FROM participations")
    cursor.execute("commit")
    return "All questions deleted", 204


@participations_bp.route('/participations', methods=['POST'])
def add_participation():
    """Ajoute une participation

    Returns:
        _type_: _description_
    """
    data = request.get_json()
    if len(data["answers"]) != 10:
        return "Pas 10 réponses", 400
    participation = Participation(
        data["playerName"], get_score(data["answers"]))
    participation.persist_to_db(get_cursor())
    return participation.to_dict(), 200


def get_score(user_answers):
    """Retourne le score d'un utilisateur

    Args:
        user_answers (List): List du numéro de la réponse par question

    Returns:
        int: score
    """
    correct_answers = []
    query = "SELECT * FROM possible_answers AS pa INNER JOIN questions as q ON (pa.question_id= q.id) ORDER BY q.position ASC"
    cursor = get_cursor()
    cursor.execute(query)
    answers = cursor.fetchall()
    count_to_reset = 1
    actual_id = -1
    for answer in answers:
        if actual_id != answer[1]:
            count_to_reset = 1
        if answer[3]:
            correct_answers.append(count_to_reset)
        count_to_reset += 1
        actual_id = answer[1]

    return sum(x == y for x, y in zip(user_answers, correct_answers))
