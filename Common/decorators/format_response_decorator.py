from functools import wraps

from flask import jsonify


def format_response(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        response = func(self, *args, **kwargs)
        if type(response) == list:
            return jsonify([r.to_dict() for r in response])
        return jsonify(response.to_dict())

    return wrapper
