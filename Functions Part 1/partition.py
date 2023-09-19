# partition
# Write a function called partition. This function accepts a list and a callback function (which you can assume returns True  or False  ). 

# The function should iterate over each element in the list and invoke the callback function at each iteration. 

# If the result of the callback function is True , the element should go into the first list (i.e. the "truthy" list).
# If the result of the callback function is False , the element should go into the second list (i.e. the "falsy" list).
# When it's finished, partition should return both lists inside of one larger list, like so:

# [truthy_list, falsy_list] 

'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

def isEven(num):
    return num % 2 == 0

def partition(main_list, isEven):
    truthy_list = []
    falsy_list = []
    for num in main_list:
        if isEven(num):
            truthy_list.append(num)
        else:
            falsy_list.append(num)
    return [truthy_list, falsy_list]

print(partition([1,2,3,4], isEven))


# ALTERNATIVE VERSION BELOW:

# List Comprehension Version
# Using a list comprehension, you can get this function down to a single line.
# It's definitely a tradeoff though.  It's much short but also more difficult to understand.
# It's a fine balance between brevity and readability. 

# def partition(lst, fn):
#     return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]