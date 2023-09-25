# Common Errors in python


# SyntaxError

# Occurs when python encounters incorrect syntac (something doesn't parse)
# Usually due to typos or not knowing python well enough

# Example 1:
def first: # SyntaxError

# Example 2:
None = 1 # SyntaxError

# Example 3:
return # SyntaxError



# NameError

# This occurs when a variable is not defined, i.e. it hasn't been assigned

# Example 1:
test # NameError: name 'test' is not defined



# TypeError

# This occurs when:
# An operation or function is applied to the wrong type 
# Python cannot interpret an operation on two data types

# Example 1:
len(5) # TypeError: object of type 'int' has no len()

# Example 2:
"awesome" + [ ] # TypeError: cannot concatenate 'str' and 'list' objects

# Example 3:
3 + 's' # TypeError: unsupported operand type(s) for +: 'int' and 'str'



# IndexError

# Occurs when you try to access an element in a list using an invalid index
# (i.e. one that is outside the range of the list or string):

# Example 1:
lst = ['hello']
lst[2] # IndexError: list index out of range

# Example 2:
name = 'colt'
name[4] # IndexError: string index out of range

# Example 3:
nums = (1,2,3,4)
nums[6] # IndexError: tuple index out of range



# ValueError

# This occurs when a built-in operation or function receives an argument that has the right type but an inappropriate value

# Example 1:
int("foo") # ValueError: invalid literal for int() with base 10: 'foo'



# KeyError

# This occurs when a dictionary does not have a specific key

# Example 1:
d = {}
d['foo'] # KeyError: 'foo'



# AttributeError

# This occurs when a variable does not have an attribute

# Example 1:
"awesome".foo # AttributeError: 'string' object has no attribute 'foo'

# Example 2:
[1,2,3].hello # AttributeError: 'list' object has no attribute 'hello'


# There are wayyy more errors than the ones listed here, these are just the most common
# All of the errors are listed in the documentation

