from typing import Union

from Common.DTOs.UserDTO import UserDTO
from Common.Entities.User import User
from Common.Exceptions.NotFoundException import NotFoundException
from Common.decorators.db_session_decorator import with_db_session_decorator
from Common.decorators.to_dto_decorator import to_dto_decorator
from Model.ModelBase import ModelBase


class UserModel(ModelBase):
    def __init__(self):
        super().__init__(User)

    @with_db_session_decorator
    @to_dto_decorator
    def get_user_by_name(self, session, username: str) -> Union[UserDTO, None]:
        user = session.query(User).filter_by(username=username).first()
        if user is not None:
            return user
        raise NotFoundException
