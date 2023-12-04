import re
import numpy as np
import pandas as pd

recipes = pd.read_json('data/recipeitems/recipeitems.json', lines=True)
# print(recipes.ingredients.str.len().describe())
# print(np.argmax(recipes.ingredients.str.len()))  # Index of the longest recipe
# print(recipes.name[np.argmax(recipes.ingredients.str.len())])  # The longest recipe
# print(recipes.description.str.contains('[Bb]reakfast').sum())
# print(recipes.ingredients.str.contains('[Cc]innamon').sum())
# print(recipes.ingredients.str.contains('[Cc]inamon').sum())

# Simple ingredients recipe search

spice_list = ['salt', 'pepper', 'oregano', 'sage', 'parsley', 'rosemary', 'tarragon', 'thyme', 'paprika', 'cumin']
spice_df = pd.DataFrame({spice: recipes.ingredients.str.contains(spice, re.IGNORECASE) for spice in spice_list})
print(spice_df.head(20))
selection = spice_df.query('parsley & paprika & tarragon')
# print(len(selection))
# print(selection)
# print(selection.index)
# print(recipes.name[selection.index])
# print(recipes.columns)
print(recipes.ingredients[selection.index])
