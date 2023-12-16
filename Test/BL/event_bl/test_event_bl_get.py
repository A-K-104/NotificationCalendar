from unittest.mock import patch
import unittest

from flask import Flask

from BL import event_bl
from Common.Exceptions.NotFoundException import NotFoundException


class TestGetEvent(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.valid_json = {'title': 'The 404 party', 'date': '20 Feb 1991 00:00:00 GMT'}

    @patch('Models.event_model.get_event_by_id')
    def test_get_event_success(self, mock_get_event):
        with self.app.app_context():
            mock_get_event.return_value = self.valid_json
            response = event_bl.get_event_bl(1)
            self.assertEqual(response.json, self.valid_json)

    @patch('Models.event_model.get_event_by_id')
    def test_get_event_wrong_id(self, mock_get_event):
        mock_get_event.return_value = None
        with self.assertRaises(NotFoundException):
            event_bl.get_event_bl(1)

    @patch('Models.event_model.get_all_events')
    def test_get_all_event_success(self, mock_get_event):
        with self.app.app_context():
            mock_get_event.return_value = [self.valid_json]
            response = event_bl.get_all_events_bl()
            self.assertEqual(response.json, [self.valid_json])


if __name__ == '__main__':
    unittest.main()
