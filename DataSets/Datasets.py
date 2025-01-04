# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
#print('Libraries loaded')
# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)
#print('Dataset loaded')
#dataset shape 
print(dataset.shape)
# datsset head
print(dataset.head(30))
# Now we look at the datasets descriptions
#this is a summary of each attribute
# the mean, the min and max values as well as some percentiles
print(dataset.describe())

#Let’s now take a look at the number of instances (rows) that belong to each class. We can view this as an absolute count.

#class distribution
print(dataset.groupby('class').size())

x = "evans"
type(x)
