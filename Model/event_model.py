from Common.Entities.Event import Event
from Model.ModelBase import ModelBase


class EventModel(ModelBase):
    def __init__(self):
        super().__init__(Event)
