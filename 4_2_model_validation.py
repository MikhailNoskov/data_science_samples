from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score


iris = load_iris()
X = iris.data
y = iris.target

# print(X)
# print(y)


# Model Validation the Wrong Way

model = KNeighborsClassifier(n_neighbors=1)
# model.fit(X, y)
# y_model = model.predict(X)

# print(accuracy_score(y, y_model))

# Model Validation the Right Way: Holdout Sets

# X1, X2, y1, y2 = train_test_split(X, y, random_state=0, train_size=0.5)
# model.fit(X1, y1)
#
# y2_model = model.predict(X2)
# print(accuracy_score(y2, y2_model))

# Model Validation via Cross-Validation

# y2_model = model.fit(X1, y1).predict(X2)
# y1_model = model.fit(X2, y2).predict(X1)
# print(accuracy_score(y1, y1_model), accuracy_score(y2, y2_model))

# print(cross_val_score(model, X, y, cv=5))


# Train on each member separately

from sklearn.model_selection import LeaveOneOut
scores = cross_val_score(model, X, y, cv=LeaveOneOut())

print(scores)
print(scores.mean())