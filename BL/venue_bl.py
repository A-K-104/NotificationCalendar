from flask import jsonify

from Common.Exceptions.MissingValueException import MissingValueException
from Common.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Common.Exceptions.NotFoundException import NotFoundException
from Model import venue_model


def get_venue_bl(venue_id: int):
    venue = venue_model.get_venue_by_id(venue_id)
    if venue:
        return jsonify(venue)
    raise NotFoundException()


def create_venue_bl(json: dict):
    if 'room_name' not in json:
        raise MissingValueException()

    try:
        new_venue = venue_model.create_venue(**json)
        return jsonify(new_venue)
    except Exception as e:
        if 'duplicate key value' in str(e):
            raise NameAlreadyUsedException()
        raise Exception(e)


def update_venue_bl(venue_id: int, json: dict):
    try:
        venue = venue_model.update_venue_by_id(venue_id, **json)
    except Exception as e:
        if 'duplicate key value' in str(e):
            raise NameAlreadyUsedException()
        raise Exception(e)

    if venue is not None:
        return jsonify(venue)
    raise NotFoundException()


def delete_venue_bl(venue_id: int):
    if venue_model.delete_venue_by_id(venue_id):
        return "Venue deleted"
    raise NotFoundException()
