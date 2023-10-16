# Testing Memory Usage with Generators

# Below is a function that returns a list containing the fibbonaci numbers up to the place we specify
# We do not want to do this because lists use a lot of memory and will bog down our computer
# In the instructors example, his mac was using over 500mb of Real Memory Size to process fibbonaci to the 1000000th place

def fib_list(max):
	nums = []
	a, b = 0, 1
	while len(nums) < max:
		nums.append(b)
		a, b = b, a+b
	return nums

# A better way to do this would be to create a generator function instead, as it uses way less memory
# In the instructors example, is mac was only using 6.7mb of Real Memory size to process fibbonaci to the 1000000th place
# This is a stark difference to the list functions memory use!

def fib_gen(max):
	x = 0
	y = 1
	count = 0
	while cound < max:
		x, y = y, x + y
		yield x
		count += 1