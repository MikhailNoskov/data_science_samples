import numpy as np
import pandas as pd

vals1 = np.array([1, None, 2, 3])
print(vals1)

data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'), dtype='Int32')
# print(data)
data.fillna(0)
print(data.fillna(0))
data_2 = data.ffill()
print(data_2)
data_3 = data.bfill()
print(data_3)

df = pd.DataFrame([[1, np.nan, 2],
                   [2, 3, 5],
                   [np.nan, 4, 6]])
print(df.ffill(axis=1))
print(df.bfill(axis=0))
print(df.ffill(axis=0))
