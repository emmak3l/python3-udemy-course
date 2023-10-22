# copy_and_reverse

# Write a function called copy_and_reverse, which takes in a file name and a new file name
# and copies the reversed contents of the first file to the second file.

# (Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)

'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''

def copy_and_reverse(text1, text2):
    with open(text1) as story:
        data = story.read()
        
    with open(text2, 'w') as copy:
        copy.write(data[::-1])