import numpy as np

arr1 = range(9) 
arr= list(range(9))
arr_n = np.array(arr) 

arr_n2 = np.reshape(arr_n,(3,3))

arr_n3 = np.float16(arr_n2) 

print(arr1) #range(0, 9)
print(arr) #[0, 1, 2, 3, 4, 5, 6, 7, 8]
print(arr_n) #[0 1 2 3 4 5 6 7 8]
print(arr_n.shape) #(9,)
print(arr_n2) #[[0 1 2] [3 4 5] [6 7 8]]
print(arr_n2.shape) #(3, 3)
print(arr_n3) #[[0. 1. 2.] [3. 4. 5.] [6. 7. 8.]]
