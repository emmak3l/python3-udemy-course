# Generators

# - Generators are iterators
# - Generators can be created with generator functions
# - Generator functions use the yield keyword
# - Generators can be created with generator expressions

# - Generators use the yield keyword instead of the return keyword of normal functions
# - Generators can yield multiple times
# - When invoked, it returns a generator, instead of a value like a normal function does

# Generator function
def count_up_to(max):
	count = 1
	while count <= max:
		yield count
		count +=1

# Generator
print(count_up_to(5)) # <generator object count_up_to at 0x10825b510>

counter = count_up_to(5)

# We need to manually call next on the generator to yield the results
print(next(counter)) # 1
print(next(counter)) # 2
print(next(counter)) # 3
print(next(counter)) # 4
print(next(counter)) # 5
# print(next(counter)) # StopIteration

# What's different about generators compared to other functions is they remember what place they're in
counter2 = count_up_to(10)

print(next(counter2)) # 1

# We can also iterate through a generator using a for loop
for num in counter2:
	print(num)
# Because we already called next on counter2 before the for loop, the for loop starts at 2, because the generator remembers its place
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10