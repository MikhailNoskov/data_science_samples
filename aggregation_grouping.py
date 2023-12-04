import pandas as pd
import numpy as np
import seaborn as sns


class Display:
    """Display HTML representation of multiple objects"""

    def __init__(self, *args):
        self.args = args
        self.template = """<div style="float: left; padding: 10px;"><p style='font-family:"Courier New", Courier, monospace'>{0}{1}"""

    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_()) for a in self.args)

    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a)) for a in self.args)


planets = sns.load_dataset('planets')
# print(planets.shape)
# print(planets.head())
# rng = np.random.RandomState(42)
# ser = pd.Series(rng.rand(5))
# print(ser)
# print(ser.sum())
# print(ser.mean())

# df = pd.DataFrame({'A': rng.rand(5), 'B': rng.rand(5)})
#
# print(df.mean())
# print(df.mean(axis=1))
# print(df.mean(axis='columns'))  # the same as above - mean in rows

# print(planets.dropna().describe())  # Basic statistics

# df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'], 'data': range(6)}, columns=['key', 'data'])
# print(df)
# print(df.groupby('key'))
# print(df.groupby('key').max())
# print(df.groupby('key').sum())

# print(planets.groupby('method')['year'].describe().unstack())

# rng = np.random.RandomState(0)
# df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'], 'data1': range(6), 'data2': rng.randint(0, 10, 6)}, columns = ['key', 'data1', 'data2'])
# print(df)
# print(df.groupby('key').aggregate(['min', np.median, max]))

# print(df.groupby('key').aggregate({'data1': ['min', 'max'], 'data2': 'max'}))

# Filtering


# def filter_func(x):
#     return x['data2'].std() > 4
#
#
# print(Display('df', "df.groupby('key').std()", "df.groupby('key').filter(filter_func)"))


def center(x) :
    return x - x.mean()


# print(df)
# print(df.groupby('key').transform(center))
#
# L = [0, 1, 0, 1, 2, 0]
# print(df.groupby(L).sum())
# print(df.groupby(df['key']).sum())

# df2 = df.set_index('key')
# print(df2)
# mapping = {'A': 'vowel', 'B': 'consonant', 'C': 'consonant'}
# print(Display('df2', 'df2.groupby(mapping).sum()'))
# print(df2.groupby(str.lower).mean())
# print(df2.groupby([str.lower, mapping]).mean())

decade = 10 * (planets['year'] // 10)
decade = decade.astype(str) + 's'
decade.name = 'decade'
print(decade)
print(planets.groupby(['method', decade])['number'].sum().unstack().fillna(0))