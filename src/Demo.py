from sklearn import datasets

iris = datasets.load_iris()
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
print("GaussianNB")
print("Number of mislabeled points out of a total %d points : %d"
      % (iris.data.shape[0], (iris.target != y_pred).sum()))

from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
y_pred = clf.predict(iris.data)
print("DecisionTree")
print("Number of mislabeled points out of a total %d points : %d"
      % (iris.data.shape[0], (iris.target != y_pred).sum()))

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris()
clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(iris.data, iris.target)
y_pred = clf.predict(iris.data)
print("LogisticRegression")
print("Number of mislabeled points out of a total %d points : %d"
      % (iris.data.shape[0], (iris.target != y_pred).sum()))

from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
iris = load_iris()
clf = LinearRegression().fit(iris.data, iris.target)
y_pred = clf.predict(iris.data)
print("LinearRegression")
print("Number of mislabeled points out of a total %d points : %d"
      % (iris.data.shape[0],(iris.target != y_pred).sum()))