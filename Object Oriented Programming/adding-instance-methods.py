# Adding Instance Methods

class User:
	def __init__(self, first, last, age):
		# self referes to the individual instance of the class
		self.first = first
		self.last = last
		self.age = age

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

user1 = User("Emma", "Kel", 27)
user2 = User("Kevin", "Web", 45)

print(user1.first, user1.last, user1.age) # Emma Kel 27
print(user2.first, user2.last, user2.age) # Kevin Web 45
print(user2.full_name()) # Kevin Web
print(user1.initials()) # E.K.
print(user2.likes("coffee")) # Kevin likes coffee
print(user1.is_senior()) # False
print(user1.age) # 27
print(user1.birthday()) # Happy 28th, Emma!
print(user1.age) # 28