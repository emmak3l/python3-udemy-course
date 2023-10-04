# Writing Your First Python Request

# Using the requests Module
# - lets us make HTTP requests from our python code!
# - installed using pip

import requests
url = "http://www.google.com"
response = requests.get(url)

print(f"your request to {url} came back with status code {response.status_code}") # your request to http://www.google.com came back with status code 200

