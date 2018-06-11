import json

import requests

from conftest import fake


class TestPost:

    special_characaters = "@#$%^&*()!`~{},./[]\|:<>?"

    def validate_field(self, data, post_url, get_url):
        """
        Utility function to test for failure if one or more filed are missing
        or has incorrect data typein post
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """
        get_response = requests.get(get_url)
        length = len(get_response.json())

        assert get_response.status_code == 200

        response = requests.post(url=post_url, json=data)

        assert response.status_code == 400

        get_response = requests.get(get_url)
        new_length = len(get_response.json())

        assert get_response.status_code == 200
        assert new_length == length

    def test_post_success(self, data, post_url, get_url):
        """
        This fucntion tests the following scenarios:
        - Gets the initial length of the available user data in the database
        - Makes a post request with the post data to enter a new user
        - Gets the new length of the user database list by making a get request after
        making a post request
        - Checks if the post is successful that the new length of the user database list
        increases by one
        - Also checks if then new list contains the new user's data
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        get_response = requests.get(get_url)
        length = len(get_response.json())

        assert get_response.status_code == 200

        post_response = requests.post(url=post_url, json=data)

        assert post_response.status_code == 201

        post_response_data = post_response.json()

        assert post_response.status_code == 200
        assert post_response_data.get("username") == data.get("username")
        assert post_response_data.get("first_name") == data.get("first_name")
        assert post_response_data.get("last_name") == data.get("last_name")
        assert post_response_data.get("email") == data.get("email")
        assert post_response_data.get("department") == data.get("department")
        # assert post_response_data.get("age") == data.get("age")
        assert post_response_data.get("salary") == data.get("salary")

        get_response = requests.get(get_url)
        new_length = len(get_response.json())

        assert get_response.status_code == 200
        assert new_length == length + 1

        get_response_data = get_response.json()

        flag = False
        # Converting age to string since age in the response payload is in string.
        # This check fails for different age datatype even if the data payload
        # exists in the response payload if there is a mis match in datatype
        data["age"] = str(data["age"])
        if data in get_response_data:
            flag = True

        assert flag

    def test_post_without_username(self, data, post_url, get_url):
        """
        test post without username
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        del data["username"]

        self.validate_field(data, post_url, get_url)

    def test_post_without_first_name(self, data, post_url, get_url):
        """
        test post without first_name
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        del data["first_name"]

        self.validate_field(data, post_url, get_url)

    def test_post_without_last_name(self, data, post_url, get_url):
        """
        test post without last_name
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        del data["last_name"]

        self.validate_field(data, post_url, get_url)

    def test_post_without_email(self, data, post_url, get_url):
        """
        test post without email
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        del data["email"]

        self.validate_field(data, post_url, get_url)

    def test_post_without_department(self, data, post_url, get_url):
        """
        test post without department
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        del data["department"]

        self.validate_field(data, post_url, get_url)

    def test_post_without_age(self, data, post_url, get_url):
        """
        test post without age
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        del data["age"]

        self.validate_field(data, post_url, get_url)

    def test_post_without_salary(self, data, post_url, get_url):
        """
        test post without salary
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        del data["salary"]

        self.validate_field(data, post_url, get_url)

    def test_post_improper_username_field_type(self, data, post_url, get_url):
        """
        test by replacing username with a bunch of integer numbers
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["username"] = 5000
        self.validate_field(data, post_url, get_url)

    def test_post_improper_first_name_field_type(self, data, post_url, get_url):
        """
        test by replacing first_name with a bunch of integer numbers
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["first_name"] = 5000
        self.validate_field(data, post_url, get_url)

    def test_post_improper_last_name_field_type(self, data, post_url, get_url):
        """
        test by replacing last_name with a bunch of integer numbers
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["last_name"] = 5000
        self.validate_field(data, post_url, get_url)

    def test_post_improper_email_field_type(self, data, post_url, get_url):
        """
        test by replacing last_name with a bunch of integer numbers
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["email"] = 5000
        self.validate_field(data, post_url, get_url)

    def test_post_improper_department_field_type(self, data, post_url, get_url):
        """
        test by replacing last_name with a bunch of integer numbers
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["department"] = 5000
        self.validate_field(data, post_url, get_url)

    def test_post_improper_age_field_type(self, data, post_url, get_url):
        """
        test by replacing age with a string
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["age"] = fake.word()
        self.validate_field(data, post_url, get_url)

    def test_post_improper_salary_field_type(self, data, post_url, get_url):
        """
        test by replacing age with a string
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["salary"] = fake.word()
        self.validate_field(data, post_url, get_url)

    def test_negative_age_value(self, data, post_url, get_url):
        """
        test putting negative values in age
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["age"] = -10
        self.validate_field(data, post_url, get_url)

    def test_negative_salary_value(self, data, post_url, get_url):
        """
        test putting negative values in age
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["salary"] = -10
        self.validate_field(data, post_url, get_url)

    def test_special_characters_in_first_name(self, data, post_url, get_url):
        """
        test putting special characters in first name
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["first_name"] = self.special_characaters
        self.validate_field(data, post_url, get_url)

    def test_special_characters_in_last_name(self, data, post_url, get_url):
        """
        test putting special characters in last name
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["last_name"] = self.special_characaters
        self.validate_field(data, post_url, get_url)

    def test_special_characters_in_username(self, data, post_url, get_url):
        """
        test putting special characters in username
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["username"] = self.special_characaters
        self.validate_field(data, post_url, get_url)

    def test_special_characters_in_email(self, data, post_url, get_url):
        """
        test putting special characters in email
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["email"] = self.special_characaters
        self.validate_field(data, post_url, get_url)

    def test_special_characters_in_department(self, data, post_url, get_url):
        """
        test putting special characters in department
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["department"] = self.special_characaters
        self.validate_field(data, post_url, get_url)

    def test_special_characters_in_age(self, data, post_url, get_url):
        """
        test putting special characters in username
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["age"] = self.special_characaters
        self.validate_field(data, post_url, get_url)

    def test_special_characters_in_salary(self, data, post_url, get_url):
        """
        test putting special characters in username
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["salary"] = self.special_characaters
        self.validate_field(data, post_url, get_url)

    def test_high_age_value(self, data, post_url, get_url):
        """
        test putting high values in age
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["age"] = 100000
        self.validate_field(data, post_url, get_url)

    def test_hogh_salary_value(self, data, post_url, get_url):
        """
        test putting high values in age
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """

        data["salary"] = 1000000000000000
        self.validate_field(data, post_url, get_url)


class TestPostUnique:

    def test_unique_email(self, data, post_url, get_url):
        """
        Test by creating two users with the same email in their profile.
        Should fail since two users cannot have the same email for two different
        profiles.
        :param data: 
        :param post_url: 
        :param get_url: 
        :return: 
        """
        get_response = requests.get(get_url)
        length = len(get_response.json())

        assert get_response.status_code == 200

        response = requests.post(url=post_url, json=data)

        assert response.status_code == 200

        get_response = requests.get(get_url)
        new_length = len(get_response.json())

        assert get_response.status_code == 200
        assert new_length == length + 1

        response = requests.post(url=post_url, json=data)

        assert response.status_code == 400

        get_response = requests.get(get_url)
        new_length2 = len(get_response.json())

        assert get_response.status_code == 200
        assert new_length2 == new_length + 1
