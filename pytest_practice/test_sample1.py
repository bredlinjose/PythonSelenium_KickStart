import pytest

@pytest.mark.regression
def test_sample_four():
    print("Inside sample four")

@pytest.mark.smoke
def test_sample_five():
    print("Inside sample five")

