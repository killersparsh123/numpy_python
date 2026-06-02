#plt.pie(x,label,colors="color name",autopct='%1.1f%%') --> in autopct we can define the format of the percentage display and 1.1f means 1 decimal place

import matplotlib.pyplot as plt
regions=['north','south','east','west']
revenue=[3000,2000,1500,1000]
plt.pie(revenue,labels=regions,colors=["red","blue","green","yellow"],autopct='%1.1f%%')
plt.title("contribution from the regions")
plt.show()