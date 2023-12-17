import unittest
from unittest.mock import patch

from BL.EventBL import EventBL
from Test.BL.Test_base.TestUpdateOneBase import TestUpdateOneBase


class TestUpdateEvent(TestUpdateOneBase):
    __test__ = True

    def setUp(self):
        super().setUp()
        self.element_bl = EventBL()
        self.update_id = 1
        self.valid_json = {'title': 'The 404 party', 'date': '20 Feb 1991 00:00:00 GMT'}
        self.model_name = 'EventModel.EventModel'


    def test_update_one_should_success(self):
        with patch(f'BL.EventBL.EventBL.post_event_update', return_value=None):
            super().test_update_one_should_success()

if __name__ == '__main__':
    unittest.main()
