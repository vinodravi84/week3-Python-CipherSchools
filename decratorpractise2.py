def add_all(*args):
    total=0
    for i in args:
        total += i
    return total
print(add_all(1,2,3,4,5))

def add_all(*args):
    total=0
    for i in args:
        total += i
    return total
print(add_all(1,2,3,4,5,[1,2,3])) # this will show a problem and to solve this we need to use the decorators

# only_int_allow
from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        data_types=[]
        for arg in args:
            data_types.append(type(arg)==int)
        if all(data_types):
            return function(*args,**kwargs)
        else:
            print("Invalid arguments")
    return wrapper        
@only_int_allow  
def add_all(*args):
    total=0
    for i in args:
        total += i
    return total
print(add_all(1,2,3,4,5,[1,2,3]))
            

from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        if all([type(arg)==int for arg in args]):
            return function(*args,**kwargs)
        print("invalid arguments")

    return wrapper        
@only_int_allow  
def add_all(*args):
    total=0
    for i in args:
        total += i
    return total
print(add_all(1,2,3,4,5,[1,2,3]))