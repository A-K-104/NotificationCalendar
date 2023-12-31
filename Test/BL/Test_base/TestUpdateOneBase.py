import unittest
from unittest.mock import Mock, patch

from flask import Flask

from Common.Exceptions.ContentException import ContentException


class TestUpdateOneBase(unittest.TestCase):
    __test__ = False

    def setUp(self):
        self.app = Flask(__name__)
        self.element_bl = None
        self.update_id = None
        self.valid_json = None
        self.model_name = None

    def test_update_one_should_success(self):
        # Arrange
        request = Mock()
        request.is_json = True
        request.json = self.valid_json

        return_value = Mock()
        return_value.to_dict.return_value = self.valid_json
        with patch(f'Model.{self.model_name}.update_one', return_value=return_value):
            with self.app.app_context():
                # Act
                response = self.element_bl.update_one(request, self.update_id)

                # Assert
                self.assertEqual(response.json, self.valid_json)

    def test_update_one_should_Content_exception(self):
        # Arrange
        request = Mock()
        request.is_json = False  # set to false to trigger ContentException

        # Act & Assert
        with self.assertRaises(ContentException):
            self.element_bl.update_one(request, self.update_id)
