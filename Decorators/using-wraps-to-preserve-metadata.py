# Using Wraps to Preserve Metadata

# To preserve the metadata for the function that gets passed into the wrapper,
# we need to import the wraps tool from the functools library
from functools import wraps

def log_function_data(fn):
	# By adding @wraps(fn) before our wrapper function, it ensures that the metadata for fn is preserved
	# So when a user tries to access the __doc__ or __name__ of fn, it will display those attributes of the fn
	# Without this, when a user tries to access the __doc__ or __name__ of the fn, python will return those attributes for the wrapper function instead of the fn function
	@wraps(fn)
	def wrapper(*args, **kwargs):
		"""I AM A WRAPPER FUNCTION"""
		print(f"You are about to call {fn.__name__}")
		print(f"Here's the documentation: {fn.__doc__}")
		return fn(*args, **kwargs)
	return wrapper

@log_function_data
def add(x,y):
	"""Adds two numbers together."""
	return x + y

print(add(5, 3))
# ^ You are about to call add
#   Here's the documentation: Adds two numbers together.
#   8 

print(add.__doc__) # Adds two numbers together
print(add.__name__) # add
# help(add)
# ^ add(x, y)
#   Adds two numbers together.
