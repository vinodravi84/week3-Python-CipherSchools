#set data type
# unordered  collection of unique items
s={1,2,3,2}
print(s)
# 1 item cannot be more than 1 times
# we cannot print like print(s[1])

l=[1,2,3,4,5,5,5,6,7,7,7]
#remove duplicate
s2=set(l)
print(s2)

l=[1,2,3,4,5,5,5,6,7,7,7]
#remove duplicate
s2=list(set(l))
print(s2)

# methods of sets
#add
s={1,2,3}
s.add(4)
s.add(5)
s.add(4)
print(s)

#remove method
s={1,2,3}
s.remove(3)
s.discard(5) # 5 is not in my set but by discard method it will not show any error
print(s)

s={1,2,3}
s.clear()
print(s)

#copy
s={1,2,3}
s1=s.copy()
print(s1)

#we cannot store lists and dic in the sets
s={1,1.0,2.3,'strings'}
print(s)