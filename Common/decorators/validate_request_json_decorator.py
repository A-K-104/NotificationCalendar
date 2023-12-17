from functools import wraps

from Common.Exceptions.ContentException import ContentException


def validate_request_json(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        if not request.is_json:
            raise ContentException()

        json = request.json

        return func(self, json, *args, **kwargs)

    return wrapper
