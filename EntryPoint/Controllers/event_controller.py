from flask import make_response, request, Blueprint

from BL.EventBL import EventBL
from Common.DTOs.UserDTO import UserDTO
from Common.Exceptions.ContentException import ContentException
from Common.Exceptions.MissingArgumentsException import MissingArgumentsException
from Common.Exceptions.NotFoundException import NotFoundException
from Common.decorators.user_logged_in_decorator import user_is_admin

api_version = 1
app = Blueprint('event_controller', __name__, url_prefix=f'/api/v{api_version}/event')

event_bl = EventBL()

@app.route('/<int:event_id>', methods=['GET'])
def get_event(event_id: int):
    try:
        return event_bl.get_one(event_id)

    except NotFoundException as e:
        return make_response(e.message, e.error_code)


@app.route('/all', methods=['GET'])
def get_all_events():
    try:
        return event_bl.get_all()

    except NotFoundException as e:
        return make_response(e.message, e.error_code)


@app.route('/', methods=['POST'])
@user_is_admin
def create_event(user: UserDTO):
    try:
        return event_bl.create_one(request, user)

    except (NotFoundException, MissingArgumentsException) as e:
        return make_response(e.message, e.error_code)


@app.route('/<int:event_id>', methods=['PUT'])
@user_is_admin
def update_event(_: dict, event_id: int):
    try:
        return event_bl.update_one(request, event_id)

    except (NotFoundException, ContentException) as e:
        return make_response(e.message, e.error_code)


@app.route('/<int:event_id>', methods=['DELETE'])
@user_is_admin
def delete_event(_: dict, event_id: int):
    try:
        event_bl.delete_event_bl(event_id)
        return make_response("Success", 200)
    except NotFoundException as e:
        return make_response(e.message, e.error_code)
