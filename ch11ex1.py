#define a function 
#input

#num, iterable(tuple, list) containing numbers as args

# example

#nums=[1,2,3] 
#to power (3,"nums) 


#output

# list [13, 8, 27]

# if user didn't pass any args then give a user a message 'hey you did't pass

#args

# else

# return list

#NOTE USE list comprehension
 

l=[1,2,3]
if l:
    print("not empty")
else:
    print("empty")


def power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "you didnt pass any args"
nums=[1,2,3]
print(power(3,*nums))