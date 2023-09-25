# triple_and_filter
# Write a function called triple_and_filter.
# This function should accept a list of numbers,
# filter out every number that is not divisible by 4,
# and return a new list where every remaining number is tripled.

'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(list1):
    return [(num*3) for num in list1 if num % 4 == 0]

print(triple_and_filter([1,2,3,4]))
print(triple_and_filter([6,8,10,12]))