from dataclasses import dataclass
from typing import List
import json


@dataclass
class Student:
    name: str
    location: str
    phone: str
    courses: List[str]


def serialize_student():

    # Create student object
    student = Student(
        name="Bharath",
        location="India",
        phone="1234567890",
        courses=["Python", "API Testing"]
    )

    # Convert to JSON string
    json_data = json.dumps(student.__dict__, indent=4)
    print("Serialized JSON:")
    print(json_data)

    # Optional: Save to file
    with open("student.json", "w") as f:
        json.dump(student.__dict__, f, indent=4)


# Run the function
if __name__ == "__main__":
    serialize_student()
