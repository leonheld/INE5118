from scipy.stats import binom
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

n, p = 5, 0.4

data_binom = binom.rvs(n=20, p=0.8, loc=0, size=100000)
sns.distplot(data_binom, kde = False)
plt.show()