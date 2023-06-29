# Ask user for a numeric input and store that in the variable num
num = input("How many times do I have to tell you? ")

# Use isnumeric() to make sure the input can be converted to an int, otherwise we print an error message.
if num.isnumeric():
	# Convert the num variable from a string to an int
	num = int(num)
	# Repeat the print function the same amount of times as the user's input
	for x in range(num):
		print("CLEAN UP YOUR ROOM!")
# Error message will display if user has input anything that can't be converted to an int
else:
	print("Uh oh! You didn't input a valid integer.")

