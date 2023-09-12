# is_palindrome

# Write a function called is_palindrome.
# A Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.
# This function should take in one parameter and returns True or False depending on whether it is a palindrome.
# As a bonus, allow your function to ignore whitespace and capitalization so that is_palindrome('a man a plan a canal Panama') returns True.

'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(string):
	stripped = string.replace(" ", "").upper()
	return stripped == stripped[::-1]