import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

sns.set()  # seaborn's method to set its chart style

# Histograms, KDE, and Densities

# data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
# print(data)
# data = pd.DataFrame(data, columns=['x', 'y'])
# print(data)
# for col in 'xy':
#     plt.hist(data[col], density=True, alpha=0.5)

# sns.kdeplot(data=data, shade=True)
# sns.kdeplot(data=data, x='x', y='y')
# iris = sns.load_dataset("iris")
# print(iris.head())
# sns.pairplot(iris, hue='species', height=2.5)

# Faceted Histograms

tips = sns.load_dataset('tips')
# tips.head()
#
tips['tip_pct'] = 100 * tips['tip'] / tips['total_bill']
# grid = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True)
# grid.map(plt.hist, "tip_pct", bins=np.linspace(0, 40, 15))

# Categorical Plots

# with sns.axes_style(style='ticks'):
#     g = sns.catplot(x="day", y="total_bill", hue="sex", data=tips, kind="box")
#     g.set_axis_labels("Day", "Total Bill")

# Joint Distributions

# with sns.axes_style('white'):
    # sns.jointplot(x="total_bill", y="tip", data=tips, kind='hex')
    # sns.jointplot(x="total_bill", y="tip", data=tips, kind='reg')  #  automatic kernel density estimation and regression

# Bar Plots

planets = sns.load_dataset('planets')
# print(planets.head())
# with sns.axes_style('white'):
#     g = sns.catplot(x="year", data=planets, aspect=2, kind="count", color='steelblue')
#     g.set_xticklabels(step=5)

with sns.axes_style('white'):
    g = sns.catplot(x="year", data=planets, aspect=4.0, kind='count', hue='method', order=range(2001, 2015))
    g.set_ylabels('Number of Planets Discovered')

plt.show()