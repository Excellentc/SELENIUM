import pytest


@pytest.fixture(scope="function", autouse=False)
def function_fix():
    print("\nFUNCTION SETUP ")
    yield
    print("\nFUNCTION TEARDOWN ")
