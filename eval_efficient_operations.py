import pandas as pd
import numpy as np


rng = np.random.default_rng(42)
nrows, ncols = 100000, 100
df1, df2, df3, df4 = (pd.DataFrame(rng.random((nrows, ncols))) for i in range(4))
print(np.allclose(df1 + df2 + df3 + df4, pd.eval('df1 + df2 + df3 + df4')))

df1, df2, df3, df4, df5 = (pd.DataFrame(rng.integers(0, 1000, (100, 3))) for _ in range(5))
result1 = -df1 * df2 / (df3 + df4) - df5
result2 = pd.eval('-df1 * df2 / (df3 + df4) - df5')
print(np.allclose(result1, result2))

result1 = (df1 < df2) & (df2 <= df3) & (df3 != df4)
result2 = pd.eval('df1 < df2 <= df3 != df4')
print(np.allclose(result1, result2))

result1 = (df1 < 0.5) & (df2 < 0.5) | (df3 < df4)
result2 = pd.eval('(df1 < 0.5) & (df2 < 0.5) | (df3 < df4)')
print(np.allclose(result1, result2))

result3 = pd.eval('(df1 < 0.5) and (df2 < 0.5) or (df3 < df4)')
print(np.allclose(result1, result3))

result1 = df2.T[0] + df3.iloc[1]
result2 = pd.eval('df2.T[0] + df3.iloc[1]')
print(np.allclose(result1, result2))

df = pd.DataFrame(rng.random((1000, 3)), columns=['A', 'B', 'C'])
print(df.head())

result1 = (df['A'] + df['B']) / (df['C'] - 1)
result2 = pd.eval("(df.A + df.B) / (df.C - 1)")
print(np.allclose(result1, result2))

result3 = df.eval('(A + B) / (C - 1)')
print(np.allclose(result1, result3))

df.eval('D = (A + B) / C', inplace=True)
print(df.head())

column_mean = df.mean(1)
result1 = df['A'] + column_mean
result2 = df.eval('A + @column_mean')  # Python variable namespace in eval
print(np.allclose(result1, result2))

result1 = df[(df.A < 0.5) & (df.B < 0.5)]
result2 = pd.eval('df[(df.A < 0.5) & (df.B < 0.5)]')
print(np.allclose(result1, result2))

result2 = df.query('A < 0.5 and B < 0.5')
print(np.allclose(result1, result2))

Cmean = df['C'].mean()
result1 = df[(df.A < Cmean) & (df.B < Cmean)]
result2 = df.query('A < @Cmean and B < @Cmean')
print(np.allclose(result1, result2))
