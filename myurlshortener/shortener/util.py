import random
import string
from .models import Url

def generate_random_chars():
    characters = string.ascii_letters + string.digits
    randomstr = ''.join(random.choice(characters) for _ in range(6))
    urlExists = Url.objects.filter(shortened_link=randomstr).exists()
    if not urlExists:
        return randomstr
    return generate_random_chars()