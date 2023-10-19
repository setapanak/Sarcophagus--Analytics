import requests
import random
import string

# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1" #will be changed to the appropriate api endpoint this is just an example

# A GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON data from the response
    api_data = response.json()

    # Extract the desired information from the API response
    title = api_data['title']
    body = api_data['body']

    # Generate a random password
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

        value = random.randint(4, 8)
        # generate random int String size

        # generate other characters
        for _i in range(value):
            password += random.choice(random_source)

        password_list = list(password)
        # shuffle all characters
        random.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)
        return password

    # Call the function to generate a random password
    random_password = get_random_password()

    # Print the API data and random password
    print("API Title:", title)
    print("API Body:", body)
    print("Random Password:", random_password)

else:
    print("Failed to retrieve data from the API. Status code:", response.status_code)
