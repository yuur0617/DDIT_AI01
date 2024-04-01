import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.plot([0, 0, 0, 0], [0, 1, 2, 3], [0, 5, 0, 5], 'r')
ax.plot([1, 1, 1, 1], [0, 1, 2, 3], [5, 0, 5, 0], 'g')
ax.plot([2, 2, 2, 2], [0, 1, 2, 3], [2.5, 2.5, 2.5, 2.5], 'y')

plt.show()