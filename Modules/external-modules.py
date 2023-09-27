# External Modules

# Built-in modules come with Python
# External modules are downloaded from the internet
# pypi.python.org/pypi <- the Python Package Index
# You can download external modules using 'pip'
# python3 -m pip install NAME_OF_PACKAGE

# We are going to install the package termcolor which allows us to change the colour of text in the terminal
# First we did 'pip install termcolor' in the terminal
# Now we can import it in this file and any other python file we want to use it it
import termcolor

# We can view the list of names in a package with the method 'dir', which isn't always helpful as it doesn't tell you what anything does
# print(dir(termcolor)) # ['ATTRIBUTES', 'COLORS', 'HIGHLIGHTS', 'RESET', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'annotations', 'colored', 'cprint', 'termcolor']

# There's another built in function 'help' which will show documentation for whatever object we pass in
# help(termcolor)

text = termcolor.colored("HI THERE!", color='blue', on_color="on_cyan")
#                                     ^changes text   ^changes background

print(text) 