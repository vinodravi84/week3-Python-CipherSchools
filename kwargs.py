#kwargs( keyword argument)
#**kwargs( double star operator)
# kwargs as a parameter
def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))
fun(first_name='ankit',last_name="singh")
# gather in dictionary

def fun(**kwargs):
    for k,v in kwargs.items():
        print(f'{k}:{v}')
fun(first_name='ankit',last_name="ankit")

def fun(name,**kwargs):
    for k,v in kwargs.items():
        print(f'{k}:{v}')
fun('athira',first_name='ankit',last_name="singh")

# dictionary unpacking
def fun(**kwargs):
    for k,v in kwargs.items():
        print(f'{k}:{v}')
d={'name':"Raunak","age":19}
fun(**d)