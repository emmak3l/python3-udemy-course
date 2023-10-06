# Dad Jokes Generator

import requests
from termcolor import colored
from pyfiglet import Figlet
from random import choice

# Create the ASCII art title:
print(colored(Figlet(font='slant').renderText("Dad Joke 3000"), color="magenta"))

# Get the topic from the user and store it in the variable user_input
user_input = input("Let me tell you a joke! Give me a topic: ")

# This is the url we'll be getting the dad jokes from
url = "https://icanhazdadjoke.com/search"

# This will search for jokes that match the user_input and store it in the variable response
response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": {user_input}}
)

# This converts the response into a python dictionary and stores it in the variable data
data = response.json()

# This pulls only the results we want from the data (which is a list of dictionaries containing the id and joke) and stores it in the variable results
results = data["results"]

# This list comprehension pulls only the jokes out of the results and stores it in the variable jokes
jokes = [j['joke'] for j in results]

# If we couldn't find any results that match the user_input we apologize and ask the user to try again
if len(jokes) == 0:
	print(f"Sorry, I don't have any jokes about {user_input}! Please try again.")
# If we only found one joke we say so and print the joke
elif len(jokes) == 1:
	print(f"I've got one joke about {user_input}. Here it is:\n{jokes[0]}")
# If we find multiple jokes we pick one at random using choice() method and then tell that one to the user
else:
	print(f"I've got {len(jokes)} jokes about {user_input}. Here's one:\n{choice(jokes)}")

 