# Requesting JSON with Python

import requests
url = "https://icanhazdadjoke.com/"

# We can get the header in plain text like this: (note that not all websites can do this, but this one is set up so you can)
# response = requests.get(url, headers={"Accept": "text/plain"})

# print(response.text) # random generated dad joke like: How does Darth Vader like his toast? On the dark side.


# We can also get JSON data instead of just the header like this

res = requests.get(url, headers={"Accept": "application/json"})

print(res.text) # this looks like a python dictionary but when you check it's type it's actually a string
print(res.json()) # this .json() method converts the json to a python dictionary

data = res.json() # data is now a python dictionary containing the json data

print(data["joke"]) # now we can access the key value pairs