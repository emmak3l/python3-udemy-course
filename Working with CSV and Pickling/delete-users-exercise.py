# delete_users

# For this exercise, you'll be working with a file called users.csv
# Each row of data consists of two columns: a user's first name, and a user's last name.

# Implement the following function:

# delete_users : Takes in a first name and a last name.
# Updates the users.csv file so that any user whose first and last names match the inputs are removed.
# The function should return a count of how many users were removed.

'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

# My solution:

from csv import reader, writer

def delete_users(user_first, user_last):
    with open("users.csv") as file:
        csv_reader = reader(file)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as file:
        csv_writer = writer(file)
        for row in rows:
            if row[0] == user_first and row[1] == user_last:
                count += 1
            else:
                csv_writer.writerow(row)
 
    return f"Users deleted: {count}."


# Instructors example is identical except for the names of the variables