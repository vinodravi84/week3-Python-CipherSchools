#paramters
# *args
# default parametrs
# **kwargs
# this is the sequence
# default
def func(name='unknown',age=19):
    print(name,age)
func('ankit',20)

def func(name='unknown',age=19):
    print(name)
    print(age)
func('ankit',20)

def func(name,*args,last_name='unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func("ankit",1,2,3,a=1,b=2)