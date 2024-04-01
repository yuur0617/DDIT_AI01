import numpy as np

arr = [1,2,3]

arr_n1 = np.array(arr)
arr_n2 = np.array(arr)

arr_d = np.append(arr_n1, arr_n2)

arr[0] = 4 # 바뀌지 않음.

print(arr_d)

