from unittest.mock import patch
import unittest

from flask import Flask

from BL import venue_bl
from Common.Exceptions.MissingValueException import MissingValueException
from Common.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException


class TestCreateVenue(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.valid_json = {'room_name': '404 TLV'}

    @patch('Models.venue_model.create_venue')
    def test_create_venue_success(self, mock_create_venue):
        with self.app.app_context():
            mock_create_venue.return_value = self.valid_json
            response = venue_bl.create_venue_bl(self.valid_json)
            self.assertEqual(response.json, self.valid_json)

    def test_create_venue_missing_room_name(self):
        with self.assertRaises(MissingValueException):
            venue_bl.create_venue_bl({})

    @patch('Models.venue_model.create_venue')
    def test_create_venue_duplicate_key_exception(self, mock_create_venue):
        mock_create_venue.side_effect = Exception("duplicate key value")
        with self.assertRaises(NameAlreadyUsedException):
            venue_bl.create_venue_bl(self.valid_json)


if __name__ == '__main__':
    unittest.main()