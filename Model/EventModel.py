from Common.Entities.Event import Event
from Model.ModelBase import ModelBase


class EventModel(ModelBase):
    def __init__(self):
        super().__init__(Event)

    def get_all_sort_by_guests(self):
        return self.get_all_sort_by(Event.guests)

    def get_all_sort_by_creat_on(self):
        return self.get_all_sort_by(Event.created_on)

    def get_all_sort_by_date(self):
        return self.get_all_sort_by(Event.date)
