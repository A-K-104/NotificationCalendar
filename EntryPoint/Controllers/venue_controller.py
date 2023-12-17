from flask import make_response, request, Blueprint

from BL.VenueBL import VenueBL
from Common.Exceptions.ContentException import ContentException
from Common.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Common.Exceptions.NotFoundException import NotFoundException

api_version = 1

app = Blueprint('venue_controller', __name__, url_prefix=f'/api/v{api_version}/venue')

venue_bl = VenueBL()


@app.route('/<int:venue_id>', methods=['GET'])
def get_venue(venue_id: int):
    try:
        return venue_bl.get_one(venue_id)

    except NotFoundException as e:
        return make_response(e.message, e.error_code)


@app.route('/', methods=['POST'])
def create_venue():
    try:
        return venue_bl.create_one(request)

    except (NameAlreadyUsedException, NotFoundException, ContentException) as e:
        return make_response(e.message, e.error_code)


@app.route('/<int:venue_id>', methods=['PUT'])
def update_venue(venue_id: int):
    try:
        return venue_bl.update_one(request, venue_id)

    except (NameAlreadyUsedException, NotFoundException, ContentException) as e:
        return make_response(e.message, e.error_code)


@app.route('/<int:venue_id>', methods=['DELETE'])
def delete_venue(venue_id: int):
    try:
        venue_bl.delete_one(venue_id)
        return make_response("Success", 200)
    except NotFoundException as e:
        return make_response(e.message, e.error_code)
