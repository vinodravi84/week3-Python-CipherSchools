#ENCAPSULATION ---> wrapping of data under a single unit

#ABSTRACTION ---> hiding the internal details(complexity to the user)

#SOME SPECIAL NAMING CONVENTION ---> # _name ----. convention to tell other user this is a private method dont change it


#NAME MANGLING--> __name(not a convention)
class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        
    def make_a_call(self,phone_no):
        print(f"calling{phone_no}...")
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def send_message(self):
        pass #twilio
p1=Phone('nokia','1100',1000)
print(p1.price)
p1.price=-1000
print(p1.price)
# _name ----. convention to tell other user this is a private method dont change it 
#__name__ --> dunder/ magic method    
l=[5,3,5,2,1]
l.sort() #tim sort
print(l)


#name mangling 
class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.__price=price
        
    def make_a_call(self,phone_no):
        print(f"calling{phone_no}...")
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def send_message(self):
        pass #twilio
p1=Phone('nokia','1100',1000)
#print(p1.__price) #thi will show error

print(p1.__dict__)
print(p1._Phone__price)