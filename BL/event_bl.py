from Common.Exceptions.NotFoundException import NotFoundException
from Common.Utiles.format_response_decorator import format_response_decorator
from Model.event_model import EventModel


# todo: implement
class EventBL:
    def __init__(self):
        self.eventModel = EventModel()
        # todo: DI

    @format_response_decorator
    def get_one(self, event_id: int):
        event = self.eventModel.get_one(event_id)
        if event:
            return event
        raise NotFoundException()

    @format_response_decorator
    def get_all(self):
        events = self.eventModel.get_all()
        if events:
            return events
        raise NotFoundException()

    @format_response_decorator
    def create_event_bl(self, user: dict, json: dict):
        if 'date' not in json or 'title' not in json:
            raise NotFoundException()

        try:
            json['organizer'] = user['id']
            new_event = self.eventModel.create_one(**json)
            return new_event
        except Exception as e:
            raise Exception(e)

    @format_response_decorator
    def update_one(self, event_id: int, json: dict):
        try:
            event = self.eventModel.update_one(event_id, **json)
        except Exception as e:
            raise Exception(e)

        if event is not None:
            return event
        raise NotFoundException()

    def delete_event_bl(self, event_id: int):
        self.eventModel.delete_one(event_id)
