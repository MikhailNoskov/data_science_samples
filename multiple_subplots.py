import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-white')
# ax1 = plt.axes()  # standard axes
# ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])

# object-oriented interface equivalent
# fig = plt.figure()
# ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4], xticklabels=[], ylim=(-1.2, 1.2))
# ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4], ylim=(-1.2, 1.2))
# x = np.linspace(0, 10)
# ax1.plot(np.sin(x))
# ax2.plot(np.cos(x))

# for i in range(1, 7):
#     plt.subplot(2, 3, i)
#     plt.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')

# the equivalent object-oriented command

# fig = plt.figure()
# fig.subplots_adjust(hspace=0.4, wspace=0.4)
# for i in range(1, 10):
#     ax = fig.add_subplot(3, 3, i)
#     ax.text(0.5, 0.5, str((3, 3, i)), fontsize=18, ha='center')

# The Whole Grid in One Go

# fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
# axes are in a two-dimensional array, indexed by [row, col]
# for i in range(2):
#     for j in range(3):
#         ax[i, j].text(0.5, 0.5, str((i, j)), fontsize=18, ha='center')

#More Complicated Arrangements

# grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
# plt.subplot(grid[0, :])
# # plt.subplot(grid[0, 1 :])
# plt.subplot(grid[1, :2])
# plt.subplot(grid[1, 2])

# Example

# Create some normally distributed data
mean = [0, 0]
cov = [[1, 1], [1, 2]]
rng = np.random.default_rng(1701)
x, y = rng.multivariate_normal(mean, cov, 3000).T
# Set up the axes with GridSpec
fig = plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
main_ax = fig.add_subplot(grid[:-1, 1:])
plt.title('Main')
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
plt.title('Left')
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)
# Scatter points on the main axes
main_ax.plot(x, y, 'ok', markersize=3, alpha=0.2)
# Histogram on the attached axes
x_hist.hist(x, 40, histtype='stepfilled', orientation='vertical', color='gray')
x_hist.invert_yaxis()
y_hist.hist(y, 40, histtype='stepfilled', orientation='horizontal', color='gray')
y_hist.invert_xaxis()
plt.show()