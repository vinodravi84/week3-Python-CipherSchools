# map
def square(a):
    return a**2
l=[1,2,3,4,5]
print(list(map(square,l)))

def square(a):
    return a**2
l=[1,2,3,4,5]
def my_map(func, l):
    new=[]
    for item in l:
        new.append(func(item))
    return new
print(my_map(square,l))
print(my_map(lambda a:a**3,l))

