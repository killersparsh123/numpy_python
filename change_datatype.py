import numpy as np

arr=np.array([1,2,3.5])
print(arr.dtype)
int_arr=arr.astype(str)
print(int_arr)
print(int_arr.dtype)
