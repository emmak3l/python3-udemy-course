# Custom For Loop 

def my_for(iterable):
	iterator = iter(iterable)
	while True:
		try:
			next(iterator)
		except StopIteration:
			break


my_for("lol", print)