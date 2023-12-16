from unittest.mock import patch
import unittest

from BL import user_bl
from Common.Exceptions.NotFoundException import NotFoundException


class TestDeleteUser(unittest.TestCase):

    def setUp(self):
        self.valid_response = "User deleted"

    @patch('Models.user_model.delete_user_by_id')
    def test_delete_user_success(self, mock_delete_user):
        mock_delete_user.return_value = True
        response = user_bl.delete_user_bl(1)
        self.assertEqual(response, self.valid_response)

    @patch('Models.user_model.delete_user_by_id')
    def test_delete_user_wrong_id(self, mock_delete_user):
        mock_delete_user.return_value = False
        with self.assertRaises(NotFoundException):
            user_bl.delete_user_bl(1)


if __name__ == '__main__':
    unittest.main()
