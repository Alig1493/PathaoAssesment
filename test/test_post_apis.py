import json

import requests


class TestPost:

    def test_post_success(self, data, post_url):

        response = requests.post(url=post_url, json=data)

        assert response.status_code == 201

    def test_post_validate_request_response_data(self, data, post_url):

        response = requests.post(url=post_url, json=data)

        response_data = response.json()

        assert response.status_code == 201
        assert response_data.get("username") == data.get("username")
        assert response_data.get("first_name") == data.get("first_name")
        assert response_data.get("last_name") == data.get("last_name")
        assert response_data.get("email") == data.get("email")
        assert response_data.get("department") == data.get("department")
        assert response_data.get("age") == data.get("age")
        assert response_data.get("salary") == data.get("salary")
