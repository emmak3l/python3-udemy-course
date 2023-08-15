# INSTRUCTIONS FOR GUESSING GAME MINI PROJECT:
# handle user guesses
#	if they guess correct, tell them they won
#		otherwise tell them if they are too high or too low
# BONUS - let player play again if they want!

import random

# this variable will determine whether the player would like to keep playing,
keep_playing = "y" 

# this while loop will continue as long as the user wants to keep playing the game
while keep_playing == "y":
	# ask the user to pick a number between 1-10
	user_guess = input("Guess a number between 1 and 10: ")

	# set the random_number variable to a random int between 1 - 10
	random_number = random.randint(1,10)

	# error handling to check whether the user_guess is a valid int to use or whether the string contains an int
	if isinstance(user_guess, int) or user_guess.isnumeric():
		# convert the string to an int
		user_guess = int(user_guess)

		# this while loop continues for as long as the user has guessed incorrectly.
		# there is also some built in error handling in case the user_guess is not a valid int
		while user_guess != random_number:	
			if isinstance(user_guess, int) or user_guess.isnumeric():
				user_guess = int(user_guess)
				if user_guess < random_number:
					print("Too low, try again!")
					user_guess = input("Guess a number between 1 and 10: ")
				elif user_guess > random_number:
					print("Too high, try again!")
					user_guess = input("Guess a number between 1 and 10: ")
			else:
				print("Uh oh! You didn't input a valid integer, try again.")
				user_guess = input("Guess a number between 1 and 10: ")
		
		# when the user guesses correctly it prints a congrats message and asks if the user would like to play again
		print("You guessed it! You won!")
		keep_playing = input("Do you want to keep playing? (y/n) ")

		# this while loop acts as error handling in case the user types anything other than a 'y' or an 'n'
		while keep_playing != "y" and keep_playing != "n":
			print("Please type either 'y' to continue playing or 'n' to exit. ")
			keep_playing = input("Do you want to keep playing? (y/n) ")
			if keep_playing == "y":
				random_number = random.randint(1,10)
			elif keep_playing == "n":
				print("Thanks for playing. Bye!")
				break
		# if the user decides not to play again we print this goodbye message
		if keep_playing == 'n':
			print("Thanks for playing. Bye!")
	# if the user_guess variable doesn't contain a valid int than this error message will print and the user will be asked to guess again
	else:
		print("Uh oh! You didn't input a valid integer, try again.")