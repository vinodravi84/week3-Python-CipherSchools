# list vs generator
# memory usage, time
# when to use list , when to use generator 
l=[i**2 for i in range(10000000)] # 10 million
# we can check the memory in TASK MANAGER 
# it will take almost '400 MB'

g=(i**2 for i in range(10000000))
# it will not take this much memory because it will take one at a time
import time
t1=time.time()
l=[i**2 for i in range(10000000)]
t2=time.time()
print(t2-t1)

import time
t1=time.time()
l=(i**2 for i in range(10000000))
t2=time.time()
print(t2-t1)