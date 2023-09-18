# compact
# Write a function called compact.
# This function accepts a list and returns a list of values that are truthy values, without any of the falsey values.

# compact([0,1,2,"",[], False, {}, None, "All done"])     # [1,2, "All done"]

'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(list1):
    return [item for item in list1 if item]

print(compact([0,1,2,"",[], False, {}, None, "All done"]))