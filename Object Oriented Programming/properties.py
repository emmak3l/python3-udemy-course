# Properties

class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = age

	# Setting a property allows us to get/set a private property without accessing it directly by doing _age
	# This is a get property
	@property
	def age(self):
		return self._age

	# This is a setter property, it includes some validation so that the age cannot be set to a negative number
	@age.setter
	def age(self, value):
		if value >= 0:
			self._age = value
		else:
			raise ValueError("age can't be negative!")

emma = Human("Emma", "Kel", 27)

# What's nice about properties is when we call them we don't have to call them with brackets after (Human.age()) like we would with a regular method
print(emma.age)
emma.age = 28
print(emma.age)

