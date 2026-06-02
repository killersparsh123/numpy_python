# in pyplot there are multiple tools collection of functions
# using this we can do pie, graph, bar
import matplotlib.pyplot as plt
x=['mon','tue','wed','thu','fri','sat','sun']
y=[10,20,1,4,2,5,3]
plt.plot(x,y)
plt.title("show the sales of 1st week")
plt.xlabel('Days of the week')
plt.ylabel("sales")
plt.show()