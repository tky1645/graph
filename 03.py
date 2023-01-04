import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(0,10,10)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.hist(data, bins=15)

fig.savefig("img.png")