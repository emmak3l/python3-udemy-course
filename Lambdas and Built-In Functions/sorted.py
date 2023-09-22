# sorted

# Unlike sort which can only be used on lists, sorted can be used on anything that is iterable, like tuples
# Returns a new sorted list from the items in iterable

# Example 1:
more_numbers = [6,1,8,2]
sorted(more_numbers) # [1, 2, 6, 8] creates a copy of the list that's sorted
print(more_numbers) # [6, 1, 8, 2] does not change the original more_numbers list
# this is different from sort, which would have sorted the numbers in place and changed the order of the more_numbers list


# Example 2:
# You can change the direction it's sorted in by setting reverse=True
nums = [4,6,1,30,55,23]
sorted(nums, reverse=True) # [55, 30, 23, 6, 4, 1]


# Example 3:
# sorted accepts tuples as well but will still return a list
sorted((2,1,45,23,99)) # [1, 2, 23, 45, 99]


# Example 4:
users = [
	{'username': 'samuel', 'tweets': ["I love cake", "I love pie", "hello world!"]},
	{'username': 'katie', 'tweets': ["I love my cat"]},
	{'username': 'jeff', 'tweets': []},
	{'username': 'bob123', 'tweets': []},
	{'username': 'doggo_luvr', 'tweets': ["dogs are the best", "I'm hungry"]},
	{'username': 'guitar_gal', 'tweets': []}
]

# Sorting users by username, need to use a lambda:
sorted(users, key=lambda user: user['username']) # [{'username': 'bob123', 'tweets': []}, {'username': 'doggo_luvr', 'tweets': ["dogs are the best", "I'm hungry"]}, {'username': 'guitar_gal', 'tweets': []}, {'username': 'jeff', 'tweets': []}, {'username': 'katie', 'tweets': ["I love my cat"]}, {'username': 'samuel', 'tweets': ["I love cake", "I love pie"]}]

# Sorting users by number of tweets (ascending):
sorted(users, key=lambda user: len(user['tweets'])) # [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'guitar_gal', 'tweets': []}, {'username': 'katie', 'tweets': ["I love my cat"]}, {'username': 'doggo_luvr', 'tweets': ["dogs are the best", "I'm hungry"]}, {'username': 'samuel', 'tweets': ["I love cake", "I love pie", "hello world!"]}]

# Sorting users by number of tweets (descending):
sorted(users, key=lambda user: len(user['tweets']), reverse=True) # [{'username': 'samuel', 'tweets': ["I love cake", "I love pie", "hello world!"]}, {'username': 'doggo_luvr', 'tweets': ["dogs are the best", "I'm hungry"]}, {'username': 'katie', 'tweets': ["I love my cat"]}, {'username': 'guitar_gal', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'jeff', 'tweets': []}]


# Example 5:
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31},
]

# Sorting by playcount (ascending):
sorted(songs, key=lambda s: s['playcount']) # [{"title": "happy birthday", "playcount": 1}, {"title": "Survive", "playcount": 6}, {"title": "Toxic", "playcount": 31}, {"title": "YMCA", "playcount": 99}]

# Sorting by playcount (descending):
sorted(songs, key=lambda s: s['playcount'], reverse=True) # [{"title": "YMCA", "playcount": 99}, {"title": "Toxic", "playcount": 31}, {"title": "Survive", "playcount": 6}, {"title": "happy birthday", "playcount": 1}]


