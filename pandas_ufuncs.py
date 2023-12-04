import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
# ser = pd.Series(rng.integers(0, 10, 4))
#
# print(ser)
#
# df = pd.DataFrame(rng.integers(0, 10, (3, 4)), columns=['A', 'B', 'C', 'D'])
# print(df)
#
# print(np.exp(ser))
# print(np.sin(df * np.pi / 4))
#
# area = pd.Series({'Alaska': 1723337, 'Texas': 695662, 'California': 423967}, name='area')
# population = pd.Series({'California': 39538223, 'Texas': 29145505, 'Florida': 21538187}, name='population')
#
# print(population / area)

# A = pd.Series([2, 4, 6], index=[0, 1, 2])
# B = pd.Series([1, 3, 5], index=[1, 2, 3])
#
# print(A + B)
# print(A.add(B, fill_value=0))

A = pd.DataFrame(rng.integers(0, 20, (2, 2)), columns=['a', 'b'])
B = pd.DataFrame(rng.integers(0, 10, (3, 3)), columns=['b', 'a', 'c'])

print(A + B)
print(A.add(B, fill_value=0))
