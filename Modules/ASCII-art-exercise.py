# ASCII Art Exercise

# Import the functions we need from the external modules we downloaded
from termcolor import colored
from pyfiglet import Figlet

# Ask user what message they want to print in what colour:
user_input = input("What message do you want to print? ")
user_colour = input("What colour? ")

# Set default colour to white if user provides invalid color option:
if user_colour not in ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'):
	user_colour = 'white'

# Create the ASCII art with the user_input:
ascii_art = Figlet(font='slant').renderText(user_input)

# Colour the ASCII art with the user_colour:
coloured_ascii = colored(ascii_art, color=user_colour)

# Print the final colourized ASCII art:
print(coloured_ascii)
