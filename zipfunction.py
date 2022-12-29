user=['user1','user2','user3']
names=['ankit','sachin','abc']
#('user1','ankit'),('user2','sachin')
print(zip(user,names)) 
print(list(zip(user,names)))

example=[('a',1),('b',2)]
# convert into dictionary
print(dict(example))


# class 160
li=[1,3,5,7]
l2=[2,4,6,8]
l=[(1,2),(3,4),(5,6),(7,8)]
# * operator with zip
print(zip(*l))
print(list(zip(*l)))
l1,l2=list(zip(*l))
print(l1)
print(l2)
print(list(l1))
print(list(l2))


li=[1,3,5,7]
l2=[2,4,6,8]
new_list=[]
#pair =[(1,2),(3,4),(5,6),(7,8)]
for pair in zip(l1,l2):
    new_list.append(max(pair))

print(new_list)