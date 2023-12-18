from Common.Entities.Event import Event
from Model.ModelBase import ModelBase


class EventModel(ModelBase):
    def __init__(self):
        super().__init__(Event)

    def get_all_sort_by_guests(self):
        return self.get_all_sort_by(Event.guests)

    def get_all_sort_by_created_on(self):
        return self.get_all_sort_by(Event.created_on)

    def get_all_sort_by_date(self):
        return self.get_all_sort_by(Event.date)

    def filter_by_venue(self, value):
        return self.filter_by('venue', value)

    def filter_by_location(self, value):
        return self.filter_by('location', value)
