import pytest

"""@pytest.fixture()
def setup():
    print("Once before every method")

def test_method1(setup):
    print("This is method1")

def test_method2(setup):
    print("This is method2")"""

@pytest.fixture()
def setup():
    print("Once before every method")
    yield
    print("Once After every method")

def test_method1(setup):
    print("This is method1")

def test_method2(setup):
    print("This is method2")