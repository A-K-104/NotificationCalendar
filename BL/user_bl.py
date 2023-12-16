from flask import jsonify

from Common.Enums.UserRollEnum import UserRollEnum
from Common.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Common.Exceptions.NotAuthorizedException import NotAuthorizedException
from Common.Exceptions.NotFoundException import NotFoundException
from Common.Exceptions.NotInEnumException import NotInEnumException
from Model.user_model import UserModel


class UserBL:

    def __init__(self):
        self.userModel = UserModel()

    def get_all(self, user_id: int):
        user = self.userModel.get_one(user_id)
        if user:
            return jsonify(user)
        raise NotFoundException()

    def get_user_by_name(self, username: str) -> dict:
        user = self.userModel.get_user_by_name(username)
        if user:
            return user
        raise NotAuthorizedException()

    def create_one(self, json: dict):
        if 'username' not in json or 'role' not in json:
            raise NotFoundException()

        if not UserRollEnum.__contains__(json.get('role')):
            raise NotInEnumException()
        try:
            new_user = self.userModel.create_one(**json)
            return jsonify(new_user)
        except Exception as e:
            if 'duplicate key value' in str(e):
                raise NameAlreadyUsedException()
            raise Exception(e)

    def update_one(self, user_id: int, json: dict):

        if json.__contains__('role') and not UserRollEnum.__contains__(json.get('role')):
            raise NotInEnumException()

        try:
            user = self.userModel.update_one(user_id, **json)
        except Exception as e:
            if 'duplicate key value' in str(e):
                raise NameAlreadyUsedException()
            raise Exception(e)

        if user is not None:
            return jsonify(user)
        raise NotFoundException()

    def delete_one(self, user_id: int):
        self.userModel.delete_one(user_id)
