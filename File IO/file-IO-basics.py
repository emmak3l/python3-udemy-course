# File I/O Basics

# You can read a file into your python program by using the open() method
# # Example:
# file = open('hello.txt')

# You can read the entire contents of a file using the read() method
# print(file.read())
# ^
# Hello, this is a new text file.
# Using this to demonstrate file I/O.
# It is pretty short.



# Python reads files with the cursor.
# When you read a file, the cursor remains at the end of the file until you reset it.
# You can reset the cursor to any index location using the seek() method

# print(file.read()) # prints a blank new line because the cursor is at the end

# file.seek(0) # resets the cursor to the beginning of the file

# print(file.read()) # prints the whole text file from the beginning again


# You can read single lines of a file using the readline() method

# file.seek(0)

# print(file.readline()) # Hello, this is a new text file.

# print(file.readline()) # Using this to demonstrate file I/O.

# print(file.readline()) # It is pretty short.



# You can read the contents of a file and save each line as a
# separate string in a list using the readlines() method.
# The read() method on the other hand combines all separate lines into a single string.
# The readlines() method preserves the structure of the file as separate lines.

# file.seek(0)

# file_list = file.readlines()

# print(file_list) # ['Hello, this is a new text file.\n', 'Using this to demonstrate file I/O.\n', 'It is pretty short.']



# If you open files manually, you have to remember to close them when you're done.
# If you don't close the file and it's updated, you'll see the updates when you read again.
# You can check whether a file is closed or not by using the closed() method
# Once you have closed a file you cannot read it anymore with the read(), readline(), or readlines() methods

# file.closed() # False

# file.close() # closes the file

# file.closed() # True



# A better way to open files is using the with arguement
# This will automatically close the file once it is finished

# with open('hello.txt') as file:
# 	print(file.read()) # reads the whole text file

# file.closed() # True



# You can also write to files using the open() method and the write() method
# To do so, you have to pass in 'w' as the second arguement
# When using 'w' it will completely overwrite what was existing in the file

# with open('hello.txt', 'w') as file:
# 	file.write("This is new text I'm writing to the file")

# with open('hello.txt') as file:
# 	print(file.read()) # "This is new text I'm writing to the file"



# You can also create a new text file that doesn't exist using 'w'

# with open('new.txt', 'w') as new_file:
# 	new_file.write("Writing files is great\n")
# 	new_file.write("Here's another line of text\n")
# 	new_file.write("Closing now, goodbye!\n")

# with open('new.txt') as new_file:
# 	print(new_file.read())
	# ^
	# Writing files is great
	# Here's another line of text
	# Closing now, goodbye!



# If you want to append to the end of a file you can use the 'a' arguements
# You can't use this to create a new file
# You also can't write to any other index position of the file other than the end

# with open('new.txt', 'a') as new_file:
# 	new_file.write("Here's one more haiku\n")
# 	new_file.write("What about the older one?\n")
# 	new_file.write("Let's go check it out!\n")

# with open('new.txt') as new_file:
# 	print(new_file.read())
	# ^
	# Writing files is great
	# Here's another line of text
	# Closing now, goodbye!
	# Here's one more haiku
	# What about the older one?
	# Let's go check it out!



# If you want to write to a different index position you can use the 'r+' arguement
# It will refault to writing at the beginning of the file
# It will also overwrite the original file to insert you new write()

with open('new.txt', 'r+') as new_file:
	new_file.write("Here's one more haiku\n")
	new_file.write("What about the older one?\n")
	new_file.write("Let's go check it out!\n")

with open('new.txt') as new_file:
	print(new_file.read())
	# ^
	# Here's one more haiku
	# What about the older one?
	# Let's go check it out!
	# !
	# Here's one more haiku
	# What about the older one?
	# Let's go check it out!


