import matplotlib.pyplot as plt
from day06graph.daostock import DaoStock
import numpy as np


ds = DaoStock()

prices = []
prices.append(ds.selectArr("삼성전자"))
prices.append(ds.selectArr("LG"))
prices.append(ds.selectArr("마니커"))
prices.append(ds.selectArr("서울식품"))

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')

xs = np.ones((10),dtype=np.int8)

ax.plot(xs*0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], prices[0], 'r')
ax.plot(xs*1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], prices[1], 'g')
ax.plot(xs*2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], prices[2], 'y')
ax.plot(xs*3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], prices[3], 'k')

plt.show()