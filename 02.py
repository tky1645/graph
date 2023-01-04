import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.randint(10,20,20)
x2 = np.random.randint(20,30,20)
y1 = np.random.randint(50,100,20)
y2 = np.random.randint(0,40,20)

fig = plt.figure()

ax1 = fig.add_subplot(111,xlim=(0,40), ylim=(0,120))

ax1.scatter(x1, y1)
ax1.scatter(x2, y2)


fig.savefig("img.png")