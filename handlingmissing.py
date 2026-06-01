"""if in array there are some null values nan then we can use np.nan_to_num() to replace them with 0 or for default value use np.nan_to_num(arr,nan=value)"""

import numpy as np
arr=np.array([1,2,np.nan,4,np.nan,5])
print(np.isnan(arr))

"""this is to check for NaN values"""

import numpy as np
arr=np.array([1,2,np.nan,4,np.nan,5])

result=np.nan_to_num(arr,nan=1)
print(result)

"""if no nan value is provided then default value 0 is used"""

"""if infinite value is present then it is replaced with a very large number and we use np.isinf() to check to replace infinite num to finite we use np.nan_to_num(arr, posinf=1**10, neginf=-1**10)"""

import numpy as np
arr=np.array([1,4,np.inf,6,-np.inf])
print(np.isinf(arr))
#to check whether is infinite or not

result=np.nan_to_num(arr,posinf=1**10,neginf=-1**10)
print(result)
