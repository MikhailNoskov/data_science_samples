import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# iris = sns.load_dataset('iris')
# print(iris.head())

# sns.pairplot(iris, hue='species', height=1.5)
# plt.show()

# X_iris = iris.drop('species', axis=1)
# y_iris = iris['species']

# print(iris.shape)
# print(X_iris.shape)
# print(y_iris.shape)

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.scatter(x, y)
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
x = np.array(x)
X = x[:, np.newaxis]
model.fit(X, y)

xfit = np.linspace(-1, 11, 15)
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)
plt.scatter(Xfit, yfit)

plt.show()