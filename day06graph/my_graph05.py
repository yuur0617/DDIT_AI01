import matplotlib.pyplot as plt
from day06graph.daostock import DaoStock
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

ds = DaoStock()
s_names = ["삼성전자", "서울식품"]

prices = []
for s in s_names:
    prices.append(ds.selectArrN(s))

cnt_t = len(prices[0])
xs = np.ones((cnt_t),dtype=np.int8)


for idx, s in enumerate(s_names):
    print(prices[idx])
    tp = (prices[idx]/prices[idx][0])*100
    print(tp)
    ax.plot(xs*idx, list(range(cnt_t)), tp, '')

plt.show()