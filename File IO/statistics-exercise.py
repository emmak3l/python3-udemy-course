# statistics

# Write a function called statistics, which takes in a file name and returns a
# dictionary with the number of lines, words, and characters in the file.

# (Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)

'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''

# First brute force solution:
# def statistics(text):
#     result = {'lines': 0, 'words': 0, 'characters': 0}

#     with open(text) as text:
#     	data = text.readlines()

#     words = 0
#     chars = 0
#     for d in data:
#     	words += len(d.split())
#     	chars += len(d)

#     result['lines'] = len(data)
#     result['words'] = words
#     result['characters'] = chars

#     return result


# Second more streamlined solution:
def statistics(file_name):
    with open(file_name) as file:
        text = file.readlines()
 
    return { "lines": len(text),
             "words": sum(len(t.split()) for t in text),
             "characters": sum(len(t) for t in text) }
