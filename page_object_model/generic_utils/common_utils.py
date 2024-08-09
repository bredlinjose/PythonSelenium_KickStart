import random
import string


def random_string(length):
    result = ''.join((random.choice(string.ascii_lowercase) for x in range(length)))
    return result

def random_number(length):
    result = int(''.join(str(random.randint(0, 9)) for _ in range(length)))
    return result

def random_email(domain):
    letters = random_string(5)
    numbers = str(random_number(3))
    return letters + numbers + domain
