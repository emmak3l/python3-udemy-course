# print_users

# For this exercise, you'll be working with a file called users.csv
# Each row of data consists of two columns: a user's first name, and a user's last name.

# Implement the following function:

# print_users : prints out all of the first and last names in the users.csv file

'''
print_users() # None
# prints to the console:
# Colt Steele
'''
from csv import DictReader

def print_users():
    with open('users.csv') as file:
    	csv_reader = DictReader(file)
    	for user in csv_reader:
    		print(f"{user['First Name']} {user['Last Name']}")