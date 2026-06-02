#savefig('filename.extension',dpi=value,bbox_inches='tight') dpi->shows the resolution of the output file and full form is dots per inch
#bbox_inches is used to specify the portion of the figure to save and there are several options like 'tight', 'standard', etc.

import matplotlib.pyplot as plt

x=[1,2,3,4,5] #x-axis(horizontal axis)
y=[20,15,30,40,50] #y-axis(vertical axis)
plt.plot(x,y)
plt.savefig('line_plot.png',dpi=300,bbox_inches="tight")
plt.show()

