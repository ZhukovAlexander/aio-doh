import string
import random

UNRESERVED_CHARS = string.ascii_letters + string.digits + '-._~'


def random_padding():
    return ''.join(random.choice(UNRESERVED_CHARS) for _ in range(random.randint(10, 50)))
