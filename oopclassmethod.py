#class method
# not that much useful
class Person:
    count_instance=0  #classs variable / class attribute
    def __init__(self, first_name,last_name,age):
        Person.count_instance +=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
    @classmethod
    def count_instances(cls):
        return f" you have created {cls.count_instance} instances of person class"
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return self.age>18

p1=Person("Isha",'Verma',19)
p2=Person("abc",'abc',19)
#Person.method_name()
#"you have created 4 instances of person class"
print(Person.count_instances())

