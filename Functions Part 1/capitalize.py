# capitalize
# Write a function called capitalize.
# This function accepts a string and returns the same string with the first letter capitalized.  You may want to use slices to help you out.

# capitalize("jamaica") # "Jamaica"
# capitalize("chicken") # "Chicken"

'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(word):
	result = ""
	for l in word:
		if l == word[0]:
			result += l.upper()
		else:
			result += l
	return result

# BETTER SOLUTION BELOW:
# def capitalize(string):
#     return string[:1].upper() + string[1:]