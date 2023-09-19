# **kwargs gathers remaining keyword arguments as a dictionary instead of a tuple
# Doesn't have to be **kwargs but it is standard to name the parameter such

def fav_colors(**kwargs):
	for person, color in kwargs.items():
		print(f"{person}'s favourite color is {color}")

fav_colors(colt='purple', ruby='red', ethel='teal')
fav_colors(colt='purple', ruby='red', ethel='teal', emma='violet', kevin='green')
fav_colors(colt='purple', ruby='red', ethel='teal', emma='violet', kevin='green', ted='blue', luke='pink')


def special_greeting(**kwargs):
	if "David" in kwargs and kwargs["David"] == "special":
		return "You get a special greeting David!"
	elif "David" in kwargs:
		return f"{kwargs['David']} David!"
	return "Not sure who this is..."

print(special_greeting(David='Hello')) # Hello David!
print(special_greeting(Bob='hello')) # Not sure who you are...
print(special_greeting(David='special')) # You get a special greeting David!
print(special_greeting(Heather='hello', David='special')) # You get a special greeting David!