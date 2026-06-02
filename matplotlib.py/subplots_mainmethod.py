#fig, ax=plt.subplots(nrows,ncolumns, figsize=(width,height))
import matplotlib.pyplot as plt

fig, ax=plt.subplots(1,3,figsize=(10,5))

x=[1,2,3,4]
y=[10,20,15,40]

ax[0].plot(x,y)
ax[0].set_title("Line Plot")
ax[0].set_xlabel("X-axis")
ax[0].set_ylabel("Y-axis")

ax[1].bar(x,y)
ax[1].set_title("Bar Plot")
ax[1].set_xlabel("X-axis")
ax[1].set_ylabel("Y-axis")

ax[2].pie(x,labels=y,autopct='%1.1f%%')
ax[2].set_title("Pie Chart")

fig.suptitle("Difference between Line and Bar Plot and Pie Chart")

plt.tight_layout()
plt.show()

