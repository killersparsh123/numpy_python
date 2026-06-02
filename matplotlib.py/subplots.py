# sub-plot helps to keep multiple line,graph,chart in single figure
#plt.subplot(nrows,ncols,index)

import matplotlib.pyplot as plt

x=[10,20,30,40,25]
y=[100,200,300,400,500]

plt.subplot(1,2,1)
plt.plot(x,y,color='black',marker='d')
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("line rep")

plt.subplot(1,2,2)
plt.bar(x,y,color='orange',width=5,edgecolor='black')
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("Bar Graph")

plt.subplot(1,3,3)
plt.pie(y,labels=x,autopct="%1.1f%%")
plt.title("Pie Chart")
plt.tight_layout() #tight_layout() improves spacing and prevents overlap 
plt.show()
