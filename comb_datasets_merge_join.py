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


# df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'], 'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
# df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'], 'hire_date': [2004, 2008, 2012, 2014]})
#
#
# print(Display('df1', 'df2'))
#
# df3 = pd.merge(df1, df2)
# print(df3)
#
# df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'], 'supervisor': ['Carly', 'Guido', 'Steve']})
# print(Display('df3', 'df4', 'pd.merge(df3, df4)'))

# df5 = pd.DataFrame({'group': ['Accounting', 'Accounting', 'Engineering', 'Engineering', 'HR', 'HR'],
#                     'skills': ['math', 'spreadsheets', 'software', 'math', 'spreadsheets', 'organization']})
#
# print(Display('df1', 'df5', "pd.merge(df1, df5)"))

# print(Display('df1', 'df2', "pd.merge(df1, df2, on='employee')"))
# df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
#                     'salary': [70000, 80000, 120000, 90000]})
#
# print(Display('df1', 'df3', 'pd.merge(df1, df3, left_on="employee", right_on="name")'))
# result = pd.merge(df1, df3, left_on="employee", right_on="name").drop('employee', axis=1)
# print(result)

# df1a = df1.set_index('employee')
# df2a = df2.set_index('employee')

# print(df1a)
# print(df2a)
# print(pd.merge(df1a, df2a, left_index=True, right_index=True))
#
# print(df1a.join(df2a))  # The same as merge above

# print(Display('df1a', 'df3', "pd.merge(df1a, df3, left_index=True, right_on='name')"))

# df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'], 'food': ['fish', 'beans', 'bread']}, columns=['name', 'food'])
# df7 = pd.DataFrame({'name': ['Mary', 'Joseph'], 'drink': ['wine', 'beer']}, columns=['name', 'drink'])
# print(Display('df6', 'df7', 'pd.merge(df6, df7, how="outer")'))
# print(Display('df6', 'df7', 'pd.merge(df6, df7, how="left")'))
# print(Display('df6', 'df7', 'pd.merge(df6, df7, how="right")'))

df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'], 'rank': [1, 2, 3, 4]})
df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'], 'rank': [3, 1, 4, 2]})

# print(Display('df8', 'df9', 'pd.merge(df8, df9, df10, on="name")'))
# print(Display('df8', 'df9', 'pd.merge(df8, df9, on="name", suffixes=["_L", "_R"])'))

print(pd.merge(df8, df9, on='name'))