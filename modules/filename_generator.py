import string
import random

def generate_random_filename():
    letters = string.ascii_lowercase
    return(''.join(random.choice(letters) for i in range(16)) + '.wav')
