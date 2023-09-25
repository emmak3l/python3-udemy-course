# abs

# Returns the absolute value of a number. (The magnitude of a real number without regard to it's sign)
# The argument may be an integer or a floating point number.
# For example the absolute value of 100 is 100, absolute value of -69 is 69

# Example 1:
abs(-5) # 5
abs(5) # 5
abs(-3.4444) # 3.4444
abs(3.4444) # 3.4444


# sum

# Takes an iterable and an optional start
# Returns the sum of start and the items of an iterable from left to right and returns the total
# Start by default is 0

# Example 1:
sum([1,2,3]) # 6

# Adding a starting point:
sum([1,2,3], 10) # 16
sum([1,2,3], -6) # 0

# Using a tuple:
sum((1.5, 2, 3.7)) # 7.2

# Using a set:
sum({1, 50, 100}) # 151

# Using a string:
sum(['hi', 'there']) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

sum(['hi', 'there'], 'lol') # TypeError: sum() can't sum strings [use ''.join(seq) instead]



# round

# Returns number rounded to ndigits precision after the decimal point.
# If ndigits is omitted or is None, it returns the nearest integer to its input

# Example 1:
round(10.2) # 10
round(1.212121, 2) # 1.21
round(3.51234) # 3
round(3.51234, 3) # 3.512
round(3.51234, None) # 4
round(9.999999999999999999999999999999999, 15) # 10.0, at some point the precision slips