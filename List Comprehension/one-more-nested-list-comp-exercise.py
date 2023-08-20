# One More Nested List Comp Challenge

# Using list comprehension, create a variable called answer with the following value :
# [
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ]
# t's a 10x10 nested list.  10 rows, each row contains the numbers 0-9.
# Don't worry about the formatting/spacing, I just added a bunch of returns to make things clearer.
# Your answer will be all on one giant line. Use nested list comprehension and range() to accomplish this.

answer = [[num for num in range(0,10)] for num in range(0,10)]
print(answer)