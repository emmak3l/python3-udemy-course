from random import randint

num = randint(0, 2)

if num == 0:
	computer = 'rock'
elif num == 1:
	computer = 'paper'
else:
	computer = 'scissors'

print("\n...rock...\n...paper...\n...scissors...")
player = input("\nEnter your choice: ").lower()
print("\nSHOOT!")

if player == computer:
	print(f"\nYou chose: {player}\nThe computer chose: {computer}\nThe game is a tie!")
elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
	print(f"\nYou chose: {player}\nThe computer chose: {computer}\nYou win!")
elif (computer == "rock" and player == "scissors") or (computer == "scissors" and player == "paper") or (computer == "paper" and player == "rock"):
	print(f"\nYou chose: {player}\nThe computer chose: {computer}\nThe computer wins!")
else:
	print("\nUh oh, something went wrong!\nPlease type either 'rock', 'paper', or 'scissors' as shown next time.")