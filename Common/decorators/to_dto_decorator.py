from functools import wraps


def to_dto_decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        element = func(self, *args, **kwargs)
        if type(element) == list:
            return [e.to_dto() for e in element]
        return element.to_dto()

    return wrapper
