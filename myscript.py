import numpy as np

name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

x = np.zeros(4, dtype=int)

print(x)

data = np.zeros(4, dtype={'names': ('name', 'age', 'weight'), 'formats': ('U10', 'i4', 'f8')})

print(data)
print(data.dtype)

data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)

print(data[-1]['age'])
print(data['age'])
