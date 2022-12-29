# define a function that take list of strings
# list containing reverse of every string
# NOTE - USE LIST COMPREHENSION because we already did this exercise
# using normal method
# example

# 1 = ['abc', 'tuv', 'xyz'] 
# reverse_string(11) -> ['bac', 'vut', 'zyx']

def reverse_strings(l):
    return[name[::-1] for name in l]
print(reverse_strings(['abc','tuv']))

def strings(l):
    new=[]
    for i in l:
        new.append(i[::-1])
    return new 
print(strings(['abc','tuv']))