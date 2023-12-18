from flask import make_response, Blueprint

from BL.EventBL import EventBL
from Common.Exceptions.NotFoundException import NotFoundException

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


@app.route('/all/creat_on', methods=['GET'])
def get_all_events_by_creat_on():
    try:
        return event_bl.all_by_creat_on()

    except NotFoundException as e:
        return make_response(e.message, e.error_code)

