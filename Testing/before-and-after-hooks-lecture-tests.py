# Before and After Hooks

# setUp and tearDown:
# - for larger applications, you may want similar application state before running tests
# - setUp runs before each test method
# - tearDown runs after each test method
# - Common use cases: adding/removing data from a test database, creating instances of a class

# Example1:

# class SomeTests(unittest.TestCase):

# 	def setUp(self):
# 		# do setup here
# 		pass

# 	def test_first(self):
# 		# setUp runs before
# 		# tearDown runs after

# 	def test_second(self):
# 		# setUp runs before
# 		# tearDown runs after

# 	def tearDown(self):
# 		# do teardown here
# 		pass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Robot Class Example

import unittest
from robotbaah import Robot

class RobotTests(unittest.TestCase):
	def setUp(self):
		self.mega_man = Robot("Mega Man", battery=50)
	def test_charge(self):
		"""The battery should be 100 after the charge method is called"""
		self.mega_man.charge()
		self.assertEqual(self.mega_man.battery, 100)

	def test_say_name(self):
		"""The robot should say "BEEP BOOP BEEP BOOP.  I AM MEGA MAN" and it's battery should decrease to 49"""
		self.assertEqual(self.mega_man.say_name(), 
			"BEEP BOOP BEEP BOOP.  I AM MEGA MAN")
		self.assertEqual(self.mega_man.battery, 49)

if __name__ == "__main__":
	unittest.main()
