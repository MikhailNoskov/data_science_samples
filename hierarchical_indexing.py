import pandas as pd
import numpy as np

#  Bad way
index = [('California', 2010), ('California', 2020), ('New York', 2010), ('New York', 2020), ('Texas', 2010), ('Texas', 2020)]
populations = [37253956, 39538223, 19378102, 20201249, 25145561, 29145505]

pop = pd.Series(populations, index=index)
# print(pop)
# print(pop[('California', 2020):('Texas', 2010)])
# print(pop[[i for i in pop.index if i[1] == 2010]])  # Slow

# Better way

index = pd.MultiIndex.from_tuples(index)
pop = pop.reindex(index=index)
# print(pop)
#
# print(pop[:, 2020])
# print(pop['California'])
# print(pop['California', 2010])

# Multiindex as extra dimension

# pop_df = pop.unstack()  # Indexes => into rows and columns
# print(pop_df)
#
# print(pop_df.stack())  # Indexes <= into rows and columns
# pop_df = pd.DataFrame({'total': pop,
#                        'under18': [9284094, 8898092, 4318033, 4181528, 6879014, 7432474]})
# print(pop_df)
#
# f_u18 = pop_df['under18'] / pop_df['total']  # ufuncs with multi-indexed dataframe
# print(f_u18.unstack())


# Methods of MultiIndex Creation

# df = pd.DataFrame(np.random.rand(4, 2),
#                   index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
#                   columns=['data1', 'data2'])
# print(df)
#
# data = {('California', 2010): 37253956,
#         ('California', 2020): 39538223,
#         ('New York', 2010): 19378102,
#         ('New York', 2020): 20201249,
#         ('Texas', 2010): 25145561,
#         ('Texas', 2020): 29145505}  # By dict
#
# ds = pd.Series(data)
#
# print(ds)
#
# ## Explicit MultiIndex Constructors
#
# indexes = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])
# print(indexes)
#
# indexes = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])
# print(indexes)
#
# indexes = pd.MultiIndex.from_product([['a', 'b', 'c'], [1, 2, 3]])
# print(indexes)
#
# indexes = pd.MultiIndex(levels=[['a', 'b'], [1, 2]], codes=[[0, 0, 1, 1], [0, 1, 0, 1]])
# print(indexes)
#
# pop.index.names = ['state', 'year']
# print(pop)

# MultiIndex for Columns
# index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]], names=['year', 'visit'])
# columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']], names=['subject', 'type'])
# data = np.round(np.random.randn(4, 6), 1)
# data[:, ::2] *= 10
# data += 37
# print(data)
#
# health_data = pd.DataFrame(data, index=index, columns=columns)
# print(health_data)
# print(health_data['Guido'])
# print(health_data.loc[2013:2014])
# idx = pd.IndexSlice
# print(health_data.loc[idx[:, 1], idx[:, :]])
# print(health_data.loc[idx[:, 2], idx[:, :]])

# Rearranging Multi-Indexes

index = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2]])
data = pd.Series(np.random.rand(6), index=index)
data.index.names = ['char', 'int']

print(data)
data = data.sort_index()
print(data['a':'b'])
# try:
#     data['a':'b']
# except KeyError as e:
#     print("KeyError", e)
pop.index.names = ['state', 'year']
print(pop.reset_index(name='population'))
df_pop = pop.reset_index(name='population')
print(df_pop.set_index(['state', 'year']))