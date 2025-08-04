import requests
import json
from jsonschema import validate


def test_get_user_schema_validation():
    # 1. API URL
    url = "https://reqres.in/api/users/2"

    # 2. Send GET request
    response = requests.get(url)

    # 3. Assert status code
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    # 4. Load schema
    with open("C:\\Users\\Lenovo\\Documents\\json_file.json", "r") as f:
        schema = json.load(f)

    # 5. Get response JSON
    response_json = response.json()
    print("Response JSON is:", response_json)

    # 6. Validate JSON using schema
    validate(instance=response_json, schema=schema)
