from unittest.mock import patch
import unittest

from BL import venue_bl
from Common.Exceptions.NotFoundException import NotFoundException


class TestDeleteVenue(unittest.TestCase):

    def setUp(self):
        self.valid_response = "Venue deleted"

    @patch('Models.venue_model.delete_venue_by_id')
    def test_delete_venue_success(self, mock_delete_venue):
        mock_delete_venue.return_value = True
        response = venue_bl.delete_venue_bl(1)
        self.assertEqual(response, self.valid_response)

    @patch('Models.venue_model.delete_venue_by_id')
    def test_delete_venue_wrong_id(self, mock_delete_venue):
        mock_delete_venue.return_value = False
        with self.assertRaises(NotFoundException):
            venue_bl.delete_venue_bl(1)


if __name__ == '__main__':
    unittest.main()
