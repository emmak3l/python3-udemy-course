# Assertions

# We can make simple assertions with the assert keyword
# assert accepts an expression and returns None if it's truthy and raises an AssertionError if falsy
# Acepts an optional error message as a second argument
# Not the be all end all of testing, there are better ways to test, this is just an option
# assert is not a function it's a statement

# def add_positive_numbers(x, y):
# 	assert x > 0 and y > 0, "Both numbers must be positive!"
# 	return x + y

# print(add_positive_numbers(1, 1)) # 2
# add_positive_numbers(1, -1) # AssertionError: Both numbers must be positive!

# if not some_expression: raise AssertionError()

def eat_junk(food):
	assert food in ['pizza', 'ice cream', 'candy', 'chocolate'], "Food must be a junk food!"
	return f"NOM NOM NOM I am eating {food}"

food = input("ENTER A FOOD PLEASE: ")
print(eat_junk(food))

# Assertions Warning
# all assert statements can be overridden(will not run, will not be evaluated, will be ignored) if the program is run in Optimized Mode (-O flag)