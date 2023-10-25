# update_users

# For this exercise, you'll be working with a file called users.csv
# Each row of data consists of two columns: a user's first name, and a user's last name.

# Implement the following function:

# update_users :
# Takes in an old first name, an old last name, a new first name, and a new last name.
# Updates the users.csv file so that any user whose first and last names match the old first and last names are updated to the new first and last names.
# The function should return a count of how many users were updated.

'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''

# My brute force overly complicated solution:

from csv import reader, writer

def update_users(old_first, old_last, new_first, new_last):
    with open('users.csv') as file:
        csv_reader = reader(file)
        users_list = list(csv_reader)
        if [old_first, old_last] in users_list:
            count = users_list.count([old_first, old_last])
            index = users_list.index([old_first, old_last])
            users_list[index] = [new_first, new_last]
            if count > 1:
                index2 = users_list.index([old_first, old_last], index+1)
                users_list[index2] = [new_first, new_last]
            with open('users.csv', 'w') as file:
                csv_writer = writer(file)
                for user in users_list:
                    csv_writer.writerow(user)
            return f"Users updated: {count}."
        else:
            count = 0
            return f"Users updated: {count}."

# update_users("Grace", "Hopper", "Hello", "World")
# update_users("Colt", "Steele", "Boba", "Fett")
# update_users("Not", "Here", "Still not", "Here")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Instructors Solution:

# import csv
 
# def update_users(old_first, old_last, new_first, new_last):
#     with open("users.csv") as csvfile:
#         csv_reader = csv.reader(csvfile)
#         rows = list(csv_reader)
 
#     count = 0
#     with open("users.csv", "w") as csvfile:
#         csv_writer = csv.writer(csvfile)
#         for row in rows:
#             if row[0] == old_first and row[1] == old_last:
#                 csv_writer.writerow([new_first, new_last])
#                 count += 1
#             else:
#                 csv_writer.writerow(row)
 
#     return f"Users updated: {count}."


