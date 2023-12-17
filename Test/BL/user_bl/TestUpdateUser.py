import unittest
from unittest.mock import Mock

from BL.UserBL import UserBL
from Common.Exceptions.NotInEnumException import NotInEnumException
from Test.BL.Test_base.TestUpdateOneBase import TestUpdateOneBase


class TestUpdateUser(TestUpdateOneBase):
    __test__ = True

    def setUp(self):
        super().setUp()
        self.element_bl = UserBL()
        self.update_id = 1
        self.valid_json = {'username': 'c0ff33', 'role': 'ADMIN'}
        self.wrong_role = {'username': 'grot', 'role': 'GROOT'}
        self.model_name = 'UserModel.UserModel'

    def test_update_one_should_enum_exception(self):
        # Arrange
        request = Mock()
        request.is_json = True
        request.json = self.wrong_role

        # Act & Assert
        with self.assertRaises(NotInEnumException):
            self.element_bl.update_one(request, self.update_id)


if __name__ == '__main__':
    unittest.main()
