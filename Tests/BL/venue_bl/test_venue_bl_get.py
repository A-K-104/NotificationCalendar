from unittest.mock import patch
import unittest

from flask import Flask

from BL import venue_bl
from Commons.Exceptions.NotFoundException import NotFoundException


class TestGetVenue(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.valid_json = {'room_name': '404 TLV'}

    @patch('Models.venue_model.get_venue_by_id')
    def test_get_venue_success(self, mock_get_venue):
        with self.app.app_context():
            mock_get_venue.return_value = self.valid_json
            response = venue_bl.get_venue_bl(1)
            self.assertEqual(response.json, self.valid_json)

    @patch('Models.venue_model.get_venue_by_id')
    def test_get_venue_wrong_id(self, mock_get_venue):
        mock_get_venue.return_value = None
        with self.assertRaises(NotFoundException):
            venue_bl.get_venue_bl(1)


if __name__ == '__main__':
    unittest.main()
