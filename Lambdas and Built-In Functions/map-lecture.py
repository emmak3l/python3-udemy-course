# map

# a standard function that accepts at least two arguments, a function, and an 'interable'
# iterable - something that can be iterated over (lists, strings, dictionaries, sets, tuples)
# runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure


# Example 1:
nums = [2,4,6,8,10]

# you don't have to create a lambda you can also pass in a named function instead
doubles = map(lambda x: x*2, nums)

print(doubles) # this returns <map object at 0x1010dbe50>

list(doubles) # this converts the map object to a list, [4, 8, 16, 20]

# doubles = list(map(lambda x: x*2, nums)) # this is usually how it would be written so doubles is turned into a list from the start


# Example 2:
people = ["Darcy", "Christina", "Dana", "Annabel"]

peeps = list(map(lambda name: name.upper, people))


# Example 3:
names = [
	{'first':'Rusty', 'last':'Steele'},
	{'first':'Colt', 'last':'Steele'},
	{'first':'Blue', 'last':'Steele'}
]

first_names = list(map(lambda x: x['first'], names))

first_names # ['Rusty', 'Colt', 'Blue']