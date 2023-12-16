from flask import jsonify

from Commons.Enums.UserRollEnum import UserRollEnum
from Commons.Exceptions.MissingValueException import MissingValueException
from Commons.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Commons.Exceptions.NotAuthorizedException import NotAuthorizedException
from Commons.Exceptions.NotFoundException import NotFoundException
from Commons.Exceptions.NotInEnumException import NotInEnumException
from Models import user_model


def get_user_bl(user_id: int):
    user = user_model.get_user_by_id(user_id)
    if user:
        return jsonify(user)
    raise NotFoundException()


def get_user_authorized_by_name_bl(username: str) -> dict:
    user = user_model.get_user_by_name(username)
    if user:
        return user
    raise NotAuthorizedException()


def create_user_bl(json: dict):
    if 'username' not in json or 'role' not in json:
        raise MissingValueException()

    if not UserRollEnum.__contains__(json.get('role')):
        raise NotInEnumException()
    try:
        new_user = user_model.create_user(**json)
        return jsonify(new_user)
    except Exception as e:
        if 'duplicate key value' in str(e):
            raise NameAlreadyUsedException()
        raise Exception(e)


def update_user_bl(user_id: int, json: dict):

    if json.__contains__('role') and not UserRollEnum.__contains__(json.get('role')):
        raise NotInEnumException()

    try:
        user = user_model.update_user_by_id(user_id, **json)
    except Exception as e:
        if 'duplicate key value' in str(e):
            raise NameAlreadyUsedException()
        raise Exception(e)

    if user is not None:
        return jsonify(user)
    raise NotFoundException()


def delete_user_bl(user_id: int):
    if user_model.delete_user_by_id(user_id):
        return "User deleted"
    raise NotFoundException()
