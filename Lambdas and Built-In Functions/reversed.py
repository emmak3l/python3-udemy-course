# reversed

# Returns a reverse iterator object

nums = [1,2,3,4]

reversed(nums) # list_reverseiterator object at ___________

list(reversed(nums)) # [4,3,2,1]


# Using a slice to reverse a string:
"hello"[::-1] # "olleh"

# Using reversed on a string:
reversed("hello") # reversed object at ___________

list(reversed("hello")) # ['o', 'l', 'l', 'e', 'h']

''.join(list(reversed("hello")))


# Using reversed on a range:
for x in reversed(range(0,10)):  # 9 \n 8 \n 7 \n 6 \n 5 \n 4 \n 3 \n 2 \n 1 \n 0
	print(x)