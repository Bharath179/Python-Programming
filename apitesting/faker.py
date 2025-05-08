import pytest
import requests
from faker import Faker

fake = Faker()


def generate_random_post():
    return {
        "title": fake.sentence(nb_words=5),
        "body": fake.paragraph(),
        "userId": fake.random_int(min=1, max=10)
    }


# Run 3 random test cases
@pytest.mark.parametrize("i", range(3))
def test_create_random_post(i):
    payload = generate_random_post()
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]
    print("Response Body:", response.json())
