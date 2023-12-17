import datetime
import unittest
from unittest.mock import patch

from flask import Flask

from BL.EventBL import EventBL
from Common.DTOs.UserDTO import UserDTO
from Test.BL.Test_base.TestCreateOneBase import TestCreateOneBase


class TestCreateEvent(TestCreateOneBase):
    __test__ = True

    def setUp(self):
        self.app = Flask(__name__)
        self.element_bl = EventBL()
        self.valid_json = {'title': 'The 404 party', 'date': '20 Feb 1991 00:00:00 GMT', 'notifications': 1800,
                           'organizer': 1}
        self.model_name = 'EventModel.EventModel'
        user: UserDTO = UserDTO(1, "WebWizard", "ADMIN", datetime.datetime.now())
        self.additional_data = [user]

    def test_create_one_should_success(self):
        with patch(f'BL.EventBL.EventBL.post_event_creation', return_value=None):
            super().test_create_one_should_success()


if __name__ == '__main__':
    unittest.main()
