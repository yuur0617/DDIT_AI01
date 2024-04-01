import numpy as np
arr=[0,0,0,0,0  ,1,0,0,0,0]

arr_n=np.array(arr)

print(arr_n)

    
mymax=-1
for i in arr:
    if i>mymax :
        mymax=i
    
for idx,i in enumerate(arr):
    if mymax == i:
        print(idx)
    