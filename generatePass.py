import requests

# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"
#url = "file:///C:/Users/setap/Desktop/Software%20Design/test/test.html"

# A GET request to the API
response = requests.get(url)
import random
import string
from random import randint
import secrets

def get_random_password():
    random_source = string.ascii_letters + string.digits + '-_@<>)(&^%$=+}{][|?`!'
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)
    # select 1 special symbol
    password += random.choice('-_@<>)(&^%$=+}{][|?`!')

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


#print("Password:", get_random_password())

# Print the response
response_json = get_random_password();
print(response_json)
