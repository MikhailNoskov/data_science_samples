import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('data/FremontBridge.csv', index_col='Date', parse_dates=True)
# print(data.head())
data.columns = ['Total', 'East', 'West']
# print(data.dropna().describe())

data.plot()
# plt.ylabel('Hourly Bicycle Count')
# plt.show()

weekly = data.resample('W').sum()
weekly.plot(style=['-', ':', '--'])
# plt.ylabel('Weekly bicycle count')
# plt.show()

daily = data.resample('D').sum()
# daily.rolling(30, center=True).sum().plot(style=['-', ':', '--'])
# plt.ylabel('mean hourly count')
# plt.show()

daily.rolling(50, center=True, win_type='gaussian').sum(std=10).plot(style=['-', ':', '--'])  #More smooth Gaussian variant
# plt.ylabel('mean hourly count')
# plt.show()

# The average traffic as a function of the time of day

# by_time = data.groupby(data.index.time).mean()
hourly_ticks = 4 * 60 * 60 * np.arange(6)
# by_time.plot(xticks=hourly_ticks, style=['-', ':', '--'])
# plt.show()

"""
The hourly traffic is a strongly bimodal sequence, with peaks around 8:00 a.m. and
5:00 p.m. This is likely evidence of a strong component of commuter traffic crossing
the bridge. There is a directional component as well: according to the data, the east
sidewalk is used more during the a.m. commute, and the west sidewalk is used more
during the p.m. commute.
"""

# The day of the week trends

# by_weekday = data.groupby(data.index.dayofweek).mean()
# by_weekday.index = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
# by_weekday.plot(style=['-', ':', '--'])
# plt.show()

# Weekdays vs versus weekends hourly analytics

weekend = np.where(data.index.weekday < 5, 'Weekday', 'Weekend')
by_time = data.groupby([weekend, data.index.time]).mean()

fig, ax = plt.subplots(1, 2, figsize=(14, 5))
by_time.loc['Weekday'].plot(ax=ax[0], title='Weekdays', xticks=hourly_ticks, style=['-', ':', '--'])
by_time.loc['Weekend'].plot(ax=ax[1], title='Weekends', xticks=hourly_ticks, style=['-', ':', '--'])
plt.show()