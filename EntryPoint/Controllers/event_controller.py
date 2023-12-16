from flask import make_response, request, Blueprint

from BL import event_bl
from BL.event_bl import EventBL
from Common.Exceptions.NotFoundException import NotFoundException
from Common.Utiles.server_error_decorator import server_error_decorator
from Common.Utiles.user_logged_in import user_is_admin

api_version = 1
app = Blueprint('event_controller', __name__, url_prefix=f'/api/v{api_version}/event')  # todo validate use of __name__

event_bl_g = EventBL()


@app.route('/<int:event_id>', methods=['GET'])
@server_error_decorator
def get_event(event_id: int):
    try:
        return event_bl_g.get_one(event_id)

    except NotFoundException as e:
        return make_response(e.message, e.error_code)


@app.route('/all', methods=['GET'])
@server_error_decorator
def get_all_events():
    try:
        return event_bl_g.get_all()

    except NotFoundException as e:
        return make_response(e.message, e.error_code)


@app.route('/', methods=['POST'])
@user_is_admin
@server_error_decorator
def create_event(user: dict):
    if not request.is_json:
        return make_response("Invalid content type, expecting JSON", 415)
    try:
        return event_bl_g.create_event_bl(user, request.json)

    except NotFoundException as e:
        return make_response(e.message, e.error_code)


@app.route('/<int:event_id>', methods=['PUT'])
@user_is_admin
@server_error_decorator
def update_event(_: dict, event_id: int):
    if not request.is_json:
        return make_response("Invalid content type, expecting JSON", 415)
    try:
        return event_bl_g.update_one(event_id, request.json)

    except NotFoundException as e:
        return make_response(e.message, e.error_code)


@app.route('/<int:event_id>', methods=['DELETE'])
@user_is_admin
@server_error_decorator
def delete_event(_: dict, event_id: int):
    try:
        event_bl_g.delete_event_bl(event_id)
        return make_response("Success", 200)  # todo: carper
    except NotFoundException as e:
        return make_response(e.message, e.error_code)
