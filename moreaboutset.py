# i keyword in sets and for loop
s={'a','b','c'}
#to check if items is present or not
if 'a' in s:
    print(True)
else:
    print(False)


s={'a','b','c'}
# for loop
for item in s:
    print(item)


l=[1,2,2,3,4,5,6,6]
print(list(set(l)))

# sets in maths
s1={1,2,3,4}
s2={3,4,5,6}
#union
#intersection
union=s1|s2
print(union)
intersection=s1&s2
print(intersection)