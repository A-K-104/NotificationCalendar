from datetime import datetime


class VenueDTO:

    def __init__(self,
                 element_id: int,
                 room_name: str,
                 notes: str,
                 created_on: datetime
                 ):
        self.element_id = element_id
        self.room_name = room_name
        self.notes = notes
        self.created_on = created_on

    def to_dict(self):
        return {
            "element_id": self.element_id,
            "room_name": self.room_name,
            "notes": self.notes,
            "created_on": self.created_on
        }
