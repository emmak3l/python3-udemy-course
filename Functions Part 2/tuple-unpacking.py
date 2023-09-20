def sum_all_nums(*args):
	total = 0
	for num in args:
		total += num
	return print(total)

# sum_all_nums(1,30,2,5,6) # 44

# You can pass the individual values of a list or a tuple into a function by adding a * beforehand, this is called unpacking
nums = [1,2,3,4,5,6]
sum_all_nums(*nums)