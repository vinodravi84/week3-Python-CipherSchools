# instance methods or object method
l=[1,2,3]
l.pop() # class kai andae jitne bhi function hote hai nko hum method bolte hai        
class Person: #captital letter convention
    def __init__(self, first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return self.age>18
        
p1=Person('Isha','Verma',19)
p2=Person('Yatin','Arora',17)
print(p2.full_name())
print(p1.is_above_18())
print(p2.is_above_18())


l=[1,2,3]
#clear , pop
l.clear()
print(l)

l=[1,2,3]
list.clear(l)
print(l)
list.append(l,10)
print(l)