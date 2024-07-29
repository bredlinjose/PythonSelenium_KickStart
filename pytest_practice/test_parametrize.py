import pytest

@pytest.mark.parametrize("username, age", [("Bredlin", 27), ("Jose", 25), ("Dev", 23)])
def test_sample_six(username, age):
    print(f"My name is {username}.", f"I am {age} years old.")
