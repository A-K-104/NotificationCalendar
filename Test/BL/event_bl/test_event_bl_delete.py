from unittest.mock import patch
import unittest

from BL import event_bl
from Common.Exceptions.NotFoundException import NotFoundException


class TestDeleteEvent(unittest.TestCase):

    def setUp(self):
        self.valid_response = "Event was deleted"


    @patch('Models.event_model.delete_event_by_id')
    def test_delete_event_success(self, mock_delete_event):
        mock_delete_event.return_value = True
        response = event_bl.delete_event_bl(1)
        self.assertEqual(response, self.valid_response)

    @patch('Models.event_model.delete_event_by_id')
    def test_delete_event_wrong_id(self, mock_delete_event):
        mock_delete_event.return_value = False
        with self.assertRaises(NotFoundException):
            event_bl.delete_event_bl(1)


if __name__ == '__main__':
    unittest.main()
