# super()

class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def speak(self, sound):
		return f"The animal goes {sound}"


class Cat(Animal):
	def __init__(self, name, breed, toy):
		# The super() method allows us to set the __init__ properties of the parent class, in this case Animal
		# This reduces duplication
		# We set the species to default to "Cat" for the Cat class so we don't have to specify it when instantiating a new Cat
		super().__init__(name, species="Cat")
		self.breed = breed
		self.toy = toy

	def play(self):
		return f"{self.name} plays with {self.toy}"

jinx = Cat("Jinx", "Calico", "Ball")
print(jinx.play()) # Jinx plays with Ball
print(jinx # Jinx is a Cat