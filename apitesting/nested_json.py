import requests
import json
from apitesting.models import NestedJsonObj, EmployeeAddress
from dataclasses import asdict


def test_create_user():
    # Create address object
    emp2 = EmployeeAddress(
        street="patel layout",
        city="Begur",
        state="Bangalore",
        pincode=560068
    )

    # Create main employee object with address
    emp1 = NestedJsonObj(
        firstname="Bharath",
        lastname="Kumar",
        gender="Male",
        age=27,
        salary=25000.45,
        address=emp2
    )

    # Convert to JSON
    json_payload = json.dumps(asdict(emp1), indent=4)

    # Make POST request
    url = "http://httpbin.org/post"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json_payload)

    # Print result
    print(response.status_code)
    print(response.json())
