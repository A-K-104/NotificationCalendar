from typing import Union, Generic, TypeVar

from Common.Exceptions.NotFoundException import NotFoundException
from Common.Utiles.db_session_decorator import with_db_session
from Common.Utiles.to_dto_decorator import to_dto

T = TypeVar('T')


class ModelBase(Generic[T]):
    def __init__(self, generic_type: T):
        self.generic_type = generic_type

    @with_db_session
    @to_dto
    def get_one(self, session, object_id: int) -> Union[dict, None]:
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
    def create_one(self, session, **kwargs) -> dict:
        create_one = self.generic_type(**kwargs)
        session.add(create_one)
        session.commit()  # todo add decorator for save_async shit
        return create_one

    @with_db_session
    @to_dto
    def update_one(self, session, object_id: int, **kwargs) -> Union[dict, None]:
        update_one = session.query(self.generic_type).get(object_id)
        for key, value in kwargs.items():
            if hasattr(update_one, key):
                setattr(update_one, key, value)
        session.commit()
        return update_one

    @with_db_session
    def delete_one(self, session, object_id: int):
        delete_one = session.query(self.generic_type).get(object_id)
        if delete_one:
            session.delete(delete_one)
            session.commit()
            return
        raise NotFoundException()
