import unittest

from BL.venue_bl import VenueBL
from Test.BL.Test_base.TestUpdateOneBase import TestUpdateOneBase


class TestUpdateVenue(TestUpdateOneBase):
    __test__ = True

    def setUp(self):
        super().setUp()
        self.element_bl = VenueBL()
        self.update_id = 1
        self.valid_json = {'room_name': '404 TLV'}
        self.model_name = 'venue_model.VenueModel'


if __name__ == '__main__':
    unittest.main()
