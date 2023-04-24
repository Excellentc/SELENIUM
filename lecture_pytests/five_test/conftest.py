import pytest


@pytest.fixture(scope="session", autouse=True)
def session_fix():
    print("\nSESSION SETUP ")
    yield
    print("\nSESSION TEARDOWN ")
