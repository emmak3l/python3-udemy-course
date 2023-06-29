# My first solution with multiple print statements
# for x in range(1,21):
# 	if x == 4 or x == 13:
# 		print(f"{x} is UNLUCKY!")
# 	elif x % 2 == 1:
# 		print(f"{x} is odd")
# 	else:
# 		print(f"{x} is even")

# Optimized solution below with only one print statement
for x in range(1,21):
	if x == 4 or x == 13:
		state = "UNLUCKY!"
	elif x % 2 == 1:
		state = "odd"
	else:
		state = "even"
	print(f"{x} is {state}")