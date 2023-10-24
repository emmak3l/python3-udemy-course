# Writing to CSV Files: DictWriter (using dictionaries)

# DictWriter - creates a writer object for writing using dictionaries
# fieldnames - kwarg for the DictWriter specifying headers
# writeheader - method on a writer to write header row
# writerow - method on a writer to write a row based on a dictionary

from csv import DictWriter, DictReader

# with open("kitties.csv", "w") as file:
# 	headers = ['Name', 'Breed', 'Age']
# 	csv_writer = DictWriter(file, fieldnames=headers)
# 	csv_writer.writeheader()
# 	csv_writer.writerow({
# 		"Name": "Garfield",
# 		"Breed": "Orange Tabby",
# 		"Age": 10
# 		})

def cm_to_in(cm):
	return cm * 0.393701

with open("fighters.csv") as file:
	csv_reader = DictReader(file)
	fighters = list(csv_reader)

with open("inches_fighters.csv", 'w') as file:
	headers = ['Name', 'Country', 'Height']
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	for f in fighters:
		# we have to be more verbose here because we want to change the header 'Height (in cm)' to just 'Height'
		# if all the headers matched up, we could just write csv_writer.writerow(f)
		csv_writer.writerow({
			"Name": f["Name"],
			"Country": f["Country"],
			"Height": cm_to_in(float(f["Height (in cm)"])) # must convert to a float as the data will come in as a string
			})
