# DISCOUNT OF 40% ON PRICE

class Laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        
    def apply_discount(self,num):
        off_price=(num/100)*self.price
        return self.price - off_price
        
        
l1=Laptop('Dell','Inspiron',50000)
l2=Laptop('HP','i7',90000)
print(l1.apply_discount(10))

class Laptop:
    discont_percent =10
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        
    def apply_discount(self):
        off_price=(Laptop.discont_percent/100)*self.price
        return self.price - off_price
        
        
l1=Laptop('Dell','Inspiron',50000)
l2=Laptop('HP','i7',90000)
print(l1.apply_discount())

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
        
Laptop.discount_percent=50    # but 10 percent is coming in outcome 
l1=Laptop('Dell','Inspiron',50000)
l2=Laptop('HP','i7',90000)
print(l2.__dict__)
print(l2.apply_discount())

