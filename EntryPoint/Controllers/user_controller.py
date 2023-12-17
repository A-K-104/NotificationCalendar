from flask import make_response, request, Blueprint

from BL.UserBL import UserBL
from Common.Exceptions.ContentException import ContentException
from Common.Exceptions.MissingArgumentsException import MissingArgumentsException
from Common.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Common.Exceptions.NotFoundException import NotFoundException
from Common.Exceptions.NotInEnumException import NotInEnumException

api_version = 1
app = Blueprint('user_controller', __name__, url_prefix=f'/api/v{api_version}/user')

user_bl = UserBL()


@app.route('/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    try:

        return user_bl.get_one(user_id)

    except NotFoundException as e:
        return make_response(e.message, e.error_code)


@app.route('/', methods=['POST'])
def create_user():
    try:
        return user_bl.create_one(request)

    except (NameAlreadyUsedException, NotInEnumException, ContentException, MissingArgumentsException) as e:
        return make_response(e.message, e.error_code)


@app.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id: int):
    try:
        return user_bl.update_one(request, user_id)

    except (NameAlreadyUsedException, NotInEnumException, NotFoundException, ContentException) as e:
        return make_response(e.message, e.error_code)


@app.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    try:
        user_bl.delete_one(user_id)
        return make_response("Success", 200)
    except NotFoundException as e:
        return make_response(e.message, e.error_code)
