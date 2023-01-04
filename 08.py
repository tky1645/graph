import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi,500)
y1 = np.sin(x)
y2 = np.cos(x)

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(x, y1,label='sin')
ax1.plot(x, y2,label='cos')

ax1.legend(loc='upper left')

fig.savefig("img.png")