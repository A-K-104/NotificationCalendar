import datetime
import unittest

from flask import Flask

from BL.event_bl import EventBL
from Common.DTOs.UserDTO import UserDTO
from Test.BL.Test_base.TestCreateOneBase import TestCreateOneBase


class TestCreateEvent(TestCreateOneBase):
    __test__ = True

    def setUp(self):
        self.app = Flask(__name__)
        self.element_bl = EventBL()
        self.valid_json = {'title': 'The 404 party', 'date': '20 Feb 1991 00:00:00 GMT'}
        self.model_name = 'event_model.EventModel'
        user: UserDTO = UserDTO(1, "WebWizard", "ADMIN", datetime.datetime.now())
        self.additional_data = [user]


if __name__ == '__main__':
    unittest.main()
