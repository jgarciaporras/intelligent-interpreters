# This module contains functions that generates a random string that can be used to create a filename
import string
import random

def generate_filename():
    letters = string.ascii_lowercase
    return(''.join(random.choice(letters) for i in range(16)))
