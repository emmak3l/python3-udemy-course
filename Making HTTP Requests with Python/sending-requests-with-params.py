# Sending Requests with Params

# What's a Query String?

# A way to pass data to the server as part of a GET request
# http://www.example.com/?key1=value1&key2=value2

import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": "cat"}
)

data = response.json()

print(data["results"])

# [{'id': 'daaUfibh', 'joke': 'Why was the big cat disqualified from the race? Because it was a cheetah.'}, {'id': 'iGJeVKmWDlb', 'joke': 'My cat was just sick on the carpet, I don’t think it’s feline well.'}, {'id': '8UnrHe2T0g', 'joke': '‘Put the cat out’ … ‘I didn’t realize it was on fire'}, {'id': '39Etc2orc', 'joke': 'Why did the man run around his bed? Because he was trying to catch up on his sleep!'}, {'id': 'BQfaxsHBsrc', 'joke': 'What do you call a pile of cats?  A Meowtain.'}, {'id': '1wkqrcNCljb', 'joke': "Did you know that protons have mass? I didn't even know they were catholic."}, {'id': 'AQn3wPKeqrc', 'joke': 'It was raining cats and dogs the other day. I almost stepped in a poodle.'}, {'id': 'O7haxA5Tfxc', 'joke': 'Where do cats write notes?\r\nScratch Paper!'}, {'id': 'TS0gFlqr4ob', 'joke': 'What do you call a group of disorganized cats? A cat-tastrophe.'}, {'id': '0DdaxAX0orc', 'joke': 'I accidentally took my cats meds last night. Don’t ask meow.'}, {'id': '0wcFBQfiGBd', 'joke': 'Did you hear the joke about the wandering nun? She was a roman catholic.'}]