# OOP

#COMMON TOPIC IN ALMOST ALL POPULAR PROGRAMMING LANGUAGES (PYTHON, C++, JAVA) 

#WITH COMMON IDEA BUT WITH DIFFERENT SYNTAX

#OOP IS JUST A STYLE/WAY TO WRITE A CODE

# VERY HELPFUL IN CREATING REAL WORLD PROGRAMS

#WE WILL SEE OTHER ADVANTAGES WHEN WE WILL START LEARNING OOP
# class , object(instance), method
# list class
#list object
#method  


# class is a blueprint in which we decide ki anne vala object kaisa hoga
l=[1,2,3,4]#l is class ka object hai
l2=[4,5,6,7] 
l.append(8) # append is method

# CLASS 186
# OBJECTIVES

# WHAT IS CLASS

# HOW TO CREATE AN CLASS

# WHAT IS INIT METHOD (constructor)

# WHAT ARE ATTRIBUTES, INSTANCE VARIABLES 

# HOW TO CREATE OUR OBJECT
class Person: #captital letter convention
    def __init__(self, first_name,last_name,age):
        print("init method// constructor get called")
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
p1=Person('Ankit','Kumar',19)# yeh mere class ka object hai
p2=Person('Aman','Singh',19)
print(p1)
print(p2)
print(p1.first_name)
print(p2.first_name)