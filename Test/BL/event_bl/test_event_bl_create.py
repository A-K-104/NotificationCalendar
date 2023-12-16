import unittest
from unittest.mock import patch

from Common.Exceptions.MissingValueException import MissingValueException
from flask import Flask

from BL import event_bl


class TestCreateEvent(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.valid_json = {'title': 'The 404 party', 'date': '20 Feb 1991 00:00:00 GMT'}
        self.user = {"id": 1, "role": "ADMIN", "username": "user"}

    @patch('Models.event_model.create_event')
    def test_create_event_success(self, mock_create_event):
        with self.app.app_context():
            # Assert
            mock_create_event.return_value = self.valid_json

            # Act
            response = event_bl.create_event_bl(self.user, self.valid_json)

            # Assert
            self.assertEqual(response.json, self.valid_json)

    def test_create_event_missing_values(self):
        with self.assertRaises(MissingValueException):
            event_bl.create_event_bl(self.user, {})


if __name__ == '__main__':
    unittest.main()
