import unittest
from unittest.mock import Mock, patch

from flask import Flask

from Common.Exceptions.ContentException import ContentException
from Common.Exceptions.NotFoundException import NotFoundException


class TestCreateOneBase(unittest.TestCase):
    __test__ = False

    def setUp(self):
        self.app = Flask(__name__)
        self.element_bl = None
        self.valid_json = None
        self.model_name = None
        self.additional_data = []

    def test_create_one_should_success(self):
        # Arrange
        request = Mock()
        request.is_json = True
        request.json = self.valid_json

        return_value = Mock()
        return_value.to_dict.return_value = self.valid_json
        with patch(f'Model.{self.model_name}.create_one', return_value=return_value):
            with self.app.app_context():
                # Act
                response = self.element_bl.create_one(request, *self.additional_data)

                # Assert
                self.assertEqual(response.json, self.valid_json)

    def test_create_one_should_not_found(self):
        # Arrange
        request = Mock()
        request.is_json = True
        request.json = {}  # Empty json to trigger NotFoundException

        # Act & Assert
        with self.assertRaises(NotFoundException):
            self.element_bl.create_one(request, *self.additional_data)

    def test_create_one_should_Content_exception(self):
        # Arrange
        request = Mock()
        request.is_json = False  # set to false to trigger ContentException

        # Act & Assert
        with self.assertRaises(ContentException):
            self.element_bl.create_one(request, *self.additional_data)
