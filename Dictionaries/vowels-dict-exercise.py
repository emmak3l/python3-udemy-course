# Vowels Dict Exercise
# Create a dictionary with the key as a vowel in the alphabet and the value as 0. 
# Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}.

# Do this programmatically (using a dict comprehension or dict method) rather than hard coding the answer!

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {k: 0 for k in ['a','e','i','o','u']}



# ALTERNATE ANSWERS

# Using dictionary comprehension with string and char instead of list
answer = {char:0 for char in 'aeiou'}


# Using dict.fromkeys
answer = dict.fromkeys("aeiou", 0)