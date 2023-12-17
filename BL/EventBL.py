from datetime import timedelta

from BL.SchedulerBL import SchedulerBL
from Common.DTOs.UserDTO import UserDTO
from Common.Exceptions.NotFoundException import NotFoundException
from Common.decorators.format_response_decorator import format_response_decorator
from Common.decorators.validate_request_json_decorator import validate_request_json_decorator
from Model.EventModel import EventModel

schedulerBL = SchedulerBL()


# todo: implement
class EventBL:
    def __init__(self):
        self.eventModel = EventModel()
        # todo: DI

    @format_response_decorator
    def get_one(self, event_id: int):
        return self.eventModel.get_one(event_id)

    @format_response_decorator
    def get_all(self):
        return self.eventModel.get_all()

    @format_response_decorator
    @validate_request_json_decorator
    def create_one(self, json, user: UserDTO):
        if 'date' not in json or 'title' not in json:
            raise NotFoundException()
        json['organizer'] = user.el_id
        event = self.eventModel.create_one(**json)

        schedulerBL.create_one(event.date, event.el_id)

        if event.notifications is not None and event.notifications > 0:
            alert_date = event.date - timedelta(seconds=event.notifications)

            schedulerBL.create_one(alert_date, event.id)
        return event

    @format_response_decorator
    @validate_request_json_decorator
    def update_one(self, json, event_id: int):
        return self.eventModel.update_one(event_id, **json)

    def delete_event_bl(self, event_id: int):
        self.eventModel.delete_one(event_id)
