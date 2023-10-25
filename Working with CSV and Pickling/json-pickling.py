# JSON Pickling

# pickle is a module that implements binary protocols for serializing and de-serializing
# a python object structure, where the object hierarchy is converted to a byte stream ('pickling'),
# and 'unpickling' converts the byte stream back into an object hierarchy.

import pickle

class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species='Cat')
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")


# blue = Cat("Blue", "Scottish Fold", "String")


# Pickling Example:
# with open("pets.pickle", 'wb') as file: # must specify 'wb'(write binary), and file must have a .pickle suffix
# 	pickle.dump(blue, file) # first the object you want serialized, then the file you want that serialized object to go

# The pets.pickle file looks like this, unreadable to humans:
# 8004 955d 0000 0000 0000 008c 085f 5f6d
# 6169 6e5f 5f94 8c03 4361 7494 9394 2981
# 947d 9428 8c04 6e61 6d65 948c 0442 6c75
# 6594 8c07 7370 6563 6965 7394 6801 8c05
# 6272 6565 6494 8c0d 5363 6f74 7469 7368
# 2046 6f6c 6494 8c03 746f 7994 8c06 5374
# 7269 6e67 9475 622e 

# If the data needs to be usable while it's stored you probably don't want to pickle it
# But if all you're doing is using a python file to open it back up and unpickle the data then this works fine


# Unpickling Example:
with open("pets.pickle", "rb") as file: # must specify 'rb'(read binary)
	zombie_blue = pickle.load(file)
	print(zombie_blue)
	print(zombie_blue.play())

