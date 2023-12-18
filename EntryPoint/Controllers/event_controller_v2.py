from flask import make_response, Blueprint, request

from BL.EventBL import EventBL
from Common.Exceptions.MissingArgumentsException import MissingArgumentsException
from Common.Exceptions.NotFoundException import NotFoundException
from Common.Exceptions.NotValidException import NotValidException

api_version = 2
app = Blueprint('event_controller_v2', __name__, url_prefix=f'/api/v{api_version}/event')

event_bl = EventBL()


@app.route('/all/date', methods=['GET'])
def get_all_events_by_date():
    try:
        return event_bl.all_by_date()

    except NotFoundException as e:
        return make_response(e.message, e.error_code)


@app.route('/all/guests', methods=['GET'])
def get_all_events_by_guests():
    try:
        return event_bl.all_by_guests()

    except NotFoundException as e:
        return make_response(e.message, e.error_code)


@app.route('/all/created_on', methods=['GET'])
def get_all_events_by_create_on():
    try:
        return event_bl.all_by_created_on()

    except NotFoundException as e:
        return make_response(e.message, e.error_code)


@app.route('/filter/venue/<int:event_id>', methods=['GET'])
def get_filter_by_venue(event_id: int):
    try:
        return event_bl.filter_by_venue(event_id)

    except (NotFoundException, NotValidException) as e:
        return make_response(e.message, e.error_code)


@app.route('/filter/location/', methods=['GET'])
def get_filter_by_location():
    try:
        return event_bl.filter_by_location(request)

    except (NotFoundException, NotValidException, MissingArgumentsException) as e:
        return make_response(e.message, e.error_code)
