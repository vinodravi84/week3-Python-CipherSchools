#we can create a list in one line
#create a list of squares from 1 to 10
squares=[]
for i in range(1,11):
    squares.append(i**2)
print(squares)

squares=[i**2 for i in range(1,11)]
print(squares)


neg=[]
for i in range(1,11):
    neg.append(-i)
print(neg)

neg=[-i for i in range(1,11)]
print(neg)

names=['Ankit','Prakash','Sachin']
new=[]
for name in names:
    new.append(name[0])
print(new)

names=['Ankit','Prakash','Sachin']
new=[name[0] for name in names]
print(new)