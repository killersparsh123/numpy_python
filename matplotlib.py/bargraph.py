#plt.bar(x,height,color="color name",width=value,label="label name")

import matplotlib.pyplot as plt
x=['A','B','C','D']
y=[1000,1500,800,1200]
plt.bar(x,y,color="black",label="bar graph") #this shows bar vertically but if you want to show horizontally then use plt.barh()
plt.legend(loc="upper right",fontsize=12)
plt.grid(color="gray")
plt.xlabel("product")
plt.ylabel("sales")
plt.title("sales report")
plt.show()