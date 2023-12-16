from flask import jsonify

from Commons.Exceptions.MissingValueException import MissingValueException
from Commons.Exceptions.NotFoundException import NotFoundException
from Models import event_model


def get_event_bl(event_id: int):
    event = event_model.get_event_by_id(event_id)
    if event:
        return jsonify(event)
    raise NotFoundException()


def get_all_events_bl():
    events = event_model.get_all_events()
    if events:
        return jsonify(events)
    raise NotFoundException()


def create_event_bl(user: dict, json: dict):
    if 'date' not in json or 'title' not in json:
        raise MissingValueException()

    try:
        new_event = event_model.create_event(user['id'], **json)
        return jsonify(new_event)
    except Exception as e:
        raise Exception(e)


def update_event_bl(event_id: int, json: dict):
    try:
        event = event_model.update_event_by_id(event_id, **json)
    except Exception as e:
        raise Exception(e)

    if event is not None:
        return jsonify(event)
    raise NotFoundException()


def delete_event_bl(event_id: int):
    if event_model.delete_event_by_id(event_id):
        return "Event was deleted"
    raise NotFoundException()
