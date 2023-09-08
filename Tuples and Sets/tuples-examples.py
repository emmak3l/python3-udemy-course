# Tuples are commonly used for UNCHANGING data:
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# We can iterate through tuples using for loops:
for month in months:
	print(month)

# We can also iterate through tuples using while loops:
i = len(months) - 1
while i >= 0:
	print(months[i])
	i -= 1

# .count() is one of the two methods built in for tuples
x = (1,2,3,3,3)
x.count(1) # 1
x.count(3) # 3

# .index() is the other built in tuple method
t = (1,2,3,3,3)
t.index(1) # 0
t.index(5) # ValueError: tuple.index(x): x not in tuple
t.index(3) # 2 - only the first matching index is returned

# Tuples can be used as keys in dictionaries: (lists cannot be used as keys)
locations = {
	(35.6895, 39.6917): "Tokyo Office",
	(40.7128, 74.0060): "New York Office",
	(37.7749, 122.4194): "San Francisco Office"
}

# Some dictionary methods like .items() return tuples
cat = {'name': 'Biscuit', 'age': 0.5, 'favourite_toy': 'my chapstick'}
cat.items()
# dict_items([('name', 'Biscuit'), ('age', 0.5), ('favourite_toy', 'my chapstick')])
#                tuple ^             tuple ^                tuple ^


# You can nest tuples:
nums = (1,2,3,(4,5),6,7)

# You can slice tuples:
nums[0:] # (1,2,3,(4,5),6,7)
nums[0:4] # (1,2,3,(4,5))
nums[0:4:2] # (1,3)