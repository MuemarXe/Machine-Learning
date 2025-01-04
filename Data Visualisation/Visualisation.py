import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt

#We start with some univariate plots, that is, plots of each individual variable.
#Given that the input variables are numeric, we can create box and whisker plots of each.

# box and whisker plots
dataset.plt(kind ='box',subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()



