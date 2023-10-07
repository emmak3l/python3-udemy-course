# The __init__ Method

# Classes in Python can have a special __init__ method, which gets called every time you create an instance of the class (instantiate)

class User:
	def __init__(self, first, last, age):
		# self referes to the individual instance of the class
		self.first = first
		self.last = last
		self.age = age

# creating an onbject that is an instance of a class is called instantiating a class
# so user1 and user2 becomes an instance of the User class
# you pass in any attributes as arguements
user1 = User("Emma", "Kel", 27)
user1 = User("Kevin", "Web", 45)

print(user1.first, user1.last) # Emma Kel
print(user2.first, user2.last) # Kevin Web
