import matplotlib.pyplot as plt
import math

x = 0
y = 0

plotx = []
ploty = []

for i in range(10000):
    y=math.cos(x)
    x+=0.001
    plotx.append(x)
    ploty.append(y)

ploty.sort()


plt.plot(plotx, ploty)
plt.show()