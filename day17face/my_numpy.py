import numpy as np

arr = [1,2,3]
arr_n = np.array(arr)

print(arr)
print(arr_n)

np.save("arr_n", arr_n)
