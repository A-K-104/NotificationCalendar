from functools import wraps

from flask import abort, request, make_response

from BL import user_bl
from Common.Enums.UserRollEnum import UserRollEnum
from Common.Exceptions.NotAuthorizedException import NotAuthorizedException


def server_error_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return make_response(f"Server error: {e}", 500)

    return wrapper
