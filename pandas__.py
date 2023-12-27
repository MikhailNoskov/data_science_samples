import numpy as np
import pandas as pd

population_dict = {'California': 39538223, 'Texas': 29145505, 'Florida': 21538187, 'New York': 20201249, 'Pennsylvania': 13002700}
population = pd.Series(population_dict)
area_dict = {'California': 423967, 'Texas': 695662, 'Florida': 170312, 'New York': 141297, 'Pennsylvania': 119280}
area = pd.Series(area_dict)
capitals = {'California': 'LA', 'Texas': 'Texas', 'Florida': 'Miami', 'New York': 'New York', 'Pennsylvania': 'Pitsburg'}

states = pd.DataFrame({'population': population, 'area': area, 'capitals': capitals})
# print(population)
# print(area)
# print(states)
# print(states.columns)
# print(states.index)
# print(states.area['Texas'])
#
# matrix = np.random.rand(3, 2)
# pandas_matrix = pd.DataFrame(matrix, columns=['foo', 'bar'], index=['a', 'b', 'c'])
# print(matrix)
# print(pandas_matrix)
print(states)