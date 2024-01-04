import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn import metrics

from sklearn.metrics import confusion_matrix
import seaborn as sns

plt.style.use('seaborn-whitegrid')

# rng = np.random.RandomState(42)
# x = 10 * rng.rand(200)
#
#
# def model(x, sigma=0.3):
#     fast_oscillation = np.sin(5 * x)
#     slow_oscillation = np.sin(0.5 * x)
#     noise = sigma * rng.randn(len(x))
#     return slow_oscillation + fast_oscillation + noise
#
#
# y = model(x)
# # plt.errorbar(x, y, 0.3, fmt='o', ecolor='red')
#
# forest = RandomForestRegressor(200)
# forest.fit(x[:, None], y)
# xfit = np.linspace(0, 10, 1000)
# yfit = forest.predict(xfit[:, None])
# ytrue = model(xfit, sigma=0)
#
# plt.errorbar(x, y, 0.3, fmt='o', alpha=0.5)
# plt.plot(xfit, yfit, '-r')
# plt.plot(xfit, ytrue, '-k', alpha=0.5)

# Example: Random Forest for Classifying Digits

digits = load_digits()
# print(digits.keys())

# set up the figure
# fig = plt.figure(figsize=(6, 6)) # figure size in inches
# fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.1, wspace=0.1)

# plot the digits: each image is 8x8 pixels
# for i in range(64):
#     ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
#     ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
#     # label the image with the target value
#     ax.text(0, 7, str(digits.target[i]))

Xtrain, Xtest, ytrain, ytest = train_test_split(digits.data, digits.target, random_state=0)
# model = RandomForestRegressor(n_estimators=1000)
model = RandomForestClassifier(n_estimators=1000)

model.fit(Xtrain, ytrain)
ypred = model.predict(Xtest)

print(metrics.classification_report(ypred, ytest))

# Confusion matrix

mat = confusion_matrix(ytest, ypred)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False, cmap='Blues')
plt.xlabel('true label')
plt.ylabel('predicted label')

# set up the figure
# fig, axes = plt.subplots(6, 6, figsize=(8, 8),
#                          subplot_kw={'xticks': [], 'yticks': []},
#                          gridspec_kw=dict(hspace=0.1, wspace=0.1))
#
# test_images = Xtest.reshape(-1, 8, 8)
# for i, ax in enumerate(axes.flat):
#     ax.imshow(test_images[i], cmap='binary', interpolation='nearest')
#     ax.text(0.05, 0.05, str(round(ypred[i], 0)),
#             transform=ax.transAxes,
#             color='green' if (int(ytest[i]) == int(round(ypred[i], 0))) else 'red')

plt.show()