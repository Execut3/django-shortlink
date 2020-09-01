import string
import random


def random_string(string_len=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_len))


def generate_random_str(num=4):
    return ''.join(random.SystemRandom().choice(
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits
    ) for _ in range(num))
