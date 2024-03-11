from django.test import TestCase
import os
from dotenv import load_dotenv
load_dotenv()

# Create your tests here.
import random
import string

def generate_short_alias():
    characters = string.ascii_letters + string.digits
    print(characters)
    return ''.join(random.choice(characters) for _ in range(6))

# print(generate_short_alias())
# print(string)

# var = os.getenv('EMAIL_HOST_USER')
# print(var)