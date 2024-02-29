"""This module handles question related logic for quizz app"""
from flask import Blueprint, request, jsonify
from auth import jwt_required
from question_model import Question, PossibleAnswer
from db import get_cursor, get_multiple_from_db, get_one_from_db

questions_bp = Blueprint('questions', __name__)


@questions_bp.route('/questions', methods=['GET'])
def get_question_by_position():
    """Gets a quesiton by its position

    Returns:
        _type_: _description_
    """
    position = request.args.get('position', None)
    question_dict = get_one_from_db(
        "SELECT * from questions where position = %s", (position,))

    if not question_dict:
        return 'Question not found', 404
    question_dict["id_"] = question_dict.pop("id")
    question = Question(**question_dict)

    possible_answers_rows, column_names = get_multiple_from_db(
        "SELECT * FROM possible_answers WHERE question_id = %s", (question.id_,))

    question.possible_answers = [] if possible_answers_rows else None

    for row in possible_answers_rows:
        parameters = dict(zip(column_names, row))
        parameters["id_"] = parameters.pop("id")
        question.possible_answers.append(
            PossibleAnswer(**parameters).to_dict())

    return jsonify(question.to_dict()), 200


@questions_bp.route('/questions/<int:question_id>', methods=['GET'])
def get_question_by_id(question_id: int):
    """Gets a quesiton by its id

    Args:
        question_id (int): id of the question

    Returns:
        _type_: _description_
    """
    question_dict = get_one_from_db(
        "SELECT * from questions where id = %s", (question_id,))

    if not question_dict:
        return 'Question not found', 404

    question_dict["id_"] = question_dict.pop("id")
    question = Question(**question_dict)

    possible_answers_rows, column_names = get_multiple_from_db(
        "SELECT * FROM possible_answers WHERE question_id = %s", (question_id,))

    question.possible_answers = [] if possible_answers_rows else None

    for row in possible_answers_rows:
        parameters = dict(zip(column_names, row))
        parameters["id_"] = parameters.pop("id")
        question.possible_answers.append(
            PossibleAnswer(**parameters).to_dict())

    return jsonify(question.to_dict()), 200


@questions_bp.route('/questions', methods=['POST'])
@jwt_required
def add_question_route():
    """Add a question to the database

    Returns:
        Unauthorized (401): If the request is not authorized.
        _type_: _description_
    """
    question = add_question()

    return {'id': question.id_}, 200


@questions_bp.route('/questions/<int:question_id>', methods=['PUT'])
def update_question_route(question_id: int):
    """Update une question

    Args:
        question_id (int): id de la question

    Returns:
        _type_: _description_
    """
    if delete_question_by_id(question_id):
        add_question(question_id)
        return "Ok", 204
    else:
        return "Not found", 404


def add_question(question_id=None):
    """Add a question to the database

    Returns:
        Question : the question added
    """
    # #récupèrer un l'objet json envoyé dans le body de la requète
    data = request.get_json()
    # Sanitize la data
    possible_answers = data.pop("possibleAnswers")
    for element in possible_answers:
        element["is_correct"] = element.pop("isCorrect")
    possible_answers = [PossibleAnswer(**element)
                        for element in possible_answers]
    cursor = get_cursor()

    question_object = Question(
        **data, possible_answers=possible_answers)
    new_position = question_object.position

    # Select all questions
    cursor = get_cursor()
    cursor.execute(
        "SELECT id, position FROM questions WHERE position >= %s ORDER BY position ASC",
        (new_position, ))
    rows = cursor.fetchall()

    # Update each question's position
    for row in rows:
        quest_id, old_pos = row
        position_futur = old_pos + 1

        # Update question's position
        cursor.execute(
            "UPDATE questions SET position = %s WHERE id = %s", (position_futur, quest_id))

    question_object.persist_to_db(get_cursor(), question_id)

    return question_object


@questions_bp.route('/questions/all', methods=['DELETE'])
@jwt_required
def delete_all_question():
    """Deletes all questions

    Returns:
        _type_: _description_
    """
    cursor = get_cursor()
    cursor.execute("begin")
    cursor.execute("DELETE FROM questions")
    cursor.execute("commit")
    return "All questions deleted", 204


@questions_bp.route('/questions/<int:question_id>', methods=['DELETE'])
@jwt_required
def delete_question_by_id_route(question_id: int):
    """Deletes question by id

    Returns:
        _type_: _description_
    """
    if not delete_question_by_id(question_id):
        return "Not found", 404
    return "Question deleted", 204


def delete_question_by_id(question_id: int):
    """Deletes question by id

    Returns:
        _type_: _description_
    """
    position = get_one_from_db(
        "SELECT position from questions where id = %s", (question_id,))

    cursor = get_cursor()
    query = "DELETE FROM questions WHERE id = %s"
    cursor.execute(query, (question_id,))
    n_deleted = cursor.rowcount

    # Select all questions
    if position:
        position = position["position"]
        cursor = get_cursor()
        cursor.execute(
            "SELECT id,position FROM questions WHERE position>=%s ORDER BY position ASC",
            (position, ))
        rows = cursor.fetchall()

        # Update each question's position
        for row in rows:
            quest_id, old_pos = row
            position_futur = old_pos - 1

            # Update question's position
            cursor.execute(
                "UPDATE questions SET position = %s WHERE id = %s", (position_futur, quest_id))

    return n_deleted
