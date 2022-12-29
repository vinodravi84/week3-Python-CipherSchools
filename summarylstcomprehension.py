square=[]
for i in range(1,11):
    square.append(i**2)
print(square)

square=[i**2 for i in range(1,11)]
print(square)

# if 
even=[i for i in range(1,11) if i%2==0]
print(even)

#if else 
odd_even=[i*2 if(i%2==0) else -i for i in range(1,11)]
print(odd_even)

#nested

new=[[ i for i in range(1,4)] for j in range(3)]
print(new)