# zip basics

# Makes an iterator that aggregates elements from each of the iterables
# Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables
# The iterator stops when the shortest input iterable is exhausted
# Goes from left to right

# Image we have two lists of numbers that are the same length.
# zip will make a new list where the first elements of each of the two lists are paired together


# Example 1:
first_zip = zip([1,2,3], [4,5,6]) # zip object at ___________

list(first_zip) # [(1, 4), (2, 5), (3, 6)]

dict(first_zip) # {1: 4, 2: 5, 3: 6}


# Example 2:
# The lists don't have to be the exact same length
nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10,11,12]

list(zip(nums1, nums2)) # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)] it stops as soon as the shortest iterable is exhausted


# Example 3:
words = ['hi', 'lol', 'haha', ':)']
list(zip(words,nums1,nums2)) # [('hi', 1, 6), ('lol', 2, 7), ('haha', 3, 8), (':)', 4, 9)]


# Example 4:
# You can use the * operator to unpack a zipped list
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

list(zip(*five_by_two)) # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]



# more complex zip examples

# Example 5:
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# Make a dict that shows the student and their highest score
# First version using list comprehension first:
highest_grades = [max(pair) for pair in zip(midterms, finals)]

final_grades = dict(zip(students, highest_grades))

print(final_grades)

# Second version going straight to dict using dict comprehension:
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}

print(final_grades)

# Third version using lambda and map:
final_grades = zip(students, map(lambda pair: max(pair), zip(midterms, finals)))

print(dict(final_grades))

# Make a dict that shows the student and their average grade:
avg_grades = zip(students, map(lambda pair: ((pair[0]+pair[1])/2), zip(midterms, finals)))

print(dict(avg_grades))
