# scatter plot is used to display values for typically two variables for a set of data
#plt.scatter(x,y,color="colorname",alpha=0.5,label="labelname")

import matplotlib.pyplot as plt
x=[1,3,5,7,9]
y=[5000,600,6000,8000,10000]

plt.scatter(x,y,color="blue",alpha=1,label="data points",marker="d '")
plt.title("scatter graph representation")
plt.legend(loc="upper right")
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.grid(True)
plt.show()
