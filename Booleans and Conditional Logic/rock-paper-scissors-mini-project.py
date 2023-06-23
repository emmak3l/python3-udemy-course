print("\n...rock...\n...paper...\n...scissors...")
player_1 = input("\nEnter Player 1's choice: ")
print("\n*** NO CHEATING ***\n\n" * 20)
player_2 = input("Enter Player 2's choice: ")
print("\nSHOOT!")

# My first attempt is below:

if player_1 == player_2:
	print(f"\nPlayer 1 chose: {player_1}\nPlayer 2 chose: {player_2}\nThe game is a tie!")
elif (player_1 == "rock" and player_2 == "scissors") or (player_1 == "scissors" and player_2 == "paper") or (player_1 == "paper" and player_2 == "rock"):
	print(f"\nPlayer 1 chose: {player_1}\nPlayer 2 chose: {player_2}\nPlayer 1 wins!")
elif (player_2 == "rock" and player_1 == "scissors") or (player_2 == "scissors" and player_1 == "paper") or (player_2 == "paper" and player_1 == "rock"):
	print(f"\nPlayer 1 chose: {player_1}\nPlayer 2 chose: {player_2}\nPlayer 2 wins!")
else:
	print("\nUh oh, something went wrong!\nPlease type either 'rock', 'paper', or 'scissors' as shown next time.")


# The code commented out below is more similar to the instructors way of doing it,
# but I don't like that if one player types 'rock', 'paper', or 'scissors' and the other player types nonsense they will never reach the error message the way it is laid out.

# if player_1 == player_2:
# 	print(f"\nPlayer 1 chose: {player_1}\nPlayer 2 chose: {player_2}\nThe game is a tie!")
# elif player_1 == "rock":
# 	if player_2 == "scissors":
# 		print(f"\nPlayer 1 chose: {player_1}\nPlayer 2 chose: {player_2}\nPlayer 1 wins!")
# 	elif player_2 == "paper":
# 		print(f"\nPlayer 1 chose: {player_1}\nPlayer 2 chose: {player_2}\nPlayer 2 wins!")
# elif player_1 == "paper":
# 	if playe_2 == "rock":
# 		print(f"\nPlayer 1 chose: {player_1}\nPlayer 2 chose: {player_2}\nPlayer 1 wins!")
# 	elif player_2 == "scissors":
# 		print(f"\nPlayer 1 chose: {player_1}\nPlayer 2 chose: {player_2}\nPlayer 2 wins!")
# elif player_1 == "scissors":
# 	if player_2 == "paper":
# 		print(f"\nPlayer 1 chose: {player_1}\nPlayer 2 chose: {player_2}\nPlayer 1 wins!")
# 	elif player_2 == "rock":
# 		print(f"\nPlayer 1 chose: {player_1}\nPlayer 2 chose: {player_2}\nPlayer 2 wins!")	
# else:
# 	print("\nUh oh, something went wrong!\nPlease type either 'rock', 'paper', or 'scissors' as shown next time.")