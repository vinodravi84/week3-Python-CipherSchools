numbers=list(range(1,11))
#[1,2,3,4,5,6,7,,8,9,10]
#even numbers output
nums=[]
for i in numbers:
    if i%2==0:
        nums.append(i)
print(nums)

numbers=list(range(1,11))
even_nums=[i for i in numbers if i%2==0]
print(even_nums)

even_nums=[i for i in range(1,11) if i%2==0]
print(even_nums)

odd=[i for i in range(1,11) if i%2 != 0]
print(odd)