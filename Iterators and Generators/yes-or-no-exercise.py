# yes_or_no

# Write a function called yes_or_no, which returns a generator that first yields yes ,
# then no , then yes , then no , and so on.

'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''

def yes_or_no():
    word = "yes"
    while True:
    	yield word
    	if word == "yes":
    		word = "no"
    	else:
    		word = "yes"