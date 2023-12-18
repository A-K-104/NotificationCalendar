import unittest
from base64 import b64encode
from unittest.mock import patch

from Domain.Init.db_init import create_db
from EntryPoint.Config import config_base
from app import create


def convert_response_to_event_dto(second_response):
    # Convert the response to a dictionary matching the format of valid_event
    response_data = {
        'title': second_response.json['title'],
        'date': second_response.json['date']
    }
    return response_data


def get_base_auth_header(username: str, password: str):
    # Create a basic auth header with given username and password
    return {"Authorization": "Basic " + b64encode(f"{username}:{password}".encode()).decode()}


@patch.object(config_base, "db_table", "NotificationDBTest")
class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Setup initial test data and mock configurations
        self.admin_user = {"username": "user", "role": "ADMIN"}
        self.non_admin_user = {"username": "user2", "role": "USER"}
        self.valid_event = {'title': 'The 404 party', 'date': 'Wed, 20 Feb 1991 00:00:00 GMT'}
        self.valid_update_event = {'title': 'The after 404 party', 'date': 'Wed, 20 Feb 1991 00:00:00 GMT'}

        # with patch.object(config_base, "db_table", "NotificationDBTest"):
        create_db()
        self.app = create()
        self.client = self.app.test_client()
        self.create_user_if_empty()

    def create_user_if_empty(self):
        # Create users if they don't already exist
        self.client.post("/api/v1/user/", json=self.admin_user)
        self.client.post("/api/v1/user/", json=self.non_admin_user)

    def tearDown(self):
        # TODO: Implement database cleanup logic
        pass

    def test_create_and_update_retrieve_event_successfully(self):
        # Test creating, updating, and retrieving an event with admin user
        user_name = self.admin_user['username']

        element_id = self.get_create_event_id(user_name)
        self.validate_event(element_id, self.valid_event)

        self.update_event(user_name, element_id)
        self.validate_event(element_id, self.valid_update_event)

        self.delete_event(user_name, element_id)

    def test_create_and_event_not_authorized(self):
        # Test creating an event with a non-admin user should be unauthorized
        user_name = self.non_admin_user['username']
        self.perform_request('post', f"/api/v1/event/", self.valid_event, user_name, 401)

    def test_update_event_not_authorized(self):
        # Test updating an event with a non-admin user should be unauthorized

        user_name = self.non_admin_user['username']
        self.perform_request('put', f"/api/v1/event/1", self.valid_event, user_name, 401)

    def test_delete_event_not_authorized(self):
        # Test delete an event with a non-admin user should be unauthorized
        user_name = self.non_admin_user['username']
        self.perform_request('delete', f"/api/v1/event/1", self.valid_event, user_name, 401)


    def delete_event(self, user_name, element_id):
        self.perform_request('delete', f"/api/v1/event/{element_id}", self.valid_update_event, user_name)

    def update_event(self, user_name, element_id):
        self.perform_request('put', f"/api/v1/event/{element_id}", self.valid_update_event, user_name)

    def validate_event(self, element_id, valid_event):
        get_response = self.perform_request('get', f"/api/v1/event/{element_id}", self.valid_update_event)

        response_data = convert_response_to_event_dto(get_response)
        self.assertEqual(response_data, valid_event)

    def get_create_event_id(self, user_name):
        post_response = self.perform_request('post', f"/api/v1/event/", self.valid_event, user_name)
        element_id = post_response.json.get('element_id')
        self.assertIsNotNone(element_id, "Element ID not returned in response")
        return element_id

    def perform_request(self, method, url, data=None, username=None, expected_status=200):
        auth_header = get_base_auth_header(username if username else self.admin_user['username'], "")
        response = getattr(self.client, method)(url, json=data, headers=auth_header)
        self.assertEqual(expected_status, response.status_code)
        return response


if __name__ == '__main__':
    unittest.main()
