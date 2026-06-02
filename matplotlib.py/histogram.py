#plt.hist(data,bins=number_of_bins,color="colorname",edgecolor="black",alpha=0.8) ------>alpha means if alpha=1(fully visible) and if alpha=0(fully transparent) and if alpha=0.5(50% transparent)

import matplotlib.pyplot as plt
scores=[10,20,40,30,50,15]
plt.hist(scores,bins=3,color='purple',edgecolor="black",alpha=0.5)
plt.show()
