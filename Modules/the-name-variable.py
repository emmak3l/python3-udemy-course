# The Mysterious __name__ Variable

# When run, every Python file has a __name__ variable
# If the file is the main file being run, it's value is "__main__"
# Otherwise, its value is the file name

# Imagine we have a python file called say_hi.py that includes this function:
def say_hi():
	print(f"HI! My __name__ is  {__name__}")

say_hi() # HI! My __name__ is __main__


# Imagine we have another python file called say_sup.py that has this function:
def say_sup():
	print(f"SUP! My __name__ is  {__name__}")

say_sup()

# If we import the say_sup function into say_hi.py file and run both functions this is what it would look like:
from say_sup import say_sup
def say_hi():
	print(f"HI! My __name__ is  {__name__}")

say_hi()
say_sup()

# OUTPUT:
# HI! My __name__ is say_sup
# HI! My __name__ is __main__
# HI! My __name__ is say_sup


# import Revisited

# When you use import, Python...
# 1. Tries to find the module (if it fails it throws an error)
# 2. Runs the code inside of the module being imported

# So because we are running say_sup() in the say_sup.py file,
# Python runs that first when executing the say_hi.py file because of the nature of import

# To ignore code on import so it doesn't automatically run, we can do this:


	# this code will only run if the file is the main file!


# To fix our previous code example we should do this to our say_sup.py file:
def say_sup():
	print(f"SUP! My __name__ is  {__name__}")

if __name__ == "__main__":
	say_sup()

# Now it won't double print when we execute the say_hi.py file:
from say_sup import say_sup
def say_hi():
	print(f"HI! My __name__ is  {__name__}")

say_hi()
say_sup()

# OUTPUT:
# HI! My __name__ is __main__
# HI! My __name__ is say_sup