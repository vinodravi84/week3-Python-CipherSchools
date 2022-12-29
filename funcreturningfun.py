def square(a):
    return a**2
def outer_func():
    def inner_func():
        print("inside inner func")
    return inner_func
print(outer_func())
var=outer_func()
var()

def outer_func2(msg):
    def inner_func2():
        print(f"message is {msg}")
    return inner_func2
var=outer_func2('hi there')
var()

