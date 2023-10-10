import random
import string
from random import randint


def get_random_password():
    random_source = string.ascii_letters + string.digits + string.punctuation
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)
    # select 1 special symbol
    password += random.choice(string.punctuation)

    value = randint(4, 8)
    #generate random int String size

    # generate other characters
    for _i in range(value):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password


print("Password:", get_random_password())
