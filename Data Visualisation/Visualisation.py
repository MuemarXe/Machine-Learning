import sys
from DataSets import Datasets
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
#We start with some univariate plots, that is, plots of each individual variable.
#Given that the input variables are numeric, we can create box and whisker plots of each.
dataset = read_csv(url,names=names)
#print(dataset.shape)
#print(dataset.head(30))
# box and whisker plots
dataset.plot(kind ='box',subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
dataset.hist()
plt.show()
scatter_matrix(dataset)
plt.show()

#Validation Dataset
array =dataset.vales
X = array[:,0:4]
Y = array[:4]
X_train,X_validation,Y_train,Y_validation = train_test_split(X,Y,test_size=0.20,random_state=1)


