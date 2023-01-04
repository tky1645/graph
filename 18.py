import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(10)
x2 = ['a','h','g','d']
y1 = np.random.randint(-10,10,10)
y2 = np.random.randint(0,200,4)

fig = plt.figure(figsize=(9,6))

ax1 = fig.add_subplot(211,
                      title='Result',
                      xlabel='x axis',ylabel='y axis',
                      )
ax1.plot(x1, y1)

ax2 = fig.add_subplot(212)
ax2.bar(x2, y2)

fig.savefig("img.png")