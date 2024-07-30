import pytest

@pytest.fixture(autouse=True, scope="function")
def setup_and_teardown():
    print("Launch the browser")
    print("Open the application")
    yield
    print("Logout from the application")
    print("Close the browser")
