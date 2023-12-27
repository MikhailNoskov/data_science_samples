import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA

# Iris sample
#
iris = sns.load_dataset('iris')
# print(iris.head())
# # sns.pairplot(iris, hue='species', height=1.5)
# # plt.show()
X_iris = iris.drop('species', axis=1)
# print(X_iris.shape)
y_iris = iris['species']
# print(y_iris.shape)


# Supervised Learning Example: Simple Linear Regression

# rng = np.random.RandomState(42)
# x = 10 * rng.rand(50)
# y = 2 * x - 1 + rng.randn(50)
# plt.scatter(x, y)
# plt.show()
# model = LinearRegression(fit_intercept=True)
# X = x[:, np.newaxis]
# model.fit(X, y)
# xfit = np.linspace(-1, 11)
# Xfit = xfit[:, np.newaxis]
#
# yfit = model.predict(Xfit)
#
# plt.scatter(x, y)
# plt.scatter(xfit, yfit, cmap='Red')
# plt.plot(xfit, yfit)

# Supervised Learning Example: Iris Classication

# Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris, random_state=1)
# model = GaussianNB()  # 2. instantiate model
# model.fit(Xtrain, ytrain)  # 3. fit model to data
# y_model = model.predict(Xtest)  # 4. predict on new data
#
# print(accuracy_score(ytest, y_model))

# Unsupervised Learning Example: Iris Dimensionality

model = PCA(n_components=2)  # 2. instantiate model
model.fit(X_iris)  # 3. fit model to data
X_2D = model.transform(X_iris)  # 4. transform the data

iris['PCA1'] = X_2D[:, 0]
iris['PCA2'] = X_2D[:, 1]

# sns.lmplot(x="PCA1", y="PCA2", hue='species', data=iris, fit_reg=False)
#
# # Unsupervised Learning Example: Iris Clustering
#
from sklearn.mixture import GaussianMixture

model = GaussianMixture(n_components=3, covariance_type='full')  # 2. instantiate model
model.fit(X_iris)  # 3. fit model to data
y_gmm = model.predict(X_iris)  # 4. determine labels
iris['cluster'] = y_gmm
sns.lmplot(x="PCA1", y="PCA2", data=iris, hue='species',col='cluster', fit_reg=False)
plt.show()