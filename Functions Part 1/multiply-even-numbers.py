# multiply_even_numbers
# Write a function called multiply_even_numbers.
# This function accepts a list of numbers and returns the product of all even numbers in the list.

'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(list1):
    evens = [num for num in list1 if num % 2 == 0]
    result = 1
    for item in evens:
    	result = result * item   
    return result
