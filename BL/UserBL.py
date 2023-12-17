from Common.DTOs.UserDTO import UserDTO
from Common.Enums.UserRollEnum import UserRollEnum
from Common.Exceptions.MissingArgumentsException import MissingArgumentsException
from Common.Exceptions.NotFoundException import NotFoundException
from Common.Exceptions.NotInEnumException import NotInEnumException
from Common.decorators.format_response_decorator import format_response
from Common.decorators.validate_request_json_decorator import validate_request_json
from Model.UserModel import UserModel


def validate_role(user_json):
    if 'role' in user_json and not UserRollEnum.__contains__(user_json.get('role')):
        raise NotInEnumException()


def event_contains_primary_values(user_json):
    return 'username' not in user_json or 'role' not in user_json


class UserBL:

    def __init__(self):
        self.userModel = UserModel()

    @format_response
    def get_one(self, user_id: int):
        return self.userModel.get_one(user_id)

    def get_user_by_name(self, username: str) -> UserDTO:
        return self.userModel.get_user_by_name(username)

    @format_response
    @validate_request_json
    def create_one(self, user_json):
        if event_contains_primary_values(user_json):
            raise MissingArgumentsException()

        validate_role(user_json)

        return self.userModel.create_one(**user_json)

    @format_response
    @validate_request_json
    def update_one(self, user_json, user_id: int):

        validate_role(user_json)

        return self.userModel.update_one(user_id, **user_json)

    def delete_one(self, user_id: int):
        self.userModel.delete_one(user_id)
