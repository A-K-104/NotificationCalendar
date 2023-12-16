from datetime import datetime


class VenueDTO:

    def __init__(self,
                 room_name: str,
                 notes: str,
                 created_on: datetime
                 ):
        self.room_name = room_name
        self.notes = notes
        self.created_on = created_on

    def to_dict(self):
        return {
            "room_name": self.room_name,
            "notes": self.notes,
            "created_on": self.created_on
        }
