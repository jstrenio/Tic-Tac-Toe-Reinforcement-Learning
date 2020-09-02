import matplotlib.pyplot as plt

with open('graph.txt') as fp:
    values = fp.read().split(',')
plt.axhline(0,color='red')
plt.yticks([-1000,-500, -100, 0,100,500,1000, 5000, 10000, 50000, 100000])
plt.plot(values)
plt.show()