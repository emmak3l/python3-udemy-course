# any and all

# all:
# returns True is all elements of the iterable are truthy (or if the iterable is empty)

# Examples 1:
all([0,1,2,3]) # False

all([char for char in 'eio' if char in 'aeiou']) # True

all([num for num in [4,2,10,6,8] if num % 2 == 0]) # True


# Example 2:
people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Cristina']

all([name[0] == 'C' for name in people]) # True

people2 = ['Charlie', 'Casey', 'Cody', 'Carly', 'Cristina', 'Kristy']

all([name[0] == 'C' for name in people2]) # False


# Example 3:
nums = [2,60,26,18]

all([num % 2 == 0 for num in nums]) # True

nums2 = [2,60,26,18,21]

all([num % 2 == 0 for num in nums2]) # False



# any:
# returns True if any element of the iterable is truthy. If the iterable is empty, it returns False

# Examples 1:
any([0,1,2,3]) # True

any([val for val in [1,2,3] if val > 2]) # True

any([val for val in [1,2,3] if val > 5]) # False

# Example 2:
any([num % 2 == 1 for num in nums2]) # True

any([num % 2 == 0 for num in nums2]) # True



# Generator Expressions and Using sys.getsizeof

# You don't need to add the list brackets []
all(name[0] == 'C' for name in people2) # False

# Running this on it's own is called a Generator Expression
# It's like a lighter weight version of a list, but you can't use any list methods with them (i.e. .append(), .extend() etc)
# Saves space and memory, and since we don't actually need to save this data in a list we only want to know whether it's True or False it makes sense to use a generator expression
# General rule of thumb is if you only need to iterate over it once, use a generator expression
# If you need to store it in a variable and iterate over it multiple times use a list comprehension
(name[0] == 'C' for name in people2) 


# Example that shows the difference in byte size between a generator expression and a list comprehension:
import sys
list_comp = sys.getsizeof(([x * 10 for x in range(1000)]))
gen_exp = sys.getsizeof((x * 10 for x in range(1000)))

print("To do the same thing, it takes...")
print(f"List comprehension: {list_comp} bytes") # 8856 bytes
print(f"Generator Expression: {gen_exp} bytes") # 208 bytes
