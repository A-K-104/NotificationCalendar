import unittest

from BL.venue_bl import VenueBL
from Test.BL.Test_base.TestCreateOneBase import TestCreateOneBase


class TestCreateVenue(TestCreateOneBase):
    __test__ = True

    def setUp(self):
        super().setUp()
        self.element_bl = VenueBL()
        self.valid_json = {'room_name': '404 TLV'}
        self.model_name = 'venue_model.VenueModel'


if __name__ == '__main__':
    unittest.main()
