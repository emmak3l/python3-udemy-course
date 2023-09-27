# Custom Modules

# You can import from your own code too
# The syntax is the same as before
# import from the name of the python file

# Example 1: (pretend this is in it's own separate file)
# file1.py
def fn():
	return "do some stuff"

def other_fn():
	return "do some other stuff"

# (Now pretend we're in another file)
# file2.py
import file1

file1.fn() # 'do some stuff'

file1.other_fn() # 'do some other stuff'


# It does matter that the files are in the same directory!
# If they aren't in the same directory you have to reference the correct path!

# If you find yourself with code that needs to be used in more than one place, put it in a module!
# If you have a large file where you could group some of the functions into a module, do that!