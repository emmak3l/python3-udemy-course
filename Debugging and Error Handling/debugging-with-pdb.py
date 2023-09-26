# Debugging with PDB

# PDB stands for "Python Debugger" and it's a module we can import just like random
# Once imported we can call the method .set_trace() which pauses execution of our code
# It allows us to step through our code in the terminal line by line to find bugs

# Example 1:
# Commonly called all on one line like this as it's temporary and will be deleted once used:
# import pdb; pdb.set_trace()


# Example 2:
# import pdb;
# first = "First"
# second = "Second"
# pdb.set_trace()
# result = first + second
# third = "Third"
# result += third
# print(result)

# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging - can use to exit the debugger)
# q (quit, but it's kindof clunky and throws an error before quitting)
# if your variable name conflicts with an existing command you wont be able to see it by just typing the variable,
# instead you must specify p first, which stands for print, and then the variable

# PDB Gotchas
def add_numbers(a,b,c,d):
	import pdb; pdb.set_trace()
	return a + b + c + d
add_numbers(1,2,3,4)