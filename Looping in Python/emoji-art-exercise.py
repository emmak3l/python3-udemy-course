# Instructions: Print a repeating smiley face emoji pattern that repeats 10 times and grows by one emoji each iteration.
# Complete the exercise with both a for loop and a while loop.

# My for loop solution
for x in range(1,11):
	print("\U0001f600" * x)

# My while loop solution
x = 1
while x < 11:	
	print("\U0001f600" * x)
	x += 1

# Nested loop example the instructor gave
# for x in range(3):
# 	for x in range(1,11):
# 		print("\U0001f600" * x)

# While loop nested in a for loop. Example the instructor gave that's ugly but will work if you didn't want to multiply the string 
for x in range(1,11):
	count = 1
	smileys = ""
	while count <= x:
		smileys += "\U0001f600"
		count += 1
	print(smileys)