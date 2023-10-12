# Inheritance

# You can access the properties of a class in a different class by inheriting from it

class Animal:
	is_cool = True

	def speak(self, sound):
		return f"The animal goes {sound}"


# Here the class Cat is inheriting from the class Animal and has access to it's properties and methods
class Cat(Animal):
	pass

cat = Cat()
print(cat.speak("meow")) # The animal goes meow
print(cat.is_cool) # True

# Because of inheritance, the variable cat is both an instance of the class Cat and the class Animal
print(isinstance(cat, Cat)) # True
print(isinstance(cat, Animal)) # True
