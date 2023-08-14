# Instructions: Use a while loop to generate a random number between 1 and 10 until you get the number 5. Every time the loop runs, increment the variable i .
# Here are more detailed steps:
# 	- Generate a random number between 1 and 10 using randint(1, 10) , storing the result in the number variable
# 	- Write a while loop to keep regenerating a new random number between 1 and 10 while the random number is not equal to 5.
# 	- In order for my tests to work, please add 1 to i  each time through the loop.  My tests use this variable to check how many times your loops runs.

from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5: # keep looping while the number isn't 5
	print(number) # printing the number to manually check that it's not a 5
	number = randint(1,10) # resetting the number to a random int between 1 and 10
	i += 1 # incrementing i by 1 for each iteration
print(f"you have now exited the loop, the number is: {number}") # printing an exit message to check that the number was actually 5 when the program exits