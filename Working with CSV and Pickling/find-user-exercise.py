# find_user
# For this exercise, you'll be working with a file called users.csv
# Each row of data consists of two columns: a user's first name, and a user's last name.

# Implement the following function:

# find_user : Takes in a first name and a last name and searches for a user with that first and last name in the users.csv file.
# If the user is found, find_user  returns the index where the user is found. 
# Otherwise it returns a message stating that the user wasn't found.

'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''
from csv import reader

def find_user(first, last):
    with open('users.csv') as file:
        csv_reader = reader(file)
        for (index, row) in enumerate(csv_reader):
            first_match = first == row[0]
            last_match = last == row[1]
            if first_match and last_match:
                return index
        return f"{first} {last} not found."
