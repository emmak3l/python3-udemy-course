# More List Comprehension Exercises

# 1. Given two lists [1,2,3,4] and [3,4,5,6], create a variable called answer, 
# which is a new list that is the intersection of the two. Your output should be [3,4] .
# Hint: use the in  operator to test whether an element is in a list. 
# For example:  5 in [1,5,2]  is True.  3 in [1,5,2]  is False.

# 2. Given a list of words ["Elie", "Tim", "Matt"] create a variable called answer2,
# which is a new list with each word reversed and in lower case 
# (use a slice to do the reversal!) Your output should be ['eile', 'mit', 'ttam'] 
list1 = [1,2,3,4]
list2 = [3,4,5,6]

answer = [x for x in list1 if x in list2]
print(answer)


names = ["Elie", "Tim", "Matt"]

answer2 = [name[::-1].lower() for name in names]
print(answer2)
