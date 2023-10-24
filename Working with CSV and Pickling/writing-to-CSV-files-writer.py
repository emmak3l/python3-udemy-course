# Writing CSV Files: Using Lists

# Python had a module (csv) that helps us write CSV data called writer
# The module has a few different methods we can use to read in the data

# writer creates a writer object for writing to CSV
# writerow() - on a writer to write a row to the CSV file
from csv import writer, reader

# with open('cats.csv', 'w') as file:
# 	csv_writer = writer(file)
# 	csv_writer.writerow(['Name', 'Age'])
# 	csv_writer.writerow(['Blue', 4])
# 	csv_writer.writerow(['Kitty', 1])


# This approach opens 1 file at a time:

# with open('fighters.csv') as file:
# 	csv_reader = reader(file)
# data is converted to a list and saved to a variable
# 	fighters = [[s.upper() for s in row] for row in csv_reader]

# with open('screaming_fighters.csv', 'w') as file:
# 	csv_writer = writer(file)
# 	for fighter in fighters:
# 		csv_writer.writerow(fighter)


# we could nest both the read and the write with statements too like this:

with open('fighters.csv') as file:
	csv_reader = reader(file) # data is never converted to a list

	with open('screaming_fighters.csv', 'w') as file:
		csv_writer = writer(file)
		for fighter in csv_reader:
			csv_writer.writerow([s.upper() for s in fighter])