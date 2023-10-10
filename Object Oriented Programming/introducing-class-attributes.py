# Introducing Class Attributes

class User:
	# Class Attribute
	active_users = 0

	def __init__(self, first, last, age):
		# self referes to the individual instance of the class
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self,thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}!"

print(User.active_users) # 0
user1 = User("Emma", "Kel", 27)
user2 = User("Kevin", "Web", 45)
print(User.active_users) # 2
print(user2.logout()) # Kevin has logged out
print(User.active_users) # 1

# print(user1.first, user1.last, user1.age) # Emma Kel 27
# print(user2.first, user2.last, user2.age) # Kevin Web 45
# print(user2.full_name()) # Kevin Web
# print(user1.initials()) # E.K.
# print(user2.likes("coffee")) # Kevin likes coffee
# print(user1.is_senior()) # False
# print(user1.age) # 27
# print(user1.birthday()) # Happy 28th, Emma!
# print(user1.age) # 28

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Pet:
	# Class attribute
	allowed = ['cat', 'dog', 'fish', 'rat']
	def __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species

	def set_species(self, species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species


cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
# tiger = Pet("Mike", "tiger") # You can't have a tiger pet!
dog.set_species('tiger') # You can't have a tiger pet!

# All three of these id methods will point to the exact same memory address
# This is because cat.allowed and dog.allowed are both references that point to Pet.allowed
id(cat.allowed)
id(dog.allowed)
id(Pet.allowed)



