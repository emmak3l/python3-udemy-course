# Doesn't have to be *args, it could be *nums instead but args is standard. The most important part is the * before
def sum_all_nums(*args):
	total = 0
	for num in args:
		total += num
	return total

print(sum_all_nums(4,6,9,4,10))

print(sum_all_nums(4,6))

def ensure_correct_info(*args):
	if "Colt" in args and "Steele" in args:
		return "Welcome back Colt!"

	return "Not sure who you are"

print(ensure_correct_info("hello", False, 78)) # Not sure who you are

print(ensure_correct_info(1, True, "Steele", "Colt")) # Welcome back Colt!