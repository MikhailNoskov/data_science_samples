import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pandas.tseries.holiday import USFederalHolidayCalendar
from sklearn.linear_model import LinearRegression
from sklearn.utils import resample

counts = pd.read_csv('data/FremontBridge.csv', index_col='Date', parse_dates=True)  # Getting data about bycicle rides and weather
weather = pd.read_csv('data/SeattleWeather.csv', index_col='DATE', parse_dates=True)

# print(counts)
# print(weather)

counts = counts[counts.index < "2020-01-01"] # Reducing data by filtering out pandemic data
weather = weather[weather.index < "2020-01-01"]

daily = counts.resample('d').sum()  # Daily trafic
daily['Total'] = daily.sum(axis=1)
daily = daily[['Total']] # remove other columns

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']  # adding binary columns that indicate the day of the week
for i in range(7):
    daily[days[i]] = (daily.index.dayofweek == i).astype(float)

cal = USFederalHolidayCalendar()  # Adding holidays binary column
holidays = cal.holidays('2012', '2020')
daily = daily.join(pd.Series(1, index=holidays, name='holiday'))
daily['holiday'].fillna(0, inplace=True)


def hours_of_daylight(date, axis=23.44, latitude=47.61):  # Adding daylight info
    """Compute the hours of daylight for the given date"""
    days = (date - datetime.datetime(year=2000, month=12, day=21)).days
    m = (1. - np.tan(np.radians(latitude)) * np.tan(np.radians(axis) * np.cos(days * 2 * np.pi / 365.25)))
    return 24. * np.degrees(np.arccos(1 - np.clip(m, 0, 2))) / 180.


daily['daylight_hrs'] = list(map(hours_of_daylight, daily.index))
daily[['daylight_hrs']].plot()
plt.ylim(8, 17)

weather['Temp (F)'] = 0.5 * (weather['TMIN'] + weather['TMAX'])
weather['Rainfall (in)'] = weather['PRCP']
weather['dry day'] = (weather['PRCP'] == 0).astype(int)
daily = daily.join(weather[['Rainfall (in)', 'Temp (F)', 'dry day']])
daily['annual'] = (daily.index - daily.index[0]).days / 365.

# print(daily)

# Drop any rows with null values
daily.dropna(axis=0, how='any', inplace=True)
column_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun',
'holiday', 'daylight_hrs', 'Rainfall (in)',
'dry day', 'Temp (F)', 'annual']
X = daily[column_names]
y = daily['Total']
model = LinearRegression(fit_intercept=False)
model.fit(X, y)
daily['predicted'] = model.predict(X)

daily[['Total', 'predicted']].plot(alpha=0.5)
plt.show()

params = pd.Series(model.coef_, index=X.columns)
print(params)


# Compute these uncertainties

np.random.seed(1)
err = np.std([model.fit(*resample(X, y)).coef_ for i in range(1000)], 0)
print(pd.DataFrame({'effect': params.round(0), 'uncertainty': err.round(0)}))
