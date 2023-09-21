# filter

# there is a lambda for each value in the iterable
# returns filter object which can be converted into other iterables
# the object contains only the values that return true to the lambda


# Example 1:
l = [1,2,3,4]

evens = list(filter(lambda x: x % 2 == 0, l))

print(evens) # [2,4]


# Example 2:
names = ["austin", "penny", "anthony", "angel", "billy"]

a_names = list(filter(lambda n: n[0]=='a', names))

print(a_names) # ["austin", "anthony", "angel"]


# Example 3:
users = [
	{'username': 'samuel', 'tweets': ["I love cake", "I love pie"]},
	{'username': 'katie', 'tweets': ["I love my cat"]},
	{'username': 'jeff', 'tweets': []},
	{'username': 'bob123', 'tweets': []},
	{'username': 'doggo_luvr', 'tweets': ["dogs are the best", "I'm hungry"]},
	{'username': 'guitar_gal', 'tweets': []}
]

inactive_users = list(filter(lambda u: not u['tweets'], users))

print(inactive_users) # [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'guitar_gal', 'tweets': []}]

inactive_usernames = list(map(lambda user: user["username"].upper(),
	filter(lambda u: not u['tweets'], users)))

print(inactive_usernames) # ['JEFF', 'BOB123', 'GUITAR_GAL']


# Example 3.1 with List Comprehension instead:
inactive_users2 = [user for user in users if not user['tweets']]

print(inactive_users2) # [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'guitar_gal', 'tweets': []}]

inactive_usernames2 = [user["username"].upper() for user in users if not user['tweets']]

print(inactive_usernames2) # ['JEFF', 'BOB123', 'GUITAR_GAL']


# Example 4:
names2 = ['Lassie', 'Colt', 'Rusty']

instructor = list(map(lambda name: f"Your instructor is {name}",
	filter(lambda value: len(value) < 5, names2)))

print(instructor) # ['Your instructor is Colt']


# Example 4.1 as List Comprehension instead:
# If you can use a list comprehension instead you should!
print([f"Your instructor is {name}" for name in names2 if len(name) < 5]) # ['Your instructor is Colt']