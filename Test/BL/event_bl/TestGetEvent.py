import datetime
import unittest
from unittest.mock import patch, Mock

from flask import Flask

from BL.EventBL import EventBL
from Common.DTOs.UserDTO import UserDTO
from Common.Exceptions.MissingArgumentsException import MissingArgumentsException
from Test.BL.Test_base.TestCreateOneBase import TestCreateOneBase


class TestGetEvent(unittest.TestCase):

    def setUp(self):
        self.element_bl = EventBL()
        self.args = {"location": "TLV"}

    def test_get_filter_by_location_should_success(self):
        # Arrange
        request = Mock()
        request.args = self.args

        with patch(f'BL.EventBL.EventBL.filter_by_location', return_value=True):
            # Act
            response = self.element_bl.filter_by_location(request)

            # Assert
            self.assertEqual(response, True)

    def test_get_filter_by_location_should_missing_args(self):
        # Arrange
        request = Mock()
        request.args = {}

        # Act & Assert
        with self.assertRaises(MissingArgumentsException):
            self.element_bl.filter_by_location(request)


if __name__ == '__main__':
    unittest.main()
