# Set Comprehension
# Looks similar to dictionary comprehension but without keys and values

new_set = {x**2 for x in range(10)} # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

another_set = {char.upper() for char in 'hello'} # {'O', 'L', 'E', 'H'}

# function that uses set comprehension to check if all 5 vowels are in a string
def are_all_vowels_in_string(string):
	return len({char for char in string if char in 'aeiou'}) == 5

string = 'sequoia' # has all 5 vowels

are_all_vowels_in_string(string) # True

