import numpy as np
import pandas as pd

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])

# data['e'] = 1.25
# print(data)
# print(list(data.items()))
# print(data[["a", "c"]])
# print(data[0:4])
# print(data[(data > 0.3) & (data < 0.8)])

# loc and iloc indexing
# data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
# print(data)
# print(data[1])
# print(data[1:3])
# print(data.loc[1])
# print(data.iloc[1])
# print(data.loc[1:3])
# print(data.iloc[1:3])

# Data selection

area = pd.Series({'California': 423967, 'Texas': 695662,
                  'Florida': 170312, 'New York': 141297,
                  'Pennsylvania': 119280})
pop = pd.Series({'California': 39538223, 'Texas': 29145505,
                 'Florida': 21538187, 'New York': 20201249,
                 'Pennsylvania': 13002700})
data = pd.DataFrame({'area': area, 'pop': pop})
data['density'] = data['pop'] / data['area']
print(data)
#
# print(list(data.items()))
# print(data.values)
# print(data.T)
#
# print(data.values[0])
# print(data['area'])
# print(data.area)

# print(data.iloc[:3, :1])
# print(data.loc[:'Florida', :'pop'])
print(data.loc[(data.density < 120) & (data.area > 200000), ['pop', 'density']])