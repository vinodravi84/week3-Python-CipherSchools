#1.) generator function
# 10, print 1 to 10
def nums(n):
    for i in range(1,n+1):
        print(i)
nums(10)

def nums(n):
    for i in range(1,n+1):
        yield i # yeild is a keyword
print(nums(10))

def nums(n):
    for i in range(1,n+1):
        yield i # yeild is a keyword
for numbers in nums(10): # for loop is demanding the numbers from the generators
    print(numbers) # generator will not work unless someone demands for it like we deamded in the for loop

def nums(n):
    for i in range(1,n+1):
        yield i 
numbers=nums(10)
for num in numbers:
    print(num)
for num in numbers:
    print(num) 
    #generator only printing numbers once

def nums(n):
    for i in range(1,n+1):
        yield i 
numbers=list(nums(10)) # list will not give the benifit of generator 
for num in numbers:
    print(num)
for num in numbers:
    print(num)


