from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Categorical Features

data = [
    {'price ': 850000, 'rooms ': 4, 'neighborhood ': 'Queen Anne'},
    {'price ': 700000, 'rooms ': 3, 'neighborhood ': 'Fremont'},
    {'price ': 650000, 'rooms ': 3, 'neighborhood ': 'Wallingford'},
    {'price ': 600000, 'rooms ': 2, 'neighborhood ': 'Fremont'}
]

# vec = DictVectorizer(sparse=False, dtype=int)
# vec = DictVectorizer(sparse=True, dtype=int)
# new_data = vec.fit_transform(data)
# print(new_data)
# print(vec.get_feature_names_out())

# Text Features

# sample = ['problem of evil', 'evil queen', 'horizon problem']
# vec = CountVectorizer()
# X = vec.fit_transform(sample)
#
# print(X)
#
# new_data = pd.DataFrame(X.toarray(), columns=vec.get_feature_names_out())
# print(new_data)
#
# vec = TfidfVectorizer()
# X = vec.fit_transform(sample)
# new_data = pd.DataFrame(X.toarray(), columns=vec.get_feature_names_out())
# print(new_data)

# Derived features

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([4, 2, 1, 3, 7])
# plt.scatter(x, y)

from sklearn.linear_model import LinearRegression
# X = x[:, np.newaxis]
# model = LinearRegression().fit(X, y)
# yfit = model.predict(X)
# plt.scatter(x, y)
# plt.plot(x, yfit)

from sklearn.preprocessing import PolynomialFeatures
# poly = PolynomialFeatures(degree=3, include_bias=False)
# X2 = poly.fit_transform(X)
# model = LinearRegression().fit(X2, y)
# yfit = model.predict(X2)
# plt.scatter(x, y)
# plt.plot(x, yfit)
# print(X2)

# Imputation of Missing Data

from numpy import nan
X = np.array([[nan, 0, 3],
              [3, 7, 9],
              [3, 5, 2],
              [4, nan, 6],
              [8, 8, 1]])

y = np.array([14, 16, -1, 8, -5])

from sklearn.impute import SimpleImputer
imp = SimpleImputer(strategy='mean')
X2 = imp.fit_transform(X)

print(X2)

model = LinearRegression().fit(X2, y)
new_data = model.predict(X2)
print(new_data)

# Feature Pipelines

from sklearn.pipeline import make_pipeline

model = make_pipeline(SimpleImputer(strategy='mean'),
                      PolynomialFeatures(degree=2),
                      LinearRegression())

model.fit(X, y)
print(y)
print(model.predict(X))

plt.show()