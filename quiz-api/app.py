"""This module is a backend API for a quizz app"""
from hashlib import md5
from typing import Tuple
from flask import Flask, request
from flask_cors import CORS
from jwt_utils import build_token
from auth import jwt_required
from db import get_cursor
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response

# Imports routes
from questions_blueprint import questions_bp
from participations_blueprint import participations_bp
from admins_blueprint import admins_bp
# End of imports

app = Flask(__name__)

# app.wsgi_app = DispatcherMiddleware(
#     Response('Not Found', status=404),
#     {'/api': app.wsgi_app}
# )

app.register_blueprint(questions_bp)
app.register_blueprint(participations_bp)
app.register_blueprint(admins_bp)
CORS(app)


@app.route('/quiz-info', methods=['GET'])
def get_quizz_info():
    """This function retrieves general quizz info

    Returns:
        json: number of questions, score
    """
    cursor = get_cursor()
    cursor.execute(
        "SELECT count(*) as size from questions")
    number_of_questions, = cursor.fetchone()
    cursor.execute(
        "SELECT nom, score FROM participations ORDER BY score DESC")
    participants = cursor.fetchall()
    scores = [{'playerName': row[0], 'score': row[1]} for row in participants]
    return {"size": number_of_questions, "scores": scores}, 200


@app.route('/login', methods=['POST'])
def login():
    """
    Login route

    Returns:
        Unauthorized (401): If the request is not authorized.
        JSON data (200): If the request is authorized, returns a JSON response with a jwt token.
    """

    payload = request.get_json()
    hashed = md5(payload['password'].encode('UTF-8')).digest()
    if hashed == b'\xd8\x17\x06PG\x92\x93\xc1.\x02\x01\xe5\xfd\xf4_@':
        return {'token': build_token()}, 200
    return 'Unauthorized', 401


@jwt_required
@app.route('/rebuild-db', methods=['POST'])
def rebuild_database() -> Tuple:
    """Rebuilds the database

    Returns:
        Tuple: Message, Http code
    """
    cursor = get_cursor()
    # Open and read the SQL file
    with open('init_db.sql', 'r', encoding="UTF-8") as file:
        # Execute the SQL script
        cursor.executescript(file.read())
    return "Ok", 200


@app.route('/')
def hello_world():
    """Hello world route"""
    return "Hello world"


if __name__ == "__main__":
    app.run()
