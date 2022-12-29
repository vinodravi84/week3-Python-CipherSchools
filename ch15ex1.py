# define generator function
# take one number as an argument
# generate a sequence of even numbers from 1 to that number
# 5 --> 2,4
# 7 --> 2,4,6
def even_generator(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
print(even_generator(20))
for num in even_generator(20):
    print(num)
for num in even_generator(15):
    print(num)


def even_generator(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
print(even_generator(20))
even_nums=even_generator(20)
for num in even_nums:
    print(num)
for num in even_nums: # it will not print
    print(num)


def even_generator(n):
    for i in range(2,n+1,2): # 2 is a step argument then we dont have to use the if n%2==0 line
       
            yield i
print(even_generator(20))
for num in even_generator(20):
    print(num)
for num in even_generator(15):
    print(num)


