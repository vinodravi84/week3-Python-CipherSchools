from functools import wraps

def decorator(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        '''this is wrapper function'''
        print("this is awesome functional") 
        any_function(*args,**kwargs)
    return wrapper_function
@decorator
def add(a,b):
    '''this is add functional'''
    return a+b
print(add.__doc__)
print(add.__name__)

def decorator(any_function):

    def wrapper_function(*args,**kwargs):
        '''this is wrapper function'''
        print("this is awesome functional") 
        any_function(*args,**kwargs)
    return wrapper_function
@decorator
def add(a,b):
    '''this is add functional'''
    return a+b
print(add.__doc__)
print(add.__name__)


# class 174
from functools import wraps
def print_function_data(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f"you are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper
        


@print_function_data
def add(a,b):
    '''This function takes two numbers as arguments and return their sum''' 
    return a+b
print(add(4,5))

# output
# you are calling add function
#This function takes two numbers as parameters and return their sum
#9

