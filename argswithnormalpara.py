def multiply(num,*args):
    mul=1
    print(num)
    print(*args)
    for i in args:
        mul *= i
    return mul
print(multiply(6,2,3))
# 6 is not a part of tuple

def multiply(*args):
    mul=1

    for i in args:
        mul *= i
    return mul
print(multiply(6,2,3))

def multiply(num1,num2,*args):
    mul=1
    print(num1)
    print(num2)
    print(*args)
   
    for i in args:
        mul *= i
    return mul
print(multiply(6,2,3,))

# lecture 145 args as argument in python
def multiply(*args):
    mul=1 
    print(args)# it will print as a tuple
    print(*args)# it will print the normal numbers
    for i in args:
        mul *= i
    return mul
print(multiply(6,2,3))

def multiply(*args):
    mul=1
    for i in args:
        mul *= i
    return mul
nums=[2,3,4]# it is the problem
print(multiply(nums))

# solution
def multiply(*args):
    mul=1
    for i in args:
        mul *= i
    return mul
nums=[2,3,4]# it is the problem
print(multiply(*nums))# add star to the list. it will unpack the list

def multiply(*args):
    mul=1
    print(args)
    print(*args)
    for i in args:
        mul *= i
    return mul
nums=(2,3,4)
print(multiply(*nums)) # * will unpack the tuple