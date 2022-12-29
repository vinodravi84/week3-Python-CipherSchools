# decorators - enhance the functionality of other functions

def decorator(any_function):
    def wrapper_function():
        print("this is awesome functional") # pehle yeh line aygi
        any_function()# phir yeh fucntion call hoga
    return wrapper_function
    
# this is awesome function
@decorator
def func1():
    print("this is function 1")
func1()
#this is awesome function
@decorator
def func2():
    print("this is function 2")
func2()
    
    
#func1=decorator(func1)
#func1()

#class 172
def decorator(any_function):
    def wrapper_function():
        print("this is awesome functional") 
        any_function()
    return wrapper_function


#@decorator # we cannot use it
def func(a):
    print(f"this is a function with argument {a}")
func(7)

def decorator(any_function):
    def wrapper_function(*args,**kwargs):
        print("this is awesome functional") 
        any_function(*args,**kwargs)
    return wrapper_function


@decorator
def func(a):
    print(f"this is a function with argument {a}")
func(7)

@decorator
def add(a,b):
    return a + b
print(add(2,3)) # we cannot get the output first we have to return the any_function


def decorator(any_function):
    def wrapper_function(*args,**kwargs):
        print("this is awesome functional") 
        return any_function(*args,**kwargs)
    return wrapper_function


@decorator
def func(a):
    print(f"this is a function with argument {a}")
func(7)

@decorator
def add(a,b):
    return a + b
print(add(2,3))