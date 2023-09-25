# Greatest Magnitude Exercise
# Write a function max_magnitude  that accepts a single list full of numbers. It should return the magnitude of the number with the largest magnitude (the number that is furthest away from zero).

# max_magnitude([300, 20, -900])   #900

# max_magnitude([10, 11, 12])   #12

# max_magnitude([-5, -1, -89])   #89

# Hint: use max and abs!

# Version 1 completed with for loop:
def max_magnitude(list1):
	list1_abs = []
	for l in list1:
		list1_abs.append(abs(l))
	return max(list1_abs)

# Version 2 completed with lambda
def max_magnitude(list1):
	return abs(max(list1, key=lambda l: abs(l)))

# Instructors version with list comprehension:
def max_magnitude(nums):
	return max(abs(num) for num in nums)