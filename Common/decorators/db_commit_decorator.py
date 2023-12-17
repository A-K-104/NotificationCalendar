from functools import wraps



def db_commit(func):
    @wraps(func)
    def wrapper(self, session, *args, **kwargs):
        response = func(self, session, *args, **kwargs)
        session.commit()
        return response

    return wrapper
