import string
import random

def random_string(length, upper=True, lower=True, digit=True, symbol=True):
    chars = ''
    if upper:
        chars += string.ascii_uppercase
    if lower:
        chars += string.ascii_lowercase
    if digit:
        chars += string.digits
    if symbol:
        chars += string.punctuation

    if len(chars) == 0:
        raise ValueException("You must enable at least one kind of character")

    return ''.join(random.SystemRandom().choice(chars) for _ in range(length));
