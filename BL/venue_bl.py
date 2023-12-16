from flask import jsonify

from Common.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Common.Exceptions.NotFoundException import NotFoundException
from Model.venue_model import VenueModel


class VenueBL:

    def __init__(self):
        self.venueModel = VenueModel()

    def get_venue_bl(self, venue_id: int):
        venue = self.venueModel.get_one(venue_id)
        if venue:
            return jsonify(venue)
        raise NotFoundException()

    def create_venue_bl(self, json: dict):
        if 'room_name' not in json:
            raise NotFoundException()

        try:
            new_venue = self.venueModel.create_one(**json)
            return jsonify(new_venue)
        except Exception as e:
            if 'duplicate key value' in str(e):
                raise NameAlreadyUsedException()
            raise Exception(e)

    def update_venue_bl(self, venue_id: int, json: dict):
        try:
            venue = self.venueModel.update_one(venue_id, **json)
        except Exception as e:
            if 'duplicate key value' in str(e):
                raise NameAlreadyUsedException()
            raise Exception(e)

        if venue is not None:
            return jsonify(venue)
        raise NotFoundException()

    def delete_venue_bl(self, venue_id: int):
        self.venueModel.delete_one(venue_id)
