# what are doc strings
# how to write docstring
# how to see docstring
# what is help function
 # doc string is a message we can give to the user to help the user to understand the function or the code
def add(a,b):
    ''' this fun take 2 numbers and return their sum '''
    return a+b
print(add.__doc__)    

# len , sum , min , max, sorted
print(len.__doc__)

print(sum.__doc__)

print(min.__doc__)

print(max.__doc__)

print(sorted.__doc__)

# help function
print(help(sum))