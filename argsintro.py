# MAKE FLEXIBLE FUNCTION
# *OPERATOR
# *ARGS
def total(a,b):
    return a+b
print(total(2,3)) # if we have to add 5 or more numbers so we use star operator

# *operator convert it into tuple
#u can write anything after * but most of the time args is written 
def total(*args):
    print(type(args))
total=(1,2,3,4,5)
print(total)

def total(*args):
    total=0
    for num in args:
        total +=num
    return total
print(total(1,2,3))