# LAMBDA EXPRESSIONS (ANONYMOUS FUNCTION)
def add(a,b):
    return a+b
# or 
add2=lambda a,b : a+b
print(add2(2,3))
print(add)
print(add2)
# we do not assign lambda to the variable
# used in inbuilt, map,reduce, filter

# at  this means where it is loacted in our memory
#0x000001D45816D310>

multiply = lambda a,b : a*b
print(multiply(2,3))
