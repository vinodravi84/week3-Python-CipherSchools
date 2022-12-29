class Person:
    count_instance=0  #classs variable / class attribute
    def __init__(self, first_name,last_name,age):
        Person.count_instance +=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
    @classmethod
    def from_str(cls,string):
        first,last,age=string.split(",")
        return cls(first,last,age)
        
    @classmethod
    def count_instances(cls):
        return f" you have created {cls.count_instance} instances of person class"
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return self.age>18

p1=Person("Ankit",'singh',19)
p2=Person("abc",'adc',19)
p3=Person.from_str("Aman,ABC,17")
print(p3.full_name())


# class 198 
# OOP STATIC METHOD 
class Person:
    count_instance=0  #classs variable / class attribute
    def __init__(self, first_name,last_name,age):
        Person.count_instance +=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
    @classmethod
    def from_str(cls,string):
        first,last,age=string.split(",")
        return cls(first,last,age)
        
    @classmethod
    def count_instances(cls):
        return f" you have created {cls.count_instance} instances of person class"
    
    
    @staticmethod
    def hello():
        print("hello, static method called")
        
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

p1=Person("Akit",'Singh',19)
p2=Person("abc",'dcv',19)