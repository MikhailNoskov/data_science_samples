import numpy as np
import pandas as pd
import seaborn as sns


titanic = sns.load_dataset('titanic')
# print(titanic.head(15))
#
# print(titanic.groupby('sex')[['survived']].mean())

# print(titanic.groupby(['sex', 'class'], observed=False)['survived'].mean().unstack())
# print(titanic.groupby(['sex', 'class'], observed=True)['survived'].aggregate('mean').unstack())  # the same as above
# print(titanic.pivot_table('survived', index='sex', columns='class', aggfunc='mean'))  # also the same with pivot table

age = pd.cut(titanic['age'], [0, 18, 80])
# print(age)
# print(titanic.pivot_table('survived', ['sex', age], 'class'))

fare = pd.qcut(titanic['fare'], 2)
# print(fare)
# print(titanic.pivot_table('survived', ['sex', age], [fare, 'class'], 'count'))

# print(titanic.pivot_table(index='sex', columns='class', aggfunc={'survived': sum, 'fare': 'mean'}))
print(titanic.pivot_table('survived', index='sex', columns='class', margins=True, margins_name='Total'))