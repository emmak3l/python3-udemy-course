# Intro to unittest

# Unit Testing:
# - Test smallest parts of an application in isolation (e.g. units)
# - Good candidates for unit testing: individual classes, modules, or functions
# - Bad candidates for unit testing: an entire application, dependencies across several classes, or modules

# unittest:
# - Python comes with a built-in modules called unittest
# - You can write unit tests encapsulated as classes that inherit from unittest.TestCase
# - This inheritance gives you access to many assertion helpers that let you test the behavior of your functions
# - You can run tests by calling unittest.main()

import unittest
from activitiesut import eat, nap, is_funny, laugh

class ActivityTests(unittest.TestCase):
	def test_eat_healthy(self):
		"""eat should have a positive message for healthy eating"""
		self.assertEqual(
			eat("broccoli", is_healthy=True),
			"I'm eating broccoli, because my body is a temple"

			)
	def test_eat_unhealthy(self):
		"""eat should indicate you've given up for eating unhealthy"""
		self.assertEqual(
			eat("pizza", is_healthy=False),
			"I'm eating pizza, because YOLO!"

			)
	def test_eat_healthy_boolean(self):
		"""is_healthy must be a bool"""
		with self.assertRaises(ValueError):
			eat("pizza", is_healthy='who cares?')
	def test_short_nap(self):
		"""short naps should be refreshing"""
		self.assertEqual(
			nap(1),
			"I'm feeling refreshed after my 1 hour nap"
			)
	def test_long_nap(self):
		"""long naps should be discouraging"""
		self.assertEqual(
			nap(3),
			"Ugh I overslept. I didn't mean to nap for 3 hours!"
			)
	def test_is_funny_tim(self):
		self.assertEqual(is_funny("tim"), False) # this is checking for False
		# self.assertFalse(is_funny("tim"), "tim should not be funny") # this is checking for Falsy values, not just False
	def test_is_funny_anyone_else(self):
		"""anyone else but tim should be funny"""
		self.assertTrue(is_funny("blue"), "blue should be funny")
		self.assertTrue(is_funny("tammy"), "tammy should be funny")
		self.assertTrue(is_funny("sven"), "sven should be funny")
	def test_laugh(self):
		"""laugh should return one of the values in the tuple ('lol', 'haha', 'tehehe')"""
		self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))
		

if __name__ == "__main__":
	unittest.main()


# We can add a docstring(comments in triple quotes) to our test functions to get more info in terminal
# To see the comments we added, run the file like this:
# python3 NAME_OF_TEST_FILE.py -v


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Types of Assertions
# - self.assertEqual(x, y)
# - self.assertNotEqual(x, y)
# - self.assertTrue(x)
# - self.assertFalse(x)
# - self.assertIsNone(x)
# - self.assertIsNotNone(x)
# - self.assertIn(x, y)
# - self.assertNotIn(x, y)
# - and more...





