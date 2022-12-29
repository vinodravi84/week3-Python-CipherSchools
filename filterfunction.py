def even(a):
    return a%2==0
num=[3,4,5,6,78,9,10]
print(filter(even,num))


def even(a):
    return a%2==0
num=[3,4,5,6,78,9,10]
evens=tuple(filter(even,num))
print(evens)

def even(a):
    return a%2==0
num=[3,4,5,6,78,9,10]
evens=tuple(filter(lambda a:a%2==0 ,num))