"""This module handles admin related logic for quizz app"""
from flask import Blueprint, request
from auth import jwt_required
# from question_model import Question, PossibleAnswer
from db import get_one_from_db
from admin_model import Admin
from jwt_utils import build_token

import hashlib


admins_bp = Blueprint('admin', __name__)


# @admins_bp.route('/admin/all', methods=['DELETE'])
# @jwt_required
# def delete_all_admins():
#     """Deletes all admins

#     Returns:
#         _type_: _description_
#     """
#     cursor = get_cursor()
#     cursor.execute("begin")
#     cursor.execute("DELETE FROM admins")
#     cursor.execute("commit")
#     return "All questions deleted", 204


@admins_bp.route('/admin/login', methods=['POST'])
def login():
    """

    Returns:
        _type_: _description_
    """
    data = request.get_json()
    print(data)
    admin = Admin(data["username"], data["password"])
    query = '''SELECT * FROM admins WHERE username=?'''
    parameters = (admin.username,)
    result = get_one_from_db(query,parameters)
    print(result)
    if not result:
        return 'This admin does not exist', 401

    if result["password"] == hashlib.md5(admin.password.encode('utf-8')).hexdigest():
        return {'token': build_token()}, 200
    else:
        return 'Wrong password', 401

    
