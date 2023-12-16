from flask import make_response, request, Blueprint

from BL import venue_bl
from Commons.Exceptions.MissingValueException import MissingValueException
from Commons.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Commons.Exceptions.NotFoundException import NotFoundException

app = Blueprint('venue_controller', __name__, url_prefix='/api/v1')


@app.route('/venue/<int:venue_id>', methods=['GET'])
def get_venue(venue_id: int):
    try:
        return make_response(venue_bl.get_venue_bl(venue_id), 200)

    except NotFoundException:
        return make_response("Venue not found", 404)

    except Exception as e:
        return make_response(f"General error: {e}", 500)


@app.route('/venue', methods=['POST'])
def create_venue():
    if not request.is_json:
        return make_response("Invalid content type, expecting JSON", 415)
    try:
        return make_response(venue_bl.create_venue_bl(request.json), 201)

    except MissingValueException:
        return make_response("Missing required fields", 400)

    except NameAlreadyUsedException:
        return make_response("Error creating venue: room name already in use", 400)

    except Exception as e:
        return make_response(f"General error: {e}", 500)


@app.route('/venue/<int:venue_id>', methods=['PUT'])
def update_venue(venue_id: int):
    if not request.is_json:
        return make_response("Invalid content type, expecting JSON", 415)
    try:
        return make_response(venue_bl.update_venue_bl(venue_id, request.json), 201)

    except NotFoundException:
        return make_response("Venue not found", 404)

    except NameAlreadyUsedException:
        return make_response(f"Error creating venue: room name already in use", 400)

    except Exception as e:
        return make_response(f"General error: {e}", 500)


@app.route('/venue/<int:venue_id>', methods=['DELETE'])
def delete_venue(venue_id: int):
    try:
        return make_response(venue_bl.delete_venue_bl(venue_id), 201)

    except NotFoundException:
        return make_response("Venue not found", 404)

    except Exception as e:
        return make_response(f"General error: {e}", 500)
