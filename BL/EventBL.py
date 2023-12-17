from datetime import timedelta

from BL.SchedulerBL import SchedulerBL
from Common.DTOs.UserDTO import UserDTO
from Common.Exceptions.NotFoundException import NotFoundException
from Common.Utiles.Utiles import to_seconds
from Common.decorators.format_response_decorator import format_response
from Common.decorators.validate_request_json_decorator import validate_request_json
from Model.EventModel import EventModel


def event_contains_primary_values(event_json) -> bool:
    return 'date' not in event_json or 'title' not in event_json


def event_contains_notification(event_json) -> bool:
    return 'notifications' not in event_json


def calculate_date_time_of_alert(event_entity):
    return event_entity.date - timedelta(seconds=event_entity.notifications)


class EventBL:
    def __init__(self):
        self.eventModel = EventModel()
        self.schedulerBL = SchedulerBL()
        # todo: DI

    @format_response
    def get_one(self, event_id: int):
        return self.eventModel.get_one(event_id)

    @format_response
    def get_all(self):
        return self.eventModel.get_all()

    @format_response
    @validate_request_json
    def create_one(self, event_dto, user: UserDTO):
        self.post_populate_event_dto(event_dto, user)
        event_entity = self.eventModel.create_one(**event_dto)
        self.post_event_creation(event_entity)

        return event_entity

    @format_response
    @validate_request_json
    def update_one(self, event_json, event_id: int):
        return self.eventModel.update_one(event_id, **event_json)

    def delete_event_bl(self, event_id: int):
        self.eventModel.delete_one(event_id)

    def post_event_creation(self, event_entity):
        alert_date = calculate_date_time_of_alert(event_entity)
        self.schedulerBL.create_one(event_entity.element_id, event_entity.date)
        self.schedulerBL.create_one(event_entity.element_id, alert_date)

    def post_populate_event_dto(self, event_dto, user):
        if event_contains_primary_values(event_dto):
            raise NotFoundException()  # todo argument exception
        self.declare_organizer_field(event_dto, user)
        if event_contains_notification(event_dto):
            self.add_default_notification(event_dto)

    @staticmethod
    def add_default_notification(event_json):
        event_json['notifications'] = to_seconds(30)  # set default alert

    @staticmethod
    def declare_organizer_field(event_json, user):
        event_json['organizer'] = user.element_id  # set default user
