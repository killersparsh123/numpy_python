import numpy as np

arr_1=np.array([10,20,30])

print(f"first array : {arr_1}")

arr_2=np.array([40,50,60])
print(f"second array : {arr_2}")

concatenate=np.concatenate((arr_1,arr_2),axis=0)
print(concatenate)