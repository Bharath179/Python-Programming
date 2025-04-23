import requests
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError


def load_schema_from_file(schema_file):
    with open(schema_file, 'r') as f:
        return json.load(f)


def test_json_schema_validation():

    # 1. Make the API GET request
    response = requests.get("http://localhost:3000/store")
    assert response.status_code == 200

    # 2. Load response body and schema
    response_json = response.json()

    # Print the JSON response body
    print("JSON Response Body:")
    print(json.dumps(response_json, indent=4))

    schema = load_schema_from_file("jsonschema.json")

    try:
        # 3. Validate response against the schema
        validate(instance=response_json, schema=schema)
        print("JSON schema validation passed.")
    except ValidationError as e:
        print("JSON schema validation failed!")
        print("Error:", e.message)
        assert False


def test_get_total_books_price():
    response = requests.get("http://localhost:3000/store")
    assert response.status_code == 200

    response_json = response.json()
    books = response_json.get("books", [])

    total_price = 0.0
    for book in books:
        total_price += book.get("price", 0.0)

    print("Total Price of All Books:", total_price)

    # Optional assertion to make sure total is not 0
    assert total_price > 0
