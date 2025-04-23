'''def testLogin():
    print("login sucessfull")

def testLogoff():
    print("logoff sucessfull")

def testCalculation():
    assert 2+2==4'''

'''import pytest


def square(x):
    return x * x


@pytest.mark.parametrize("actual, expected", [
    (2, 4),
    (3, 9),
    (4, 16)
    ])
def test_square(actual, expected):
    assert square(actual) == expected'''

import pytest

'''def divide(a, b):
    return a / b


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)'''


@pytest.fixture()
def setUp():
    print("Launch the Browser")
    print("Login")
    print("Browse the products")
    yield
    print("Logout")
    print("Close the browser")


def test_add_product(setUp):
    print("Product has been added to cart")


def test_remove_product(setUp):
    print("Product has been removed from cart")
