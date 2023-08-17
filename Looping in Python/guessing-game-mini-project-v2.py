# This is a more streamlined solution that the lecturer provided
# It doesn't include any error handling and I come back to this and add my own error-handling logic to it at another time

# INSTRUCTIONS FOR GUESSING GAME MINI PROJECT:
# handle user guesses
#	if they guess correct, tell them they won
#		otherwise tell them if they are too high or too low
# BONUS - let player play again if they want!

import random

random_number = random.randint(1,10)

while True:
	guess = input("Pick a number from 1-10: ")
	guess = int(guess)
	if guess < random_number:
		print("Too low!")
	elif guess > random_number:
		print("Too high!")
	else:
		print("You won!!!")
		play_again = input("Do you want to play again? (y/n) ")
		if play_again == "y":
			random_number = random.randint(1,10)
			guess = None
		else:
			print("Thank you for playing!")
			break