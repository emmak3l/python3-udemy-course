# Generator Expressions
import time

# You can also create generators from generator expressions
# Generator expressions look a lot like list comprehensions but they use () instead of []

# Using a generator function
def nums():
	for num in range(1,10):
		yield num

# Using a generator expression to do the same thing
g = (num for num in range(1,10))


# Below is a demonstration of the time different between using a list comprehension versus a generator expression
# This is why we imported time at the top of the file, for use in this example

gen_start_time = time.time()
print(sum(n for n in range(100000000)))
gen_duration = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_duration = time.time() - list_start_time

print(f"sum(n for n in range(100000000)) took: {gen_duration}") # sum(n for n in range(10000000)) took: 4.645614147186279
print(f"sum([n for n in range(100000000)]) took: {list_duration}") # sum([n for n in range(10000000)]) took: 6.019468069076538

# Almost a 2 second difference in speed!