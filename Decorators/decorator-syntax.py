# Decorators with Different Signatures

def shout(fn):
	# doesn't have to be called wrapper but that's the standard since we're wrapping a function with it
	# to accept multiple parameters we can just use *args and **kwargs so that we can pass in any number of args or key value pairs
	def wrapper(*args, **kwargs):
		return fn(*args, **kwargs).upper()
	return wrapper

@shout
def greet(name):
	return f"Hi, I'm {name}"

@shout
def order(main, side):
	return f"Hi, I'd like the {main}, with a side of {side}, please"

@shout
def lol():
	return 'lol'

print(greet('todd'))
print(order('hamburger', 'fries'))
print(lol())