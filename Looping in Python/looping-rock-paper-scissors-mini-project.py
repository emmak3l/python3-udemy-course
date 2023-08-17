# Import randit so we can use it to generate our computers move
from random import randint

# These variables keep track of how many times the player and computer has won as well as what the winning score is
player_wins = 0
computer_wins = 0
winning_score = 3

print("Rock... Paper... Scissors... Shoot!!!")
print("Best of 3 wins!")

# This loop runs continuously until there is a winner or until the user quits the program
while player_wins < winning_score and computer_wins < winning_score:
	print(f"\nPlayer Score: {player_wins} Computer Score: {computer_wins}")

	# Use randit to choose a random number between 0-2 and assign it to the variable 'num'
	num = randint(0, 2)

	# Use the 'num' variable to choose a move for the computer, either 'rock', 'paper', or 'scissors'
	if num == 0:
		computer = 'rock'
	elif num == 1:
		computer = 'paper'
	else:
		computer = 'scissors'

	# Title sequence and assign user input to the variable 'player'. The input is changed to all lowercase using the .lower() function to make the input case insensitive
	player = input("\nEnter your choice: ").lower()
	
	# If the player wants to quit before the game is over they can type 'quit' or 'q'
	if player == "quit" or player == "q":
		break

	print("\nSHOOT!")

	# Logic for the rock paper scissors game including a very basic exception handling else statement in case the player doesn't enter 'rock', 'paper', or 'scissors'
	if player == computer:
		print(f"\nYou chose: {player}\nThe computer chose: {computer}\nThe game is a tie!")
	elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
		print(f"\nYou chose: {player}\nThe computer chose: {computer}\nYou win!")
		player_wins += 1
	elif (computer == "rock" and player == "scissors") or (computer == "scissors" and player == "paper") or (computer == "paper" and player == "rock"):
		print(f"\nYou chose: {player}\nThe computer chose: {computer}\nThe computer wins!")
		computer_wins += 1
	else:
		print("\nUh oh, something went wrong!\nPlease type either 'rock', 'paper', or 'scissors' next time.")

# This conditional shows whether the player won, the computer won, or it's a tie 
if player_wins > computer_wins:
	print("Congrats, you won!!!")
elif player_wins == computer_wins:
	print("It's a tie!")
else:
	print("Oh no! The computer won :(")

# Printing the final score
print(f"\n*FINAL SCORE*\nPlayer: {player_wins} Computer: {computer_wins}")