from Common.Exceptions.NotFoundException import NotFoundException
from Common.decorators.format_response_decorator import format_response
from Common.decorators.validate_request_json_decorator import validate_request_json
from Model.VenueModel import VenueModel


def venue_contains_primary_values(venue_json) -> bool:
    return 'room_name' not in venue_json


class VenueBL:

    def __init__(self):
        self.venueModel = VenueModel()

    @format_response
    def get_one(self, venue_id: int):
        return self.venueModel.get_one(venue_id)

    @format_response
    @validate_request_json
    def create_one(self, venue_json):
        if venue_contains_primary_values(venue_json):
            raise NotFoundException()

        return self.venueModel.create_one(**venue_json)

    @format_response
    @validate_request_json
    def update_one(self, venue_json, venue_id: int):
        return self.venueModel.update_one(venue_id, **venue_json)

    def delete_one(self, venue_id: int):
        self.venueModel.delete_one(venue_id)
