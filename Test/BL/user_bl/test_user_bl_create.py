from unittest.mock import patch
import unittest

from flask import Flask

from BL import user_bl
from Common.Exceptions.MissingValueException import MissingValueException
from Common.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Common.Exceptions.NotInEnumException import NotInEnumException


class TestCreateUser(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.valid_json = {'username': 'c0ff33', 'role': 'ADMIN'}
        self.wrong_role = {'username': 'grot', 'role': 'GROOT'}

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

    def test_create_user_with_wrong_roll_exception(self):
        with self.assertRaises(NotInEnumException):
            user_bl.create_user_bl(self.wrong_role)


if __name__ == '__main__':
    unittest.main()
