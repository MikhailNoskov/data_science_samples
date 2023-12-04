import pandas as pd
import numpy as np


class Display:
    """Display HTML representation of multiple objects"""

    def __init__(self, *args):
        self.args = args
        self.template = """<div style="float: left; padding: 10px;"><p style='font-family:"Courier New", Courier, monospace'>{0}{1}"""

    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_()) for a in self.args)

    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a)) for a in self.args)


pop = pd.read_csv('data/state-population.csv')
areas = pd.read_csv('data/state-areas.csv')
abbrevs = pd.read_csv('data/state-abbrevs.csv')

print(Display('pop.head()', 'areas.head()', 'abbrevs.head()'))

merged = pd.merge(pop, abbrevs, how='outer', left_on='state/region', right_on='abbreviation')
merged = merged.drop('abbreviation', axis=1)  # drop duplicate info
print(merged.head())

print(merged.isnull().any())  # Check if any values are null in any column

print(merged[merged['population'].isnull()].head())
print(merged.loc[merged['state'].isnull(), 'state/region'].unique())

merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'

print(merged.isnull().any())

final = pd.merge(merged, areas, on='state', how='left')
print(final.head(10))

print(final.isnull().any())
print( final['state'][final['area (sq. mi)'].isnull()].unique())

final.dropna(inplace=True)
data2010 = final.query("year == 2010 & ages == 'total'")
print(data2010.head())

data2010.set_index('state', inplace=True)
density = data2010['population'] / data2010['area (sq. mi)']
density.sort_values(ascending=False, inplace=True)

print(density)