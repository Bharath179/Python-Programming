import pytest


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def headers():
    return {
        "Authorization": "Bearer faketoken123",
        "Content-Type": "application/json"
    }
