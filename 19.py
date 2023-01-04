import matplotlib.pyplot as plt
import numpy as np

labels = ['a','h','g','d']
size = [15,30,45,10]
explode = (0,0.1,0,0)

fig = plt.figure(figsize=(9,6))

ax1 = fig.add_subplot(111)
ax1.pie(size, explode=explode,labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

fig.savefig("img.png")