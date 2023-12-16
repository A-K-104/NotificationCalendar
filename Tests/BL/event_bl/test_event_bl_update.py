from unittest.mock import patch
import unittest

from flask import Flask

from BL import event_bl
from Commons.Exceptions.NotFoundException import NotFoundException


class TestUpdateEvent(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.valid_json = {'title': 'The 404 party', 'date': '20 Feb 1991 00:00:00 GMT'}

    @patch('Models.event_model.update_event_by_id')
    def test_update_event_success(self, mock_update_event):
        with self.app.app_context():
            mock_update_event.return_value = self.valid_json
            response = event_bl.update_event_bl(1, self.valid_json)
            self.assertEqual(response.json, self.valid_json)

    @patch('Models.event_model.update_event_by_id')
    def test_update_event_values(self, mock_update_event):
        mock_update_event.return_value = None
        with self.assertRaises(NotFoundException):
            event_bl.update_event_bl(1, self.valid_json)


if __name__ == '__main__':
    unittest.main()
