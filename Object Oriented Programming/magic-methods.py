# Magic Methods

# Imported this so we can make clones with the ___mul___ magic method
from copy import copy

class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = age

	def __repr__(self):
		return f"Human named {self.first} {self.last}"

	# below are three magic methods (__len__, __add__, __mul__) we defined for the human class that override their original functionality with whatever we decide for this particular class
	def __len__(self):
		return self._age

	def __add__(self, other):
		if isinstance(other, Human):
			return Human(first="Newborn", last=self.last, age=0)
		raise TypeError("You can't add a Human and a non-human!")

	def __mul__(self, other):
		if isinstance(other, int):
			# copy allows us to create new memory addresses for the object we are replicating, so that each instance is its own object and not a reference that points to the original
			return [copy(self) for i in range(other)]
		raise TypeError("You can't multiply these two types!")


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
kevin = Human("Kevin", "Web", 45)

print(kevin + emma) # Human named Newborn Web
triplets = kevin * 3 # [Human named Kevin Web, Human named Kevin Web, Human named Kevin Web]
triplets[1].first = 'Kyle' # Changing the second triplets first name to Kyle
triplets[2].first = 'Keanu' # Changing the third triplets first name to Keanu
print(triplets) # [Human named Kevin Web, Human named Kyle Web, Human named Keanu Web]