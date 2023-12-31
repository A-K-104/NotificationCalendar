from typing import Union, Generic, TypeVar

from Common.Exceptions.ForeignKeyException import ForeignKeyException
from Common.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Common.Exceptions.NotFoundException import NotFoundException
from Common.Exceptions.NotValidException import NotValidException
from Common.decorators.db_commit_decorator import db_commit
from Common.decorators.db_session_decorator import with_db_session
from Common.decorators.to_dto_decorator import to_dto

T = TypeVar('T')


def trigger_known_errors(e):
    if 'duplicate key value' in str(e):
        raise NameAlreadyUsedException()
    elif 'is not present in table "venue"' in str(e):
        raise ForeignKeyException()
    raise Exception(e)


class ModelBase(Generic[T]):
    def __init__(self, generic_type: T):
        self.generic_type = generic_type

    @with_db_session
    @to_dto
    def get_one(self, session, object_id: int):
        get_one = session.query(self.generic_type).get(object_id)
        if get_one is not None:
            return get_one
        raise NotFoundException()

    @with_db_session
    @to_dto
    def get_all(self, session) -> Union[list, None]:
        get_all = session.query(self.generic_type).all()
        if get_all is not None:
            return get_all
        raise NotFoundException()

    @with_db_session
    @to_dto
    def get_all_sort_by(self, session, order_by):
        get_all = session.query(self.generic_type).order_by(order_by).all()
        if get_all is not None:
            return get_all
        raise NotFoundException()

    @with_db_session
    @to_dto
    def filter_by(self, session, field_name, field_value):
        if hasattr(self.generic_type, field_name):
            filter_args = {field_name: field_value}
            get_all = session.query(self.generic_type).filter_by(**filter_args).all()
            if get_all:
                return get_all
            else:
                raise NotFoundException()
        else:
            raise NotValidException()

    @with_db_session
    @to_dto
    def create_one(self, session, **kwargs):
        try:
            create_one = self.generic_type(**kwargs)
            session.add(create_one)
            session.commit()
            return create_one
        except Exception as e:
            trigger_known_errors(e)

    @with_db_session
    @to_dto
    def update_one(self, session, object_id: int, **kwargs):
        update_one = session.query(self.generic_type).get(object_id)
        if update_one is None:
            raise NotFoundException()
        try:
            for key, value in kwargs.items():
                if hasattr(update_one, key):
                    setattr(update_one, key, value)
            session.commit()
            return update_one

        except Exception as e:
            trigger_known_errors(e)

    @with_db_session
    @db_commit
    def delete_one(self, session, object_id: int):
        delete_one = session.query(self.generic_type).get(object_id)
        if delete_one:
            session.delete(delete_one)
            return
        raise NotFoundException()
