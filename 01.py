import matplotlib.pyplot as plt
import numpy as np

x= np.arange(10)
y = np.random.randint(-10,10,10)

fig = plt.figure()
ax = fig.add_subplot(111, xlabel='x', ylabel='y', title='Result')
ax.plot(x, y)



fig.savefig("img.png")