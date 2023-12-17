import unittest
from unittest.mock import Mock

from BL.UserBL import UserBL
from Common.Exceptions.NotInEnumException import NotInEnumException
from Test.BL.Test_base.TestCreateOneBase import TestCreateOneBase


class TestCreateUser(TestCreateOneBase):
    __test__ = True

    def setUp(self):
        super().setUp()
        self.element_bl = UserBL()
        self.valid_json = {'username': 'c0ff33', 'role': 'ADMIN'}
        self.wrong_role = {'username': 'grot', 'role': 'GROOT'}
        self.model_name = 'UserModel.UserModel'

    def test_create_one_should_enum_exception(self):
        # Arrange
        request = Mock()
        request.is_json = True
        request.json = self.wrong_role

        # Act & Assert
        with self.assertRaises(NotInEnumException):
            self.element_bl.create_one(request)


if __name__ == '__main__':
    unittest.main()
