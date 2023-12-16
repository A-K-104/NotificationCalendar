from flask import make_response, request, Blueprint

from BL import event_bl
from Common.Exceptions.MissingValueException import MissingValueException
from Common.Exceptions.NotFoundException import NotFoundException
from Common.Utiles.user_logged_in import user_is_admin

app = Blueprint('event_controller', __name__, url_prefix='/api/v1')


@app.route('/event/<int:event_id>', methods=['GET'])
def get_event(event_id: int):
    try:
        return make_response(event_bl.get_event_bl(event_id), 200)

    except NotFoundException:
        return make_response("Event not found", 404)

    except Exception as e:
        return make_response(f"General error: {e}", 500)


@app.route('/event/all', methods=['GET'])
def get_all_events():
    try:
        return make_response(event_bl.get_all_events_bl(), 200)

    except NotFoundException:
        return make_response("Events not found", 404)

    except Exception as e:
        return make_response(f"General error: {e}", 500)


@app.route('/event', methods=['POST'])
@user_is_admin
def create_event(user: dict):
    if not request.is_json:
        return make_response("Invalid content type, expecting JSON", 415)
    try:
        return make_response(event_bl.create_event_bl(user, request.json), 201)

    except MissingValueException:
        return make_response("Missing required fields", 400)

    except Exception as e:
        return make_response(f"General error: {e}", 500)


@app.route('/event/<int:event_id>', methods=['PUT'])
@user_is_admin
def update_event(user: dict, event_id: int):
    if not request.is_json:
        return make_response("Invalid content type, expecting JSON", 415)
    try:
        return make_response(event_bl.update_event_bl(event_id, request.json), 201)

    except NotFoundException:
        return make_response("Event not found", 404)


    except Exception as e:
        return make_response(f"General error: {e}", 500)


@app.route('/event/<int:event_id>', methods=['DELETE'])
@user_is_admin
def delete_event(user: dict, event_id: int):
    try:
        return make_response(event_bl.delete_event_bl(event_id), 201)

    except NotFoundException:
        return make_response("Event not found", 404)

    except Exception as e:
        return make_response(f"General error: {e}", 500)
