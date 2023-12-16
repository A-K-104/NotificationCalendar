from typing import Union, Generic, TypeVar

from Common.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Common.Exceptions.NotFoundException import NotFoundException
from Common.decorators.db_session_decorator import with_db_session_decorator
from Common.decorators.to_dto_decorator import to_dto_decorator

T = TypeVar('T')


class ModelBase(Generic[T]):
    def __init__(self, generic_type: T):
        self.generic_type = generic_type

    @with_db_session_decorator
    @to_dto_decorator
    def get_one(self, session, object_id: int) -> Union[dict, None]:
        get_one = session.query(self.generic_type).get(object_id)
        if get_one is not None:
            return get_one
        raise NotFoundException()

    @with_db_session_decorator
    @to_dto_decorator
    def get_all(self, session) -> Union[list, None]:
        get_all = session.query(self.generic_type).all()
        if get_all is not None:
            return get_all
        raise NotFoundException()

    @with_db_session_decorator
    @to_dto_decorator
    def create_one(self, session, **kwargs) -> dict:
        try:
            create_one = self.generic_type(**kwargs)
            session.add(create_one)
            session.commit()  # todo add decorator for save_async shit
            return create_one
        except Exception as e:
            if 'duplicate key value' in str(e):
                raise NameAlreadyUsedException()
            raise Exception(e)

    @with_db_session_decorator
    @to_dto_decorator
    def update_one(self, session, object_id: int, **kwargs) -> Union[dict, None]:
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
            if 'duplicate key value' in str(e):
                raise NameAlreadyUsedException()
            raise Exception(e)

    @with_db_session_decorator
    def delete_one(self, session, object_id: int):
        delete_one = session.query(self.generic_type).get(object_id)
        if delete_one:
            session.delete(delete_one)
            session.commit()
            return
        raise NotFoundException()
