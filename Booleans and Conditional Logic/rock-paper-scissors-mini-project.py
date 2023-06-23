print("...rock...\n...paper...\n...scissors...")
player_1 = input("\nEnter Player 1's choice: ")
print("\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n")
player_2 = input("Enter Player 2's choice: ")
print("\nSHOOT!")

if (player_1 == "rock" and player_2 == "scissors") or (player_1 == "scissors" and player_2 == "paper") or (player_1 == "paper" and player_2 == "rock"):
	print(f"\nPlayer 1 chose: {player_1}\nPlayer 2 chose: {player_2}\nPlayer 1 wins!")
elif player_1 == player_2:
	print(f"\nPlayer 1 chose: {player_1}\nPlayer 2 chose: {player_2}\nThe game is a tie!")
else:
	print(f"\nPlayer 1 chose: {player_1}\nPlayer 2 chose: {player_2}\nPlayer 2 wins!")