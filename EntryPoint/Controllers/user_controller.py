from flask import make_response, request, Blueprint

from BL import user_bl
from Common.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Common.Exceptions.NotFoundException import NotFoundException
from Common.Exceptions.NotInEnumException import NotInEnumException
from Common.Utiles.server_error_decorator import server_error_decorator

app = Blueprint('user_controller', __name__, url_prefix='/api/v1')


@app.route('/user/<int:user_id>', methods=['GET'])
@server_error_decorator
def get_user(user_id: int):
    try:

        return make_response(user_bl.get_user_bl(user_id), 200)

    except NotFoundException as e:
        return make_response(e.message, e.error_code)



@app.route('/user', methods=['POST'])
@server_error_decorator
def create_user():
    if not request.is_json:
        return make_response("Invalid content type, expecting JSON", 415)
    try:
        return make_response(user_bl.create_user_bl(request.json), 201)

    except NameAlreadyUsedException | NotInEnumException | NotFoundException as e:
        return make_response(e.message, e.error_code)


@app.route('/user/<int:user_id>', methods=['PUT'])
@server_error_decorator
def update_user(user_id: int):
    if not request.is_json:
        return make_response("Invalid content type, expecting JSON", 415)
    try:
        return make_response(user_bl.update_user_bl(user_id, request.json), 201)

    except NameAlreadyUsedException | NotInEnumException | NotFoundException as e:
        return make_response(e.message, e.error_code)



@app.route('/user/<int:user_id>', methods=['DELETE'])
@server_error_decorator
def delete_user(user_id: int):
    try:
        return make_response(user_bl.delete_user_bl(user_id), 201)

    except NotFoundException as e:
        return make_response(e.message, e.error_code)

