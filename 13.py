import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.randint(10,20,20)
x2 = np.random.randint(20,30,20)
x3 = np.random.randint(20,30,20)
y1 = np.random.randint(50,100,20)
y2 = np.random.randint(0,40,20)
y3 = np.random.randint(0,40,20)

fig = plt.figure(figsize=(9,3))

ax1 = fig.add_subplot(131,
                      xlim=(0,40), ylim=(0,120),
                      xticks=np.arange(0,50, 10), yticks=np.arange(0,150, 10))

ax1.scatter(x1, y1, marker='*',s=80,c='red')
ax2 = fig.add_subplot(132,
                      xlim=(0,40), ylim=(0,120),
                      xticks=np.arange(0,50, 10), yticks=np.arange(0,150, 10))

ax2.scatter(x2, y2, marker='^',s=60,c='blue')

ax3 = fig.add_subplot(133,
                      xlim=(0,40), ylim=(0,120),
                      xticks=np.arange(0,50, 10), yticks=np.arange(0,150, 10))
ax3.scatter(x3, y3, marker='x',s=30,c='green')


fig.savefig("img.png")