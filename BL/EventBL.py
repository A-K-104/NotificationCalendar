from datetime import timedelta

from BL.SchedulerBL import SchedulerBL
from Common.DTOs.UserDTO import UserDTO
from Common.Exceptions.MissingArgumentsException import MissingArgumentsException
from Common.Utiles.Utiles import to_seconds
from Common.decorators.format_response_decorator import format_response
from Common.decorators.validate_request_json_decorator import validate_request_json
from Model.EventModel import EventModel


def event_filter_contains_primary_value(request) -> bool:
    return 'location' not in request.args


def event_contains_primary_values(event_json) -> bool:
    return 'date' not in event_json or 'title' not in event_json


def event_contains_notification(event_json) -> bool:
    return 'notifications' not in event_json


def event_update_date_or_notifications(event_json) -> bool:
    return 'notifications' in event_json or 'date' in event_json


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
        event = self.eventModel.update_one(event_id, **event_json)

        self.post_event_update(event, event_json)
        return event

    @format_response
    def all_by_date(self):
        return self.eventModel.get_all_sort_by_date()

    @format_response
    def all_by_guests(self):
        return self.eventModel.get_all_sort_by_guests()

    @format_response
    def all_by_created_on(self):
        return self.eventModel.get_all_sort_by_created_on()

    @format_response
    def filter_by_venue(self, venue_id):
        return self.eventModel.filter_by_venue(venue_id)

    @format_response
    def filter_by_location(self, request):
        if event_filter_contains_primary_value(request):
            raise MissingArgumentsException()

        location = request.args.get("location")
        return self.eventModel.filter_by_location(location)

    def delete_event_bl(self, event_id: int):
        self.schedulerBL.delete_many(str(event_id))
        self.eventModel.delete_one(event_id)

    def post_event_update(self, event, event_json):
        if event_update_date_or_notifications(event_json):
            self.schedulerBL.delete_many(event.element_id)
            self.post_event_creation(event)

    def post_event_creation(self, event_entity):
        if event_entity.notifications is not None:
            alert_date = calculate_date_time_of_alert(event_entity)
            self.schedulerBL.create_one(event_entity.element_id, alert_date)
        self.schedulerBL.create_one(event_entity.element_id, event_entity.date)

    def post_populate_event_dto(self, event_dto, user):
        if event_contains_primary_values(event_dto):
            raise MissingArgumentsException()
        self.declare_organizer_field(event_dto, user)
        if event_contains_notification(event_dto):
            self.add_default_notification(event_dto)

    @staticmethod
    def add_default_notification(event_json):
        event_json['notifications'] = to_seconds(30)  # set default alert

    @staticmethod
    def declare_organizer_field(event_json, user):
        event_json['organizer'] = user.element_id  # set default user
