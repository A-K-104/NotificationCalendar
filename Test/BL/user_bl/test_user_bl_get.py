from unittest.mock import patch
import unittest

from flask import Flask

from BL import user_bl
from Common.Exceptions.NotFoundException import NotFoundException


class TestGetUser(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.valid_json = {'username': 'c0ff33', 'role': 'admin'}

    @patch('Models.user_model.get_user_by_id')
    def test_get_user_success(self, mock_get_user):
        with self.app.app_context():
            mock_get_user.return_value = self.valid_json
            response = user_bl.get_user_bl(1)
            self.assertEqual(response.json, self.valid_json)

    @patch('Models.user_model.get_user_by_id')
    def test_get_user_wrong_id(self, mock_get_user):
        mock_get_user.return_value = None
        with self.assertRaises(NotFoundException):
            user_bl.get_user_bl(1)


if __name__ == '__main__':
    unittest.main()
