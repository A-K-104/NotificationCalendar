from Common.Entities.Venue import Venue
from Model.ModelBase import ModelBase


class VenueModel(ModelBase):
    def __init__(self):
        super().__init__(Venue)
