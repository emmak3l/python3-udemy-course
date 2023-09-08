# Sets Examples

# Sets are a collection of data that do not have duplicate values and the elements aren't ordered
# You cannot access items in a set by index
# Sets are useful for keeping track of a collection of elements if you don't care about ordering, keys or values, and want no duplicates

# Sets cannot have duplicates
set1 = set({1, 2, 3, 4, 5, 5, 5}) # returns {1, 2, 3, 4, 5}


# Creating a new set using set() function
s = set({1, 4, 5})


# Creating a set without the set() function

s = {1, 4, 5}

4 in s # returns True

8 in s # returns False


# You can access all values in a set using a for loop
nums = {1, 2, 3, 4}

for num in nums:
	print(num)
# 1
# 2
# 3
# 4
# (order not guaranteed though)


# You can convert a list to a set to eliminate duplicate values, and convert that back to a list
cities = ['Los Angeles', 'Boulder', 'Kyoto', 'Florence', 'Santiago', 'Los Angeles', 'Shanghai', 'Boulder', 'San Francisco', 'Oslo', 'Tokyo']
print(len(cities)) # 11

print(set(cities)) # {'Los Angeles', 'Boulder', 'Kyoto', 'Florence', 'Santiago', 'Shanghai', 'San Francisco', 'Oslo', 'Tokyo'}

print(list(set(cities))) # ['Los Angeles', 'Boulder', 'Kyoto', 'Florence', 'Santiago', 'Shanghai', 'San Francisco', 'Oslo', 'Tokyo']

print(len(list(set(cities)))) # 9

#------------------------------------------------------------------------------------------------------------------------------------------------

# Set Methods: Add (will NOT throw error if item is already in the set)
s = {1, 2, 3}

s.add(4)

print(s) # {1, 2, 3, 4}


# Set Methods: Remove (will throw error if item isn't in the set)
set2 = {1, 2, 3, 4, 5, 6}

set2.remove(3)

print(set2) # {1, 2, 4, 5, 6}


# Set Methods: Discard (will NOT throw error if the item isn't in the set, but will remove it if it is in the set)
set3 = {1, 2, 3, 4, 5, 6}

set3.discard(8) # no error

print(set3) # {1, 2, 3, 4, 5, 6}

set3.discard(5) # will remove 5

print(set3) # {1, 2, 3, 4, 6}


# Set Methods: Copy
s = set([1,2,3])

another_s = s.copy()

print(another_s) # {1,2,3}

another_s is s # False


# Set Methods: Clear
s = set([1,2,3])

s.clear()

print(s) # set()

#------------------------------------------------------------------------------------------------------------------------------------------------

# Set Math: set's have quite a few mathematical methods including intersection, symmetric_difference, and union

# Suppose you teach two classes:
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

# If you want a set of all your students without duplicate you can create a union like this
all_students = math_students | biology_students

print(all_students) # {"Matthew", "Helen", "Prashant", "James", "Aparna", "Jane", "Charlotte", "Mesut", "Oliver"}

# If you want a set of all students who are both in your math class and in your biology class you can intersect like this
both_classes = math_students & biology_students

print(both_classes) # {'James', 'Matthew'}
