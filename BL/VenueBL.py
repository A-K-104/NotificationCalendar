from Common.Exceptions.NotFoundException import NotFoundException
from Common.decorators.format_response_decorator import format_response_decorator
from Common.decorators.validate_request_json_decorator import validate_request_json_decorator
from Model.VenueModel import VenueModel


class VenueBL:

    def __init__(self):
        self.venueModel = VenueModel()

    @format_response_decorator
    def get_one(self, venue_id: int):
        return self.venueModel.get_one(venue_id)

    @format_response_decorator
    @validate_request_json_decorator
    def create_one(self, json):
        if 'room_name' not in json:
            raise NotFoundException()

        return self.venueModel.create_one(**json)

    @format_response_decorator
    @validate_request_json_decorator
    def update_one(self, json, venue_id: int):
        return self.venueModel.update_one(venue_id, **json)

    def delete_one(self, venue_id: int):
        self.venueModel.delete_one(venue_id)