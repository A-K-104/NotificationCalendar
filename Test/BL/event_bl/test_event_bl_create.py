from unittest.mock import patch
import unittest

from flask import Flask

from BL import event_bl
from Common.Exceptions.MissingValueException import MissingValueException


class TestCreateEvent(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.valid_json = {'title': 'The 404 party', 'date': '20 Feb 1991 00:00:00 GMT'}
        self.user = {"id": 1, "role": "ADMIN", "username": "user"}

    @patch('Models.event_model.create_event')
    def test_create_event_success(self, mock_create_event):
        with self.app.app_context():
            mock_create_event.return_value = self.valid_json
            response = event_bl.create_event_bl(self.user, self.valid_json)
            self.assertEqual(response.json, self.valid_json)

    def test_create_event_missing_values(self):
        with self.assertRaises(MissingValueException):
            event_bl.create_event_bl(self.user, {})


if __name__ == '__main__':
    unittest.main()
