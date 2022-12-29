# create a laptop class with attributes like brand name, model name, price
# create two obejects/instance of your laptop
class Laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
l1=Laptop('Dell','Inspiron',50000)
l2=Laptop('HP','i7',90000)
print(l1.brand)

class Laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        self.laptop_name=brand + ' ' + model
l1=Laptop('Dell','Inspiron',50000)
l2=Laptop('HP','i7',90000)
print(l1.brand)
print(l1.laptop_name)