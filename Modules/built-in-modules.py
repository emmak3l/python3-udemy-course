# Working with Built-In Modules

# Why use Modules?:
# - Keeps Python files small
# - Reuse code across multiple files by importing
# - A module is just a Python file!

# Built-In Modules Examples

# Example 1:
# You can also give the module an ailis by using the 'as' keyword
# import random as r

# r.choice(["apple", "banana", "cherry", "durian"]) # picks a random option from the choices provided
# r.randint(0,100) # picks a random integer

# You can import parts of a module by using the keyword 'from'
# Good rule of thumb is to only import what you need!
# If you still want to import everything, you can also use the from MODULE import * pattern
from random import choice, randint

# If you do it this way you no longer have to reference the module name or ailis when calling the method, you can now just use the name of the method
choice(["apple", "banana", "cherry", "durian"]) # picks a random option from the choices provided
randint(0,100) # picks a random integer
