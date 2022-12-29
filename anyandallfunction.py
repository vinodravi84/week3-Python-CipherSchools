# any() and all(()) function
# all -->> is only one will beacme false it will print false
# any-->> if atleast one is true it will show true
num1=[2,4,6,8,10]
num2=[1,2,3,4,5,6]
evens1=[]
for num in num1:
    evens1.append(num%2==0)
    
print(all([True, True, True, True, True]))


#all
num1=[1,2,3,4,5,6,7,8,9]
print(all([num%2==0 for num in num1]))

#any
num1=[1,2,3,4,5,6,7,8,9]
print(any([num%2==0 for num in num1]))

num1=[2,4,6,8,10]
print(all([num%2==0 for num in num1]))

# any all function practise class 163
def my_sum(*args):
    total=0
    for num in args:
        total += num
    return total
print(my_sum(1,2,3,4))


def my_sum(*args):
    if all([(type(arg)==int or type(arg)==float)for arg in args]):
        total=0
        
        for num in args:
            total +=num
            return total
    else:
           return "wrong input"

        
      
print(my_sum(1,2,3,'ankit',['abc']))




