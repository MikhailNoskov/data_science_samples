import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import datetime

sns.set()


def convert_time(s):
    """Here we convert data from str to datetime"""
    h, m, s = map(int, s.split(':'))
    return h * 3600 + m * 60 + s


data = pd.read_csv('data/marathon-data.csv', converters={'split': convert_time, 'final': convert_time})

# with sns.axes_style('white'):
#     g = sns.jointplot(x='split', y='final', data=data, kind='hex')
#     g.ax_joint.plot(np.linspace(4000, 16000),
#     np.linspace(8000, 32000), ':k')

data['split_frac'] = 1 - 2 * data['split'] / data['final']  # Split fraction calculation
# print(data.head())
# sns.displot(data['split_frac'], kde=False)
# plt.axvline(0, color="k", linestyle="--")
# g = sns.PairGrid(data, vars=['age', 'split', 'final', 'split_frac'], hue='gender', palette='RdBu_r')
# g.map(plt.scatter, alpha=0.8)
# g.add_legend()
# sns.kdeplot(data.split_frac[data.gender == 'M'], label='men', shade=True)
# sns.kdeplot(data.split_frac[data.gender == 'W'], label='women', shade=True)
# plt.xlabel('split_frac')
# sns.violinplot(x="gender", y="split_frac", data=data, palette=["lightblue", "lightpink"])

data['age_dec'] = data.age.map(lambda age: 10 * (age // 10))
# print(data.head())

men = (data.gender == 'M')
women = (data.gender == 'W')

# with sns.axes_style(style=None):
#     sns.violinplot(x="age_dec", y="split_frac", hue="gender", data=data, split=True, inner="quartile", palette=["lightblue", "lightpink"])

g = sns.lmplot(x='final', y='split_frac', col='gender', data=data,
               markers=".", scatter_kws=dict(color='c'))
g.map(plt.axhline, y=0.0, color="k", ls=":")
plt.show()
