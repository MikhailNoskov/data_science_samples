import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris

plt.style.use('seaborn-whitegrid')
# x = np.linspace(0, 10, 30)
# y = np.sin(x)
# plt.plot(x, y, 'o', color='black')

# rng = np.random.default_rng(0)
# for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:  # Options for symbols
#     plt.plot(rng.random(2), rng.random(2), marker, color='black', label="marker='{0}'".format(marker))
# plt.legend(numpoints=1, fontsize=13)
# plt.xlim(0, 1.8)

# plt.plot(x, y, '-ok')

# plt.plot(x, y, '-p', color='gray',
#          markersize=15, linewidth=4,
#          markerfacecolor='white',
#          markeredgecolor='gray',
#          markeredgewidth=2)
# plt.ylim(-1.2, 1.2)

# plt.scatter(x, y, marker='o')  # Each point can have different properties
# rng = np.random.default_rng(0)
# x = rng.normal(size=100)
# y = rng.normal(size=100)
# colors = rng.random(100)
# sizes = 1000 * rng.random(100)
#
# plt.scatter(x, y, c=colors, s=sizes, alpha=0.3)
# plt.colorbar()

iris = load_iris()
# print(iris)
features = iris.data.T
# print(features)
#
plt.scatter(features[0], features[1], alpha=0.4, s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()