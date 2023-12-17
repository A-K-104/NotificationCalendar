from functools import wraps

from flask import abort, request

from BL.UserBL import UserBL
from Common.DTOs.UserDTO import UserDTO
from Common.Enums.UserRollEnum import UserRollEnum
from Common.Exceptions.NotAuthorizedException import NotAuthorizedException
from Common.Exceptions.NotFoundException import NotFoundException


def user_is_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if auth is not None:
            try:
                user_bl = UserBL()
                user: UserDTO = user_bl.get_user_by_name(auth.username)
                if user is not None and UserRollEnum.ADMIN.__eq__(user.role):
                    return func(user, *args, **kwargs)
            except (NotAuthorizedException, NotFoundException):
                abort(401)
        abort(401)

    return wrapper
