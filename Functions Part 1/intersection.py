# intersection
# Write a function called intersection.
# This function should accept two lists and return a list with the values that are in both input lists.

# intersection([1,2,3], [2,3,4])    #[2,3]
# intersection(['a','b','z'], ['x','y','z']) .  # ['z']

# flesh out intersection pleaseeeee
def intersection(list1, list2):
    return [x for x in list1 if x in list2]



# SLIGHTLY MORE EFFICIENT VERSION BELOW:

# Sets Solution
# This solution(submitted by Sebastian on the discussion boards) is the most efficient of the three.
# It converts the lists to sets, which removes duplicate values, and then finds the intersection of them using &.
# If you need review, watch the sets section again (it's super short).

# def intersection(list1, list2):
#     return [val for val in set(list1) & set(list2)]