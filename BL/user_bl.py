from flask import jsonify

from Commons.Exceptions.MissingValueException import MissingValueException
from Commons.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Commons.Exceptions.NotFoundException import NotFoundException
from Models import user_model


def get_user_bl(user_id: int):
    user = user_model.get_user_by_id(user_id)
    if user:
        return jsonify(user)
    raise NotFoundException()


def create_user_bl(json: dict):
    if 'username' not in json or 'role' not in json:
        raise MissingValueException()

    try:
        new_user = user_model.create_user(**json)
        return jsonify(new_user)
    except Exception as e:
        if 'duplicate key value' in str(e):
            raise NameAlreadyUsedException()
        raise Exception(e)


def update_user_bl(user_id: int, json: dict):
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
