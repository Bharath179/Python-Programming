import json
import pytest
import requests


# Load JSON data from file
def load_json_data(filepath):
    with open(filepath, "r") as f:
        return json.load(f)


# Load test data
test_data = load_json_data("D://New folder (1)//data.json")


# Parametrized API test using the data
@pytest.mark.parametrize("payload", test_data)
def test_create_post(payload):
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    print("Response Body:", response.json())

    # Basic response check
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"

    # Validate response content
    response_json = response.json()
    assert response_json["title"] == payload["title"], "Title mismatch"
    assert "id" in response_json, "Missing ID in response"
