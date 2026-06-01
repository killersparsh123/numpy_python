import numpy as np
arr=np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
insert_into=np.insert(arr,0,[1,2,3],axis=0)
print(insert_into)
