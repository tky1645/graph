import matplotlib.pyplot as plt
import numpy as np

mu1, sig1 = 100 ,15
mu2, sig2 = 90 ,20
mu3, sig3 = 110 ,10

x2 = mu2+sig2*np.random.randn(10000)
x3 = mu3+sig3*np.random.randn(10000)
x1 = mu1+sig1*np.random.randn(10000)


fig = plt.figure(figsize=(9,6))

ax1 = fig.add_subplot(111, title='histgram', xlabel='x', ylabel='frequency',
                      xlim=(0,180))
ax1.hist([x1,x2,x3],color=['yellow','skyblue','blue'], stacked=True)
# ax1.hist(x1, bins=10, color='yellow',label='x1',zorder=10,stacked=True, density = True)
# ax1.hist(x2, bins=10, color='skyblue',label='x2',zorder=5,stacked=True, density = True)
# ax1.hist(x3, bins=10, color='blue',label='x3',zorder=1,stacked=True, density = True)

ax1.legend(loc=2)
ax1.grid()

fig.savefig("img.png")