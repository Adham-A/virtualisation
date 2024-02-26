"""This module handles auth related logic for quizz app"""
from functools import wraps
from typing import Callable
from flask import request
from jwt_utils import decode_token, JwtError

# JWT Token decorator


def jwt_required(func):
    """Decorator to force login to access route

    Args:
        func (Callable): function which is called

    Returns:
        Unauthorized (401): If the request is not authorized.
        Callable: function which is called
    """
    @wraps(func)
    def decorated(*args, **kwargs) -> Callable:
        token = request.headers.get('Authorization')
        if token:
            try:
                # Enlève le "Bearer " depuis la requête
                decode_token(token.replace("Bearer ", ""))
            except JwtError as exception:
                return f'Unauthorized : {exception.message}', 401
            return func(*args, **kwargs)
        else:
            return 'Unauthorized : No bearer token sent', 401
    return decorated
