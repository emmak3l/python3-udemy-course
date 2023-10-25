# Extra Fancy JSON Pickling

# JSON Demo:

# import json

# class Cat():
# 	def __init__(self, name, breed):
# 		self.name = name
# 		self.breed = breed


# # json.dumps formats a python object as a string of JSON
# #j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

# # print(j) # ["foo", {"bar": ["baz", null, 1.0, 2]}]

# c = Cat('Charles', 'Tabby')

# j = json.dumps(c.__dict__) # converts Cat object to a dict, which is then converted into json

# print(j) # {"name": "Charles", "breed": "Tabby"}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# JSON Pickle Demo:

import jsonpickle

class Cat():
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed

# c = Cat('Charles', 'Tabby')

# with open('cat.json', 'w') as file:
# 	frozen = jsonpickle.encode(c)
# 	file.write(frozen) # new cat.json file now has this data: {"py/object": "__main__.Cat", "name": "Charles", "breed": "Tabby"}

# print(frozen) # {"py/object": "__main__.Cat", "name": "Charles", "breed": "Tabby"}

with open('cat.json', 'r') as file:
	contents = file.read()
	unfrozen = jsonpickle.decode(contents)
	print(unfrozen) # <__main__.Cat object at 0x10a55f410>