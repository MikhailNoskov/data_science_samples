import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-white')
rng = np.random.default_rng(1701)

# data = rng.normal(size=1000)
# print(data)
# plt.hist(data)
# plt.hist(data, bins=30, density=True, alpha=0.5,
#          histtype='stepfilled', color='steelblue',
#          edgecolor='none')

# x1 = rng.normal(0, 0.8, 1000)
# x2 = rng.normal(-2, 1, 1000)
# x3 = rng.normal(3, 2, 1000)
#
# kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, bins=40)
#
# plt.hist(x1, **kwargs)
# plt.hist(x2, **kwargs)
# plt.hist(x3, **kwargs)
# plt.show()

# Two-Dimensional Histograms and Binnings

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = rng.multivariate_normal(mean, cov, 10000).T
# print(x)
# print(y)
# plt.hist2d(x, y, bins=30)  # Square bins
plt.hexbin(x, y, gridsize=30)  # Hexagonal bins
cb = plt.colorbar()
cb.set_label('counts in bin')

plt.show()