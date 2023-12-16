from flask import jsonify

from Common.Exceptions.NotFoundException import NotFoundException
from Model.event_model import EventModel


class EventBL:
    def __init__(self):
        self.eventModel = EventModel()

    def get_one(self, event_id: int):
        event = self.eventModel.get_one(event_id)
        if event:
            return jsonify(event)
        raise NotFoundException()

    def get_all(self):
        events = self.eventModel.get_all()
        if events:
            return jsonify(events)
        raise NotFoundException()

    def create_event_bl(self, user: dict, json: dict):
        if 'date' not in json or 'title' not in json:
            raise NotFoundException()

        try:
            json['organizer'] = user['id']
            new_event = self.eventModel.create_one(**json)
            return jsonify(new_event)
        except Exception as e:
            raise Exception(e)

    def update_one(self, event_id: int, json: dict):
        try:
            event = self.eventModel.update_one(event_id, **json)
        except Exception as e:
            raise Exception(e)

        if event is not None:
            return jsonify(event)
        raise NotFoundException()

    def delete_event_bl(self, event_id: int):
        self.eventModel.delete_one(event_id)
