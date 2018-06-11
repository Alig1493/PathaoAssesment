import requests
import re

from utils import verify_email


class TestGet:

    def test_get_users(self, get_url):
        """
        Testing the success scenario for getting a list of users
        Since there is a possibility for the list of users to be empty,
        we are checking if the list of data contains any values and if they are,
        each payload in the list contains values all the required fields.
        :return: 
        """

        response = requests.get(url=get_url)

        data = response.json()

        assert response.status_code == 200
        assert isinstance(data, list)

    def test_validate_get_data_values(self, get_url):
        """
        Testing if all the fields in the response payload list
        contains values in them
        :param get_url: 
        :return: 
        """
        response = requests.get(url=get_url)

        data = response.json()

        assert response.status_code == 200
        assert isinstance(data, list)

        if data:
            for item in data:
                assert item.get("username", "")
                assert item.get("first_name", "")
                assert item.get("last_name", "")
                assert item.get("email", "")
                assert item.get("department", "")
                assert item.get("age", "")
                assert item.get("salary", "")

    def test_validate_get_data_value_types(self, get_url):
        """
        Checking the datatype of the fields in the returning payload list. 
        :param get_url: 
        :return: 
        """
        response = requests.get(url=get_url)

        data = response.json()

        assert response.status_code == 200
        assert isinstance(data, list)

        if data:
            for item in data:
                assert isinstance(item.get("username", ""), str)
                assert isinstance(item.get("first_name", ""), str)
                assert isinstance(item.get("last_name", ""), str)
                assert isinstance(item.get("email", ""), str)
                assert verify_email(email=item.get("email", ""))
                assert isinstance(item.get("department", ""), str)

                # age should be integer
                assert not isinstance(item.get("age", ""), int)
                # salary can be either an integer or float
                assert isinstance(item.get("salary", ""), int) or isinstance(item.get("salary", ""), float)
