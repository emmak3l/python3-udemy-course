# Intro to Decorators

# - Decorators are functions
# - They wrap other functions and enhance their behavior
# - They are examples of higher order functions
# - They have their own syntax, using "@" (syntactic sugar)

# def be_polite(fn):
# 	def wrapper():
# 		print("What a pleasure to meet you!")
# 		fn()
# 		print("Have a great day!")
# 	return wrapper

# def greet():
# 	print("My name is Colt.")

# def rage():
# 	print('I HATE YOU!')

# we are decorating our function with politeness!
# greeting = be_polite(greet)
# greeting()
# What a pleasure to meet you!
# My name is Colt.
# Have a great day!

# polite_rage = be_polite(rage)
# polite_rage()
# What a pleasure to meet you!
# I HATE YOU!
# Have a great day!

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Decorator Syntax

def be_polite(fn):
	def wrapper():
		print("What a pleasure to meet you!")
		fn()
		print("Have a great day!")
	return wrapper

@be_polite
def greet():
	print("My name is Colt.")

@be_polite
def rage():
	print('I HATE YOU!')

# Now we don't need to set
# greeting = be_polite(greet)

greet()
# What a pleasure to meet you!
# My name is Colt.
# Have a great day!

rage()
# What a pleasure to meet you!
# I HATE YOU!
# Have a great day!



