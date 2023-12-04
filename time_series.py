from datetime import datetime
from dateutil import parser
import numpy as np
import pandas as pd
from pandas.tseries.offsets import BDay
from pandas_datareader import data
import matplotlib.pyplot as plt

# date = parser.parse("4th of July, 2021")
# print(date)
# print(date.strftime('%A'))  # Nice one

# date = np.array('2021-07-04', dtype=np.datetime64)
# date = date + np.arange(12)
# print(date)

# day = np.datetime64('2021-07-04')
# print(day)
# day = np.datetime64('2021-07-04 12:00')
# print(day)
# day = np.datetime64('2021-07-04 12:59:59.50', 'ns')
# print(day)

# date = pd.to_datetime("4th of July, 2021")
# print(date)
# print(date.strftime('%A'))  # Same as in datetime
# print(date.strftime('%a'))

# date += pd.to_timedelta(np.arange(12), 'D')
# print(date)

# index = pd.DatetimeIndex(['2020-07-04', '2020-08-04', '2021-07-04', '2021-08-04'])
# data = pd.Series([0, 1, 2, 3], index=index)
#
# print(data)
# print(data['2020-07-04':'2021-07-04'])
# print(data['2021'])
# print(data['2020-07':'2021-07'])

# Pandas Time Series Data Structures

# dates = pd.to_datetime([datetime(2021, 7, 3), '4th of July, 2021', '2021-Jul-6', '07-07-2021', '20210708'])
# print(dates, dates.dtype)  # DatetimeIndex
# print(dates - dates[0])  # TimedeltaIndex

# Regular Sequences: pd.date_range

# print(pd.date_range('2015-07-03', '2015-07-10'))  # Date ranges
# print(pd.date_range('2015-07-03', periods=8))
# print(pd.date_range('2015-07-03', periods=8, freq='H'))
# print(pd.period_range('2015-07', periods=8, freq='M'))  # Period range
# print(pd.timedelta_range(0, periods=6, freq='H'))  # Timedelta range
# print(pd.timedelta_range(0, periods=6, freq="2H30T"))  # Timedelta range with a frequency of 2 hours and 30 minutes

# print(pd.date_range('2015-07-01', periods=12, freq=BDay()))  # Business days offset

# Resampling, Shifting, and Windowing

sp500 = data.DataReader('^DJI', 'stooq', start='2018', end='2022')
print(sp500.head())
sp500 = sp500['Close']
plt.style.use('seaborn-whitegrid')
# sp500.plot()
# plt.show()

# sp500.plot(alpha=0.5, style='-')
# sp500.resample('BA').mean().plot(style=':')
# sp500.asfreq('BA').plot(style='--')
# plt.legend(['input', 'resample', 'asfreq'], loc='lower left')
# plt.show()

# fig, ax = plt.subplots(2, sharex=True)
# data = sp500.iloc[:20]
# data.asfreq('D').plot(ax=ax[0], marker='o')
# data.asfreq('D', method='bfill').plot(ax=ax[1], style='-o')
# data.asfreq('D', method='ffill').plot(ax=ax[1], style='--o')
# ax[1].legend(["back-fill", "forward-fill"])
# plt.show()

# ROI = 100 * (sp500.shift(-365) - sp500) / sp500
# ROI.plot()
# plt.ylabel('% Return on Investment after 1 year')
# plt.show()

rolling = sp500.rolling(365, center=True)
data = pd.DataFrame({'input': sp500, 'one-year rolling_mean': rolling.mean(), 'one-year rolling_median': rolling.median()})
ax = data.plot(style=['-', '--', ':'])
ax.lines[0].set_alpha(0.3)
plt.show()
