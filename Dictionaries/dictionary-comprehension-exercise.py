# Dictionary Comprehension Exercise

# Example 1
numbers = dict(first=1, second=2, third=3)

squared_numbers = {key: value ** 2 for key,value in numbers.items()}

print(squared_numbers)


# Example 2
{num: num**2 for num in [1,2,3,4,5]}


# Example 3
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0,len(str1))}
print(combo)


# Example 4
instructor = {'name': 'colt', 'city': 'san francisco', 'color': 'purple'}

yelling_instructor = {k.upper(): v.upper() for k,v in instructor.items()}

print(yelling_instructor)



# Conditional Logic with Dictionaries

# Example 5, conditional logic on values
num_list = [1,2,3,4]

num_dict = {num:('even' if num % 2 == 0 else 'odd') for num in num_list}

print(num_dict)


# Example 6, conitional logic on keys
instructor = {'name': 'colt', 'city': 'san francisco', 'color': 'purple'}

yelling_instructor = {(k.upper() if k is 'color' else k): v.upper() for k,v in instructor.items()}

print(yelling_instructor)
