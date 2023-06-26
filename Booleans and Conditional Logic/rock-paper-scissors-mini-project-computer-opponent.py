# Import randit so we can use it to generate our computers move
from random import randint

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
print("\nSHOOT!")

# Logic for the rock paper scissors game including a very basic exception handling else statement in case the player doesn't enter 'rock', 'paper', or 'scissors'
if player == computer:
	print(f"\nYou chose: {player}\nThe computer chose: {computer}\nThe game is a tie!")
elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
	print(f"\nYou chose: {player}\nThe computer chose: {computer}\nYou win!")
elif (computer == "rock" and player == "scissors") or (computer == "scissors" and player == "paper") or (computer == "paper" and player == "rock"):
	print(f"\nYou chose: {player}\nThe computer chose: {computer}\nThe computer wins!")
else:
	print("\nUh oh, something went wrong!\nPlease type either 'rock', 'paper', or 'scissors' next time.")