import matplotlib.pyplot as plt
import numpy as np

# Dividing the section of the pie chart
y=np.array([10,20,35,20,25])
#give the name of the section
mylabels=["Apples","Mango","Bananas","Orange","Graphes"]
myexplode=[0.2,0,0,0,0]   #0.3 is distance between the slice 

plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
plt.show()