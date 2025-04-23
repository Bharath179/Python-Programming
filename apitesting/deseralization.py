from dataclasses import dataclass
from typing import List
import json


@dataclass
class Student:
    name: str
    location: str
    phone: str
    courses: List[str]


def deserialize_student():

    # Load JSON from file
    with open("student.json", "r") as f:
        data = json.load(f)

    # Convert to Student object
    student = Student(**data)

    # Print fields
    print("Deserialized Student Object:")
    print("Name:", student.name)
    print("Location:", student.location)
    print("Phone:", student.phone)
    print("Courses:", ", ".join(student.courses))


# Run the function
if __name__ == "__main__":
    deserialize_student()
