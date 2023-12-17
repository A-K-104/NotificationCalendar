import unittest

from BL.event_bl import EventBL
from Test.BL.Test_base.TestUpdateOneBase import TestUpdateOneBase


class TestUpdateEvent(TestUpdateOneBase):
    __test__ = True

    def setUp(self):
        super().setUp()
        self.element_bl = EventBL()
        self.update_id = 1
        self.valid_json = {'title': 'The 404 party', 'date': '20 Feb 1991 00:00:00 GMT'}
        self.model_name = 'event_model.EventModel'


if __name__ == '__main__':
    unittest.main()
