# __repr__ method

class User:
	# Class Attribute
	active_users = 0

	# Class Method
	@classmethod
	def display_active_users(cls):
		return f"There are currently {User.active_users} active users."

	# Class Method
	# Only write these when you don't need access to a specific instance, but the class itself
	# Commonly used to initiate a new instance from comma separated values, as shown below
	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(",")
		return cls(first, last, int(age))


	def __init__(self, first, last, age):
		# self referes to the individual instance of the class
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	# the __repr__ method is one of several ways to provide a nicer string representation of an instance
	# there are other dunders to return classes in string format like __str__ and __format__ and choosing one is a bit complicated
	def __repr__(self):
		return f"{self.full_name()} is {self.age}"

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def login(self):
		User.active_users += 1
		return f"{self.first} has logged in"

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

tom = User.from_string("Tom,Petty,70") # Initiating new User Tom Petty with the from_string() Class Method
print(tom.first) # Tom
print(tom.full_name()) # Tom Petty
print(tom.birthday()) # Happy 71th, Tom!

print(tom) # Tom Petty is 71 (because of the __repr__ method we defined)

e = User("Emma", "Kel", 27)
e = str(e) # __repr__ is also called when we turn the instance into a string
print(e) # Emma Kel is 27

