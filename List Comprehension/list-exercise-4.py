# List Exercise 4

# Given the string "amazing", create a variable called answer, 
# which is a list containing all the letters from "amazing" 
# but not the vowels (a, e, i, o, and u).  
# The answer should look like: ['m', 'z', 'n', 'g'].

answer = [l for l in "amazing" if l not in 'aeiou']
print(answer)