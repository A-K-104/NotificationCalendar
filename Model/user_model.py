from typing import Union
from Common.Entities.User import User
from Common.Exceptions.NotFoundException import NotFoundException
from Common.Utiles.db_session_wrapper import with_db_session

from Common.Entities.Event import Event
from Model.ModelBase import ModelBase


class UserModel(ModelBase):
    def __init__(self):
        super().__init__(User)

    @with_db_session
    def get_user_by_name(self, session, username: str) -> Union[dict, None]:
        user = session.query(User).filter_by(username=username).first()
        if user is not None:
            return user.to_dict()
        raise NotFoundException
