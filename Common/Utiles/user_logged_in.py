from functools import wraps

from flask import abort, request

from BL import user_bl
from Common.Enums.UserRollEnum import UserRollEnum
from Common.Exceptions.NotAuthorizedException import NotAuthorizedException


def user_is_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if auth is not None:
            try:
                user: dict = user_bl.get_user_authorized_by_name_bl(auth.username)
                if user is not None and UserRollEnum.ADMIN.__eq__(user['role']):
                    return func(user, *args, **kwargs)
            except NotAuthorizedException:
                abort(401)
        abort(401)

    return wrapper
