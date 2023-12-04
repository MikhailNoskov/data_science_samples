import pandas as pd
import numpy as np


def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data, ind)


class Display:
    """Display HTML representation of multiple objects"""

    def __init__(self, *args):
        self.args = args
        self.template = """<div style="float: left; padding: 10px;"><p style='font-family:"Courier New", Courier, monospace'>{0}{1}"""

    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_()) for a in self.args)

    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a)) for a in self.args)


# ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
# ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
#
# print(ser1)
# print(ser2)
#
# print(pd.concat([ser1, ser2]))
#
df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
#
# print(df1)
# print(df2)
#
# disp = Display('df1', 'df2', 'pd.concat([df1, df2])')
# print(disp)
#
# df3 = make_df('AB', [0, 1])
# df4 = make_df('CD', [0, 1])
# disp = Display('df3', 'df4', "pd.concat([df3, df4], axis='columns')")
# print(disp)

# x = make_df('AB', [0, 1])
# y = make_df('AB', [2, 3])
#
# disp = Display('x', 'y', 'pd.concat([x, y])')
# print(disp)
#
# y.index = x.index  # make indices match
# disp = Display('x', 'y', 'pd.concat([x, y])')
# print(disp)
#
# try:
#     print(pd.concat([x, y], verify_integrity=True))
# except ValueError as e:
#     print("ValueError:", e)
#
# disp = Display('x', 'y', 'pd.concat([x, y], ignore_index=True)')
# print(disp)
#
# disp = Display('x', 'y', "pd.concat([x, y], keys=['x', 'y'])")
# print(disp)

# df5 = make_df('ABC', [1, 2])
# df6 = make_df('BCD', [3, 4])
# disp = Display('df5', 'df6', 'pd.concat([df5, df6])')
# print(disp)
#
# disp = Display('df5', 'df6', "pd.concat([df5, df6], join='inner')")  # Default join='outer'
# print(disp)
#
# print(pd.concat([df5, df6.reindex(df5.columns, axis=1)]))

disp = Display('df1', 'df2', 'df1._append(df2)')
print(disp)
