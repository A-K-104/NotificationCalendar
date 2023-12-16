from unittest.mock import patch
import unittest

from flask import Flask

from BL import user_bl
from Commons.Exceptions.MissingValueException import MissingValueException
from Commons.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException


class TestCreateUser(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.valid_json = {'username': 'c0ff33', 'role': 'admin'}

    @patch('Models.user_model.create_user')
    def test_create_user_success(self, mock_create_user):
        with self.app.app_context():
            mock_create_user.return_value = self.valid_json
            response = user_bl.create_user_bl(self.valid_json)
            self.assertEqual(response.json, self.valid_json)

    def test_create_user_missing_room_name(self):
        with self.assertRaises(MissingValueException):
            user_bl.create_user_bl({})

    @patch('Models.user_model.create_user')
    def test_create_user_duplicate_key_exception(self, mock_create_user):
        mock_create_user.side_effect = Exception("duplicate key value")
        with self.assertRaises(NameAlreadyUsedException):
            user_bl.create_user_bl(self.valid_json)


if __name__ == '__main__':
    unittest.main()