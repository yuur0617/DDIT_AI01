import numpy as np

arr_n = np.array(
    [
        [1,0,0,0,0],
        [0,1,0,0,0],
        [0,1,2,2,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
)
arr_n90 = np.rot90(arr_n)
arr_n180 = np.rot90(arr_n90)

print(arr_n)
print(arr_n90)
print(arr_n180)