import numpy as np
arr=[0,5,0,0,1  ,2,0,0,3,0]

arr_n=np.array(arr)

mymax=np.max(arr_n)

print("mymax",mymax)

myidx = np.argmax(arr_n)

print("myidx",myidx)