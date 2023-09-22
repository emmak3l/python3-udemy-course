# min and max

# max:
# Return the largest item in an iterable or the largest of two or more arguements

# Example 1:
max(3,67,99) # 99

max('c', 'd', 'a') # 'd' (because of the way strings are weighted)


# Example 2:
# max (strings, dicts with same keys)
max([3,4,1,2]) # 4
max((1,2,3,4)) # 4
max('awesome') # 'w'
max({1: 'a', 3: 'c', 2: 'b'}) # 3


# Example 3:
names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

min(names) # 'Arya' (goes by alphabetical order)
max(names) # 'Tim'        ^ same for max

# Finding the min length of value in names
min(len(names) for name in names) # 3

# Finding the name with the max characters
max(names, key=lambda n: len(n)) # 'Ollivander'


# Example 4:
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# Finding the song with the least number of plays
min(songs, key=lambda s: s['playcount']) # {"title": "happy birthday", "playcount": 1}

# Finding the song with the most number of plays
max(songs, key=lambda s: s['playcount']) # {"title": "YMCA", "playcount": 99}

# If we want only the title of the song we tack it on to the end
max(songs, key=lambda s: s['playcount'])['title'] # 'YMCA'