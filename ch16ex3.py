class Person:
    count_instance=0
    def __init__(self, first_name,last_name,age):
        Person.count_instance +=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

p1=Person("Isha",'Verma',19)
p2=Person("abc",'abc',19) # there are 2 object p1 and p2 ths is a object counter
print(Person.count_instance)