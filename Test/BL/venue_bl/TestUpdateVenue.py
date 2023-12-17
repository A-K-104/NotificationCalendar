import unittest

from BL.VenueBL import VenueBL
from Test.BL.Test_base.TestUpdateOneBase import TestUpdateOneBase


class TestUpdateVenue(TestUpdateOneBase):
    __test__ = True

    def setUp(self):
        super().setUp()
        self.element_bl = VenueBL()
        self.update_id = 1
        self.valid_json = {'room_name': '404 TLV'}
        self.model_name = 'VenueModel.VenueModel'


if __name__ == '__main__':
    unittest.main()
