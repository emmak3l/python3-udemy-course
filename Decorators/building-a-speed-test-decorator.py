# Building a Speed Test Decorator
from time import time
from functools import wraps

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums_gen():
	return sum(x for x in range(90000000))

@speed_test
def sum_nums_list():
	return sum([x for x in range(90000000)])

print(sum_nums_gen())
# ^ Executing sum_nums_gen
#   Time Elapsed: 4.3216588497161865
#   4049999955000000

print(sum_nums_list())
# ^ Executing sum_nums_list
#   Time Elapsed: 5.80743408203125
#   4049999955000000