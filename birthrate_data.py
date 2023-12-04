import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime


births = pd.read_csv('data/births.csv')

# print(births.head())
births['decade'] = 10 * (births['year'] // 10)  # Decades - i.e. 1960s

# print(births.pivot_table('births', index='decade', columns='gender', aggfunc='sum'))
plt.style.use('seaborn-whitegrid')

births.pivot_table('births', index='year', columns='gender', aggfunc='sum').plot()
plt.ylabel('total births per year, mln pers')
# plt.show()

quartiles = np.percentile(births['births'], [25, 50, 75])
# print(quartiles)
mu = quartiles[1]
# print(mu)
sig = 0.74 * (quartiles[2] - quartiles[0])
# print(sig)
births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
births['day'] = births['day'].astype(int)

births.index = pd.to_datetime(10000 * births.year + 100 * births.month + births.day, format='%Y%m%d')  # create a datetime index from the year, month, day
births['dayofweek'] = births.index.dayofweek

# births.pivot_table('births', index='dayofweek', columns='decade', aggfunc='mean').plot()
# plt.gca().set(xticks=range(7), xticklabels=['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
# plt.ylabel('mean births by day')
# plt.show()

births_by_date = births.pivot_table('births', [births.index.month, births.index.day])
# print(births_by_date.head(62))
births_by_date.index = [datetime(2012, month, day) for (month, day) in births_by_date.index]
# print(births_by_date.head())
fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax)
plt.show()