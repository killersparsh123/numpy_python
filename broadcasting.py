#suppose we want to provide 10% dsicount in every product then

import numpy as np

arr=np.array([100,400,500])
discount=0.1
final_price=arr-(arr*discount)
print(final_price)