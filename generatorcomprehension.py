square=[i**2 for i in range(1,11)]
# first what we have to append 
# then the range
print(square)

square=(i**2 for i in range(1,11)) # insted of [] we have to use ()
print(square)

square=(i**2 for i in range(1,11))
for num in square:
    print(num)
for num in square:
    print(num)


