class Phone:

    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=max(price,0)
    
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class Smartphone:
    
    def __init__(self,brand,model,price,ram,memory,rear_camera):
        self.brand=brand
        self.model=model
        self.price=max(price,0)
        self.ram=ram
        self.memory=memory
        self.rear_camera=rear_camera
    
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")
        
    def full_name(self):
        return f"{self.brand} {self.model}"

p=Phone('Nokia','1100',1000)
s=Smartphone("OnePlus",'5',30000,'6 GB','64 GB', '20 MP')
print(p.full_name())
print(s.full_name())

class Phone: #base/parent class

    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=max(price,0)
    
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class Smartphone(Phone): #child/derived class
    
    def __init__(self,brand,model,price,ram,memory,rear_camera):
        #Phone.__init__(self,brand,model,price) #uncommon way
        super().__init__ (brand,model,price) #common way       
        self.ram=ram
        self.memory=memory
        self.rear_camera=rear_camera
    
 
p=Phone('Nokia','1100',1000)
s=Smartphone("OnePlus",'5',30000,'6 GB','64 GB', '20 MP')
print(p.full_name())
print(s.full_name())