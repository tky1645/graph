import matplotlib.pyplot as plt
import numpy as np

x = ['a','b','c','d']
y = np.random.randint(0,10,4)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.bar(x,y)

fig.savefig("img.png")