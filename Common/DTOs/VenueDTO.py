from datetime import datetime


class VenueDTO:

    def __init__(self,
                 el_id: int,
                 room_name: str,
                 notes: str,
                 created_on: datetime
                 ):
        self.el_id = el_id
        self.room_name = room_name
        self.notes = notes
        self.created_on = created_on

    def to_dict(self):
        return {
            "el_id": self.el_id,
            "room_name": self.room_name,
            "notes": self.notes,
            "created_on": self.created_on
        }
