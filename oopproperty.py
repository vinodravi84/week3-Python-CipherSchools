class Phone:

    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        self.complete_specification = f"{self.brand} {self.model} and price is {self.price}"
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
p1=Phone("Nokia","1100",1000)
print(p1.brand)
print(p1.model)
p1.price= -500 
print(p1.price)
print(p1.complete_specification)
# problem 1 price cannot be negative as it is practically not possible
# problem 2 price is not changing in the complete_sprcifications


#soltuion 
class Phone:

    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=max(price,0)
        #if price >0:
        #    self.price=price
        #else:
         #   self.price=0
        self.complete_specification = f"{self.brand} {self.model} and price is {self.price}"
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
p1=Phone("Nokia","1100",-1000)
print(p1.brand)
print(p1.model)
 
print(p1.price)
print(p1.complete_specification)

# problem 2 soln
class Phone:

    def complete_specification(self):
        return f"{self.brand} {self.model} and price is {self.price}"
    
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
p1=Phone("Nokia","1100",1000)

p1.price= 500 
print(p1.price)
print(p1.complete_specification())   
def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=max(price,0)
        #self.complete_specification = f"{self.brand} {self.model} and price is {self.price}"



# property decorator 
# problem 2 soln
class Phone:

    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=max(price,0)
        #self.complete_specification = f"{self.brand} {self.model} and price is {self.price}"
    @property
    def complete_specification(self):
        return f"{self.brand} {self.model} and price is {self.price}"
    
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
p1=Phone("Nokia","1100",1000)

p1.price= 500 
print(p1.price)
print(p1.complete_specification)  # i can print it without the ()


# to make it practical
class Phone:

    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=max(price,0)
        #self.complete_specification = f"{self.brand} {self.model} and price is {self.price}"
    @property
    def complete_specification(self):
        return f"{self.brand} {self.model} and price is {self.price}"
    #getter 
    @property
    def pricee(self):
        return self.price
    
    #setter
    @pricee.setter
    def price(self,new_price):
        self.price=max(new_price,0)
        
    
p1=Phone("Nokia","1100",1000)

p1.price= 500 
print(p1.price)
print(p1.complete_specification)