from unittest.mock import patch
import unittest

from flask import Flask

from BL import venue_bl
from Common.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Common.Exceptions.NotFoundException import NotFoundException


class TestUpdateVenue(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.valid_json = {'room_name': '404 TLV'}

    @patch('Models.venue_model.update_venue_by_id')
    def test_update_venue_success(self, mock_update_venue):
        with self.app.app_context():
            mock_update_venue.return_value = self.valid_json
            response = venue_bl.update_venue_bl(1, self.valid_json)
            self.assertEqual(response.json, self.valid_json)

    @patch('Models.venue_model.update_venue_by_id')
    def test_update_venue_missing_room_name(self, mock_update_venue):
        mock_update_venue.return_value = None
        with self.assertRaises(NotFoundException):
            venue_bl.update_venue_bl(1, self.valid_json)

    @patch('Models.venue_model.update_venue_by_id')
    def test_update_venue_duplicate_key_exception(self, mock_update_venue):
        mock_update_venue.side_effect = Exception("duplicate key value")
        with self.assertRaises(NameAlreadyUsedException):
            venue_bl.update_venue_bl(1, self.valid_json)


if __name__ == '__main__':
    unittest.main()