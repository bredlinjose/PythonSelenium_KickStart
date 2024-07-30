# function name must be same as mentioned here

def setup_module(module):  # first
    print("Open browser")

def teardown_module(module):  # last
    print("Close browser")

def setup_function(function):  # before each test
    print("Open application")

def teardown_function(function):  # after each test
    print("Close application")

def test_login_with_valid_credentials():
    print("Login with the valid username and password")

def test_login_with_invalid_credentials():
    print("Login with the invalid username and password")

def test_search_for_valid_product():
    print("Searching valid products")

def test_search_for_invalid_product():
    print("Searching invalid products")
