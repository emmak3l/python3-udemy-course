# Doctests

# - We can write tests for functions inside of the docstring
# - Write code that looks like it's inside of a REPL

def add(a, b):
	"""
	>>> add(2, 3)
	5
	>>> add(100,200)
	300
	"""
	# return a * b # This is purposefully incorrect to show the tests failing
	return a + b

# To get python to run these tests we write this in the terminal:
# python3 -m doctest -v name_of_file.py


# Below is what we see in the terminal when returning a * b in the add function: (Failed tests)
# Trying:
#     add(2, 3)
# Expecting:
#     5
# **********************************************************************
# File "/Users/emma/Documents/GitHub/python3-udemy-course/Testing/doctests.py", line 8, in doctests.add
# Failed example:
#     add(2, 3)
# Expected:
#     5
# Got:
#     6
# Trying:
#     add(100,200)
# Expecting:
#     300
# **********************************************************************
# File "/Users/emma/Documents/GitHub/python3-udemy-course/Testing/doctests.py", line 10, in doctests.add
# Failed example:
#     add(100,200)
# Expected:
#     300
# Got:
#     20000
# 1 items had no tests:
#     doctests
# **********************************************************************
# 1 items had failures:
#    2 of   2 in doctests.add
# 2 tests in 2 items.
# 0 passed and 2 failed.
# ***Test Failed*** 2 failures.


# Below is what we see in the terminal when returning a + b in the add function: (Passed Tests)
# Trying:
#     add(2, 3)
# Expecting:
#     5
# ok
# Trying:
#     add(100,200)
# Expecting:
#     300
# ok
# 1 items had no tests:
#     doctests
# 1 items passed all tests:
#    2 tests in doctests.add
# 2 tests in 2 items.
# 2 passed and 0 failed.
# Test passed.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Writing Tests the Test Driven Design(TDD) Way

# - Tests should fail first, remember "Red, Green, Refactor"

def double(values):
	""" double the values in a list

	>>> double([1,2,3,4])
	[2, 4, 6, 8]

	>>> double([])
	[]

	>>> double(['a','b','c'])
	['aa', 'bb', 'cc']

	>>> double([True, None])
	Traceback (most recent call last):
		...
	TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
	"""
	return [v*2 for v in values]

# Below are the results (I didn't paste the first examples tests again, that's why it says 6 tests passed instead of 4 tests)
# Trying:
#     double([1,2,3,4])
# Expecting:
#     [2, 4, 6, 8]
# ok
# Trying:
#     double([])
# Expecting:
#     []
# ok
# Trying:
#     double(['a','b','c'])
# Expecting:
#     ['aa', 'bb', 'cc']
# ok
# Trying:
#     double([True, None])
# Expecting:
#     Traceback (most recent call last):
#             ...
#     TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
# ok
# 1 items had no tests:
#     doctests
# 2 items passed all tests:
#    2 tests in doctests.add
#    4 tests in doctests.double
# 6 tests in 3 items.
# 6 passed and 0 failed.
# Test passed.


# Some things to Note:
# - Doctest always expects strings to be wrapped in single quotes: ''  not double quotes ""
# - If there is a trailing whitespace when expecting a bool (True or False) then the doctest with also fail
# - Doctest cares about the order of keys in a dict

# Issues with Doctests:
# - Syntax is a little strange
# - Clutters up our function code
# - Lacks many features of larger testing tools
# - Tests can be brittle






