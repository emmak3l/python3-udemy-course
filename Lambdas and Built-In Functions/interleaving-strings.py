# Interleaving Strings (kind of tough!)
# This challenge is a bit more involved than the others in this section.
# Do not worry if you can't get it!

# Write a function interleave  that accepts two strings.
# It should return a new string containing the 2 strings interwoven or zipped together.
# For example:

# interleave('hi','ha')    # 'hhia'

# interleave('aaa', 'zzz')  # 'azazaz'

# interleave('lzr','iad') #  'lizard'

# This might seem like an easy task using zip , but in fact there are a couple intermediate steps to go from zip back to a single string.
# If you need help, I've written up a basic walkthrough of the steps:

# suppose we call interleave('hi', 'no')  

# zip  the two strings together, giving you a list of tuples (once you convert from the default zip_object)
# -  [('h','n'), ('i','o')]  

# For each of the tuples in the list, join them together using "".join  resulting in ['hn', 'io']
# - Easiest if you use a list comp.  You need to join EACH tuple.

# Finally, join the items in the list together using "".join  again resulting in 'hnio'  

# Don't stress if you don't get this one!

# First solution:
def interleave(str1, str2):
	first_zip = list(zip(str1, str2))
	first_join = [''.join(s) for s in first_zip]
	return ''.join(first_join)

# Second solution: (instructors version)
def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))