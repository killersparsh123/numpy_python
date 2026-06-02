#plt.plot(x,y,color='color name ',linestyle='line_style',linewidth=value,marker="marker_symbol",label="label name") 
#plt.legend(loc="location",fontsize=value)
#plt.grid(color=" ",linestyle="")
#plt.xlim(start,end)
#axis-ticks --->> plt.xticks([ ],[ ])
    

import matplotlib.pyplot as plt
company=['google','apple','microsoft','amazon','facebook']
valuation=[1000,2100,3000,1500,2500]

plt.plot(company,valuation,color="violet",linestyle="-",linewidth=4,marker="o",label="Company Valuation")
plt.xlabel("Company")
plt.ylabel("Valuation (in billions)")
plt.title("Company Valuation Comparison")
plt.legend(loc='upper left',fontsize=6)
plt.grid(color='gray',linestyle=':')
plt.xlim('microsoft','facebook')
plt.ylim(0,2200)
plt.show()
