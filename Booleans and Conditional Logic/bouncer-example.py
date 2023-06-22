# ask for age
age = input("How old are you?: ")

if age:
	age = int(age)
	if age >= 21:
		# 21+ drink, normal entry
		print("You can enter and can drink!")
	elif age >= 18:
		# 18-21 wristband
		print("You can enter, but you need a wristband!")
	else:
		# too young sorry
		print("You can't come in little one, sorry!")
else:
	print("Please enter an age!")