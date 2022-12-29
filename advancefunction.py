#THIS IS CHALLENGE

# define a function take any no of lists containing number 
# [1,2,3], [4,5,6], [7,8,9]

# return average
# (1+4+7)/3, (2,5,8)/3, (3,6,9)/3

# try to make this anonymous function in one line using lambda


def  average(l1,l2):
    avg=[]
    for pair in zip(l1,l2):
        avg.append(sum(pair)/len(pair))
    return avg
print(average([1,2,3],[4,5,6]))

def  average(*args):
    avg=[]
    for pair in zip(*args):
        avg.append(sum(pair)/len(pair))
    return avg
print(average([1,2,3],[4,5,6],[7,8,9]))

average=lambda*args:[sum(pair)/len(pair) for pair in zip(*args)]
print(average([1,2,3],[4,5,6],[7,8,9]))