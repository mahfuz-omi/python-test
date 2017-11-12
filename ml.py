import scipy
import numpy
import matplotlib
import pandas
import sklearn



# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# head
print(dataset.head(20))

# descriptions
print(dataset.describe())

dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
matplotlib.pyplot.show()


dataset.hist()
matplotlib.pyplot.show()


# scatter plot matrix
pandas.scatter_matrix(dataset)
matplotlib.pyplot.show()