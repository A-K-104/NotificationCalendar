from Common.DTOs.UserDTO import UserDTO
from Common.Enums.UserRollEnum import UserRollEnum
from Common.Exceptions.NotFoundException import NotFoundException
from Common.Exceptions.NotInEnumException import NotInEnumException
from Common.decorators.format_response_decorator import format_response_decorator
from Common.decorators.validate_request_json_decorator import validate_request_json_decorator
from Model.UserModel import UserModel


class UserBL:

    def __init__(self):
        self.userModel = UserModel()

    @format_response_decorator
    def get_one(self, user_id: int):
        return self.userModel.get_one(user_id)

    def get_user_by_name(self, username: str) -> UserDTO:
        return self.userModel.get_user_by_name(username)

    @format_response_decorator
    @validate_request_json_decorator
    def create_one(self, json):
        if 'username' not in json or 'role' not in json:
            raise NotFoundException()

        if not UserRollEnum.__contains__(json.get('role')):
            raise NotInEnumException()

        return self.userModel.create_one(**json)

    @format_response_decorator
    @validate_request_json_decorator
    def update_one(self, json, user_id: int):

        if json.__contains__('role') and not UserRollEnum.__contains__(json.get('role')):
            raise NotInEnumException()

        return self.userModel.update_one(user_id, **json)

    def delete_one(self, user_id: int):
        self.userModel.delete_one(user_id)
