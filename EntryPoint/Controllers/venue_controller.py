from flask import make_response, request, Blueprint

from BL import venue_bl
from Common.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Common.Exceptions.NotFoundException import NotFoundException
from Common.Utiles.server_error_decorator import server_error_decorator

api_version = 1

app = Blueprint('venue_controller', __name__, url_prefix=f'/api/v{api_version}/venue')


@app.route('/<int:venue_id>', methods=['GET'])
@server_error_decorator
def get_venue(venue_id: int):
    try:
        return make_response(venue_bl.get_venue_bl(venue_id), 200)

    except NotFoundException as e:
        return make_response(e.message, e.error_code)


@app.route('/', methods=['POST'])
@server_error_decorator
def create_venue():
    if not request.is_json:
        return make_response("Invalid content type, expecting JSON", 415)
    try:
        return make_response(venue_bl.create_venue_bl(request.json), 201)

    except NameAlreadyUsedException | NotFoundException as e:
        return make_response(e.message, e.error_code)


@app.route('/<int:venue_id>', methods=['PUT'])
@server_error_decorator
def update_venue(venue_id: int):
    if not request.is_json:
        return make_response("Invalid content type, expecting JSON", 415)
    try:
        return make_response(venue_bl.update_venue_bl(venue_id, request.json), 201)

    except NameAlreadyUsedException | NotFoundException as e:
        return make_response(e.message, e.error_code)


@app.route('/<int:venue_id>', methods=['DELETE'])
@server_error_decorator
def delete_venue(venue_id: int):
    try:
        return make_response(venue_bl.delete_venue_bl(venue_id), 201)

    except NotFoundException as e:
        return make_response(e.message, e.error_code)
