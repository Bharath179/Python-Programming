from dataclasses import dataclass


@dataclass
class EmployeeAddress:
    street: str
    city: str
    state: str
    pincode: int


@dataclass
class NestedJsonObj:
    firstname: str
    lastname: str
    gender: str
    age: int
    salary: float
    address: EmployeeAddress
