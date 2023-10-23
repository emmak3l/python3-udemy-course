# Reading CSV Files

# Python had a module (csv) that helps us read in CSV data
# The module has a few different methods we can use to read in the data
from csv import reader, DictReader


# reading data in using reader() method
# reader() creates a list for each row of data in the CSV file
# with open("fighters.csv") as file:
# 	csv_reader = reader(file) # creates a csv_reader object, which is an iterator
# 	for row in csv_reader:
# 		print(row) # each row is a list
# 		# ^
# 		# ['Name', 'Country', 'Height (in cm)']
# 		# ['Ryu', 'Japan', '175']
# 		# ['Ken', 'USA', '175']
# 		# ['Chun-Li', 'China', '165']
# 		# ['Guile', 'USA', '182']
# 		# ['E. Honda', 'Japan', '185']
# 		# ['Dhalsim', 'India', '176']
# 		# ['Blanka', 'Brazil', '192']
# 		# ['Zangief', 'Russia', '214']

# with open("fighters.csv") as file:
# 	csv_reader = reader(file)
# 	next(csv_reader) # Because csv_reader is an iterator, we can skip the first row (the headers) by using the next keyword
# 	for fighter in csv_reader:
# 		print(f'{fighter[0]} is from {fighter[1]}') # {Name} is from {Country}
# 		# ^
# 		# Ryu is from Japan
# 		# Ken is from USA
# 		# Chun-Li is from China
# 		# Guile is from USA
# 		# E. Honda is from Japan
# 		# Dhalsim is from India
# 		# Blanka is from Brazil
# 		# Zangief is from Russia


# reading data using DictReader() method
# DictReader() creates an OrderedDict for each row of data in the CSV file
# The reason it's an OrderedDict is that the keys are always in the same order
# In the below example, 'Name' comes first, then 'Country', then 'Height (in cm)'
# The keys are set up to be the headers automatically

# with open('fighters.csv') as file:
# 	csv_reader = DictReader(file) # creates a csv.DictReader object, which is an iterator
# 	for row in csv_reader:
# 		print(row) # each row is an OrderedDict (says class 'dict' when I used the type() method)
# 		# ^
# 		# {'Name': 'Ryu', 'Country': 'Japan', 'Height (in cm)': '175'}
# 		# {'Name': 'Ken', 'Country': 'USA', 'Height (in cm)': '175'}
# 		# {'Name': 'Chun-Li', 'Country': 'China', 'Height (in cm)': '165'}
# 		# {'Name': 'Guile', 'Country': 'USA', 'Height (in cm)': '182'}
# 		# {'Name': 'E. Honda', 'Country': 'Japan', 'Height (in cm)': '185'}
# 		# {'Name': 'Dhalsim', 'Country': 'India', 'Height (in cm)': '176'}
# 		# {'Name': 'Blanka', 'Country': 'Brazil', 'Height (in cm)': '192'}
# 		# {'Name': 'Zangief', 'Country': 'Russia', 'Height (in cm)': '214'}

with open('fighters.csv') as file:
	csv_reader = DictReader(file)
	for row in csv_reader:
		print(row['Name'])
		# ^
		# Ryu
		# Ken
		# Chun-Li
		# Guile
		# E. Honda
		# Dhalsim
		# Blanka
		# Zangief


# Other Delimiters:
# Readers accept a delimiter kwarg in case your data isn't separated by commas,
# as long as they're separated by the same character

# Example:
# from csv import reader
# with open('example.csv') as file:
# 	csv_reader = reader(file, delimiter='|')
# 	for row in csv_reader:
# 		print(row)



