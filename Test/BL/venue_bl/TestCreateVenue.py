import unittest

from BL.VenueBL import VenueBL
from Test.BL.Test_base.TestCreateOneBase import TestCreateOneBase


class TestCreateVenue(TestCreateOneBase):
    __test__ = True

    def setUp(self):
        super().setUp()
        self.element_bl = VenueBL()
        self.valid_json = {'room_name': '404 TLV'}
        self.model_name = 'VenueModel.VenueModel'


if __name__ == '__main__':
    unittest.main()
