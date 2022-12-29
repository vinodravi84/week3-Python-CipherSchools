# circle variable
# circle
# area
# circumference
class Circle:
    def __init__(self,radius,pi):
        self.radius=radius
        self.pi=pi
    def calc_cicum(self): # self represent object
        return 2**self.pi*self.radius
c=Circle(4,3.14)
c2=Circle(5,3.14)
print(c.calc_cicum())

class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        
    def calc_cicum(self): # self represent object
        return 2**Circle.pi*self.radius
    
c=Circle(4)
print(c.calc_cicum())

# class 193
# sale khatam abb 0 krna hai
class Laptop:
    discont_percent =10
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        
    def apply_discount(self):
        off_price=(Laptop.discont_percent/100)*self.price
        return self.price - off_price
        
Laptop.discount_percent=0        
l1=Laptop('Dell','Inspiron',50000)
l2=Laptop('HP','i7',90000)
print(l1.apply_discount())

# print dictionary
class Laptop:
    discont_percent =10
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        
    def apply_discount(self):
        off_price=(Laptop.discont_percent/100)*self.price
        return self.price - off_price
        
Laptop.discount_percent=0        
l1=Laptop('Dell','Inspiron',50000)
l2=Laptop('HP','i7',90000)
print(l1.__dict__)

class Laptop:
    discont_percent =10
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        
    def apply_discount(self):
        off_price=(Laptop.discont_percent/100)*self.price
        return self.price - off_price
        
Laptop.discont_percent=50    # but 10 percent is coming in outcome 
l1=Laptop('Dell','Inspiron',50000)
l2=Laptop('HP','i7',90000)
print(l2.__dict__)
print(l2.apply_discount())

class Laptop:
    discont_percent =10
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        
    def apply_discount(self):
        off_price=(self.discont_percent/100)*self.price  #### write self
        return self.price - off_price
        
Laptop.discont_percent=50
l1=Laptop('Dell','Inspiron',50000)
l2=Laptop('HP','i7',90000)
print(l2.__dict__)
print(l2.apply_discount())