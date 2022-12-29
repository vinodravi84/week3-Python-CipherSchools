#summary
d={'name':'ankit',"age":19}
#or
d1=dict(name='ankit', age=19)
#or
d2={
    'name':'ankit',
    'age':19,
}
print(d)
print(d1)
print(d2)

#how to acces data from the dic
#there is no order inside the dictionary
#we cannot use the indexing [0]
d1=dict(name='ankit', age=19)
print(d['name'])

#add data inside an empty dic
empty={}
empty['key1']='value1'
empty['key2']='value2'
print(empty)

#check existence of values inside dict
#if  'name' in d

#how to iterate(loop) in dic
#most common method
d={'name':'ankit',"age":19}
for key,value in d.items():
    print(f'key is {key} and value is {value}')


#to print all the keys
d={'name':'ankit',"age":19}
for i in d:
    print(i)

#to print all the values
d={'name':'ankit',"age":19}
for i in d.values():
    print(i)

#get method
d={'name':'ankit',"age":19}
print(d.get('name'))
#why we use get metthod
# to get rid of errors

d={'name':'ankit',"age":19}
#print(d['names']) it will show error
print(d.get("names")) #it will return none

# to detele
d={'name':'ankit',"age":19}
pop=d.pop('name')
print(d)

d={'name':'ankit',"age":19}
#popitem
popped=d.popitem()
print(d)
print(popped)