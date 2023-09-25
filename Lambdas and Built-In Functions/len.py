# len

# Returns the length (the number of items) of an object.
# The arguement may be a sequence (such as a string, tuple, list or range) or a collection (such as a dictionary, set)

# Example 1:

# len on string, tuple, list and range
len('awesome') # 7
len((1,2,3,4)) # 4
len([1,2,3,4]) # 4
len(range(0,10)) # 10

# len on set and dictionary
len({1,2,3,4}) # 4
len('a':1, 'b':2, 'c':3) # 3


# Example 2, defining our own __len__ with small intro to OOP:
class SpecialList:
	def __init__(self, data):
		self.__data = data

	def __len__(self): # Pay attention to this line
		return 50

l1 = SpecialList([1,40,30,100])
l2 = []

print(len(l1)) # will always return 50, as that's how it's defined in the SpecialList class
print(len(l2)) # ^^
