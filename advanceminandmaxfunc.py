# advance min() and max()

# numbers = [1,2,4,5,7] print(min(numbers))
def func(item):
    return len(item)
names = ['Harshit', 'Mohit', 'ab']
print(max(names,key=func))
print(min(names,key=func))
students = {
    'ankit': {'score':90, 'age':19},
    'mohit': {'score':5, 'age':16},
    'rohit': {'score':76, 'age': 23}
}
print(max(students, key=lambda item: students[item]['score']))
print(max(students, key=lambda item: students[item]['age']))

students2 =[
     {'name': 'harshit', 'score':90, 'age':24},
     {'name': 'mohit', 'score':9, 'age':94},
     {'name':'rohit', 'score':98, 'age':34}
    ]
print(max(students2, key=lambda item:item.get("score")))
print(max(students2,key=lambda item:item.get("score"))['name'])
print(max(students2, key=lambda item:item.get("age")))
print(max(students2,key=lambda item:item.get("age"))['name'])


# or 
names = ['Harshit', 'Mohit', 'ab']
print(max(names,key=lambda item : len(item)))
print(min(names,key=lambda item : len(item)))