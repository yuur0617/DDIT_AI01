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
arr_nlr = np.fliplr(arr_n)
arr_nud = np.flipud(arr_n)

print(arr_n)
print(arr_nlr)
print(arr_nud)
