import pandas as pd


# data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
# names = pd.Series(data)
# names = names.str.capitalize()
# print(names)
#
monte = pd.Series(['Graham Chapman', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones', 'Michael Palin'])
# print(monte.str.extract('([A-Za-z]+)', expand=False))  # Extract first name
# print(monte.str.findall(r'^[^AEIOU].*[^aeiou]$'))
# print(monte.str.split().str[-1])  # Extract last name

full_monte = pd.DataFrame({'name': monte, 'info': ['B|C|D', 'B|D', 'A|C', 'B|D', 'B|C', 'B|C|D']})
print(full_monte)
print(full_monte['info'].str.get_dummies('|'))  # Split out info indicator variables into a DataFrame
