import csv
import pytest
import requests


# Load CSV data from file
def load_csv_data(filepath):
    with open(filepath, "r") as f:
        return list(csv.DictReader(f))


# Parametrized API test using the data
test_data = load_csv_data("D://New folder (1)//data1.csv")


@pytest.mark.parametrize("payload", test_data)
def test_create_post_csv(payload):
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201
    print("Response Body:", response.json())
