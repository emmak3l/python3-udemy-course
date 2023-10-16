# Higher Order Functions (review)

# There are a few types of higher order functions as demonstrated below


# We can pass functions as args to other functions like so:

def sum(n, func):
	total = 0
	for num in range(1, n+1):
		total += func(num)
	return total

def square(x):
	return x*x

def cube(x):
	return x*x*x

print(sum(3, square)) # 14
print(sum(3, cube)) # 36


# We can also nest a function inside of another function like so:

from random import choice

def greet(person):
	def get_mood():
		msg = choice(('Hello there ', 'Go away ', 'I love you '))
		return msg
	result = get_mood() + person
	return result

print(greet('Kevin')) # This returns either 'Hello there Kevin', 'Go away Kevin', or 'I love you Kevin'


# We can also return another function

def make_laugh_func():
	def get_laugh():
		l = choice(('HAHAHAHA', 'lol', 'tehehe'))
		return l
	return get_laugh

laugh = make_laugh_func()
print(laugh()) # When we execute our laugh variable which is holding the function returned from make_laugh_func(), it returns 'HAHAHAHA', 'lol', or 'tehehe'


# We can also return a function while passing a normal variable arg into the main function
# Inner functions can access outer function scope
# This is what's known as a closure

def make_laugh_at_func(person):
	def get_laugh():
		l = choice(('HAHAHAHA', 'lol', 'tehehe'))
		return f"{l} {person}"
	return get_laugh

laugh_at = make_laugh_at_func('Linda')
print(laugh_at()) # When we execute() our laugh_at variable which is holding the function returned from make_laugh_at_func(), it returns 'HAHAHAHA Linda', 'lol Linda', or 'tehehe Linda'




