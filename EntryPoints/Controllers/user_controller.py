from flask import make_response, request, Blueprint

from BL import user_bl
from Commons.Exceptions.MissingValueException import MissingValueException
from Commons.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Commons.Exceptions.NotFoundException import NotFoundException
from Commons.Exceptions.NotInEnumException import NotInEnumException

app = Blueprint('user_controller', __name__, url_prefix='/api/v1')


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    try:
        return make_response(user_bl.get_user_bl(user_id), 200)

    except NotFoundException:
        return make_response("User not found", 404)

    except Exception as e:
        return make_response(f"General error: {e}", 500)


@app.route('/user', methods=['POST'])
def create_user():
    if not request.is_json:
        return make_response("Invalid content type, expecting JSON", 415)
    try:
        return make_response(user_bl.create_user_bl(request.json), 201)

    except MissingValueException:
        return make_response("Missing required fields", 400)

    except NotInEnumException:
        return make_response("The selected role is allowed", 400)

    except NameAlreadyUsedException:
        return make_response("Error creating user: username already in use", 400)

    except Exception as e:
        return make_response(f"General error: {e}", 500)


@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id: int):
    if not request.is_json:
        return make_response("Invalid content type, expecting JSON", 415)
    try:
        return make_response(user_bl.update_user_bl(user_id, request.json), 201)

    except NotFoundException:
        return make_response("User not found", 404)

    except NotInEnumException:
        return make_response("The selected role is allowed", 400)

    except NameAlreadyUsedException:
        return make_response(f"Error updating user: username already in use", 400)

    except Exception as e:
        return make_response(f"General error: {e}", 500)


@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    try:
        return make_response(user_bl.delete_user_bl(user_id), 201)

    except NotFoundException:
        return make_response("User not found", 404)

    except Exception as e:
        return make_response(f"General error: {e}", 500)
