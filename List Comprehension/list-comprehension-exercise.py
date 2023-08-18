# List Comprehension Exercise

# Given a list ["Elie", "Tim", "Matt"], create a variable called answer,
# which is a new list containing the first letter of each name in the list. 
# I would use a list comprehension, though you could also loop over manually.

# Given a list [1,2,3,4,5,6], create a new variable called answer2,
# which is a new list of all the even values. Another good candidate for a list comp.

list1 = ["Elie", "Tim", "Matt"]

list2 = [1,2,3,4,5,6]

answer = [x[0] for x in list1]

answer2 = [num for num in list2 if num % 2 == 0]