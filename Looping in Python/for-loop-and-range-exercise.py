#Use a for loop to add up every odd number from 10 to 20 (inclusive) and store the result in the variable x . 

# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# YOUR CODE GOES HERE: (conditional solution)
for num in range(10,21):
	if num % 2 == 1:
		x += num

# (range step solution)
# for i in range(11,21,2):
#     x += i