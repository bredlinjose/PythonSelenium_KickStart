
def test_sample_one():
    print("Inside sample one")
    a = 5
    b = 10
    assert a > b, str(a) + " is not greater than " + str(b)
    print("This is a print statement")  # it won't print

def test_sample_two():
    print("Inside sample two")
    a = 10
    b = 10
    assert a == b, str(a) + " is equal " + str(b)

def test_sample_three():
    print("Inside sample three")
    a = 'Bredlin'
    b = 'Bredline'
    assert a.__eq__(b), a + " is not equal to " + b
