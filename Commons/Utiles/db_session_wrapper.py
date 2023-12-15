from functools import wraps
from Commons.DI import db_connection

def with_db_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = db_connection.get_db_session()
        try:
            return func(session, *args, **kwargs)
        finally:
            session.close()
    return wrapper