from functools import wraps
from Common.DI import db_connection


def with_db_session(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        session = db_connection.get_db_session()
        try:
            return func(self, session, *args, **kwargs)
        finally:
            session.close()

    return wrapper
