from unittest.mock import patch
import unittest

from flask import Flask

from BL import user_bl
from Common.Exceptions.NameAlreadyUsedException import NameAlreadyUsedException
from Common.Exceptions.NotFoundException import NotFoundException
from Common.Exceptions.NotInEnumException import NotInEnumException


class TestUpdateUser(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.valid_json = {'username': 'c0ff33', 'role': 'ADMIN'}
        self.wrong_role = {'username': 'grot', 'role': 'GROOT'}

    @patch('Models.user_model.update_user_by_id')
    def test_update_user_success(self, mock_update_user):
        with self.app.app_context():
            mock_update_user.return_value = self.valid_json
            response = user_bl.update_user_bl(1, self.valid_json)
            self.assertEqual(response.json, self.valid_json)

    @patch('Models.user_model.update_user_by_id')
    def test_update_user_missing_arguments(self, mock_update_user):
        mock_update_user.return_value = None
        with self.assertRaises(NotFoundException):
            user_bl.update_user_bl(1, self.valid_json)

    @patch('Models.user_model.update_user_by_id')
    def test_update_user_duplicate_key_exception(self, mock_update_user):
        mock_update_user.side_effect = Exception("duplicate key value")
        with self.assertRaises(NameAlreadyUsedException):
            user_bl.update_user_bl(1, self.valid_json)

    def test_update_user_with_wrong_roll_exception(self):
        with self.assertRaises(NotInEnumException):
            user_bl.create_user_bl(self.wrong_role)


if __name__ == '__main__':
    unittest.main()
