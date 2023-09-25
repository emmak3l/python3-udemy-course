# extract_full_name
# Write a function called extract_full_name.
# This function should accept a list of dictionaries and return a new list of strings with the first and last name keys in each dictionary concatenated.

'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''

# My solution using list comprehension:
def extract_full_name(dict_list):
	return [dict_list[i]['first'] + ' ' + dict_list[i]['last'] for i in range(0,len(dict_list))]

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))

# Instructors solution using map and lambda: (better way)
def extract_full_name(l):
    return list(map(lambda val: f"{val['first']} {val['last']}", l))