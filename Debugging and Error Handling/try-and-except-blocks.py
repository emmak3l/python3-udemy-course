# Try and Except Blocks

# In Python, it is strongly encouraged to use try/except blocks,
# to catch exceptions when we can do something about them

# Example 1:
try:
	foobar
except NameError as err:
	print(err) # name 'foobar' is not defined
print("after the try")


# You don't want to catch all errors with a blank except like in the next example
# Example 2:
try:
	colt
except:
	print("You tried to use a variable that was never declared!")

# ^ What we are doing here is catching every error, which means we are not able to correctly identify "what" went wrong
# It is highly discouraged to do this.


# Example 3:
# This is better because it is more explicit
try:
	colt
except NameError:
	print("You tried to use a variable that was never declared!")


# Example 4:
d = {"name": "Ricky"}
d["city"] # KeyError

def get(d,key):
	try:
	    return d[key]
	except KeyError:
		return None

print(get(d, "name")) # Ricky
print(get(d, "city")) # None



# Try, Except, Else and Finally

# Example 1:

while True:
    try:
	    num = int(input("Please enter a number: "))
    except ValueError: # except will run if there is a problem
	    print("That's not a number!")
    else: # else will run when except does not run
	    print("Good job, you entered a number!")
	    break
    finally: # finally will run no matter what, even after the loop breaks
	    print("RUNS NO MATTER WHAT")
print("REST OF GAME LOGIC")


# Example 2:
def divide(a,b):
	try:
		result = a / b
	except ZeroDivisionError as err:
		print("don't divide by zero please!")
		print(err)
	except TypeError as err:
		print("a and b must be ints or floats")
		print(err)
	else:
		print(f"{a} divided by {b} is {result}")

