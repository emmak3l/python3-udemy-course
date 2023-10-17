# Enforcing Arguement Types with a Decorator

def enforce(*types):
	def decorator(fn):
		def new_func(*args, **kwargs):
			# convert args into something mutable
			newargs = []
			for (a, t) in zip(args, types):
				newargs.append(t(a)) # feel free to have more elaboration here
			return fn(*newargs, **kwargs)
		return new_func
	return decorator

@enforce(str, int)
def repeat_msg(msg, times):
	for time in range(times):
		print(msg)

@enforce(float, float)
def divide(a,b):
	print(a/b)

repeat_msg("hello", '3')
divide(8,2)
divide('10', '5.0')