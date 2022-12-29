
num=[1,2,3,4]
def square(a):
    return a**2
[square(1),square(2)]
#map function
num=[1,2,3,4]
def square(a):
    return a**2
print(map(square, num))

num=[1,2,3,4]
def square(a):
    return a**2
square=list(map(square,num))
print(square)

num=[1,2,3,4]
square=list(map(lambda a:a**2,num))
print(square)

# list comp
num=[1,2,3,4]
square=[i**2 for i in num]
print(square)

numbers=[1,2,3,4]
l=[]
for num in numbers:
    l.append(num**2)
print(l)

names=['abc','abcd','abcde']
length=map(len,names)
for i in length:
    print(i)
for j in names:
    print(j)

