from datetime import datetime


class EventDTO:
    def __init__(self,
                 el_id: int,
                 title: str,
                 date: datetime,
                 organizer: int,
                 guests: str,
                 location: str,
                 venue: int,
                 link: str,
                 notifications: int,
                 description: str,
                 created_on: datetime,
                 ):
        self.el_id = el_id
        self.title = title
        self.date = date
        self.organizer = organizer
        self.guests = guests
        self.location = location
        self.venue = venue
        self.link = link
        self.notifications = notifications
        self.description = description
        self.created_on = created_on

    def to_dict(self):
        return {
            "el_id": self.el_id,
            "title": self.title,
            "date": self.date,
            "organizer": self.organizer,
            "guests": self.guests,
            "location": self.location,
            "venue": self.venue,
            "link": self.link,
            "notifications": self.notifications,
            "description": self.description,
            "created_on": self.created_on
        }