from random import randint

import pytest

from faker import Faker

fake = Faker()


# Using urls as fixtures since we will need the same url in different parts of tests
# Fixtures discovered automatically so no need to explicitly import
@pytest.fixture
def get_url():
    return "http://128.199.158.232:8002/employees"


@pytest.fixture
def post_url():
    return "http://128.199.158.232:8002/employees"


@pytest.fixture
def id_url():

    def url(id):
        return f"http://128.199.158.232:8002/employees/{id}"

    return url


@pytest.fixture
def data():
    post_data = {
        "username": fake.name(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "department": fake.job(),
        "age": randint(20, 70),
        "salary": randint(1000, 10000)
    }

    return post_data
