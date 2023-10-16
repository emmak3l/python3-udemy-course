# Making a Beat Making Generator

def current_beat():
	beat = 1
	while True:
		yield beat
		if beat < 4:
			beat += 1
		else:
			beat = 1

b = current_beat()

print(next(b)) # 1
print(next(b)) # 2
print(next(b)) # 3
print(next(b)) # 4
print(next(b)) # 1
print(next(b)) # 2
print(next(b)) # 3
print(next(b)) # 4
print(next(b)) # 1
print(next(b)) # 2
print(next(b)) # 3
print(next(b)) # 4