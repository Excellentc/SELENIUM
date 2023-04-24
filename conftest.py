import pytest


@pytest.fixture(scope="function", autouse=True)
def function_fix():
    print("\nFUNCTION SETUP ")
    yield
    print("\nFUNCTION TEARDOWN ")
