import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import collections
import scipy
from scipy.stats import binom

#Seaborn, pra deixar bonitinho
sns.set(style = "darkgrid", context = "paper")

def binpmf(start, stop, n, p):
	k = np.arange(start, stop, 1) #start, stop, step
	pmf = scipy.stats.binom.pmf(k, n, p)
	plt.stem(k, pmf, '-.', bottom=0)
	plt.show()

n = [10, 10, 10, 100, 100]
p = [0.95, 0.05, 0.5, 0.05, 0.95]

for i in range(0, 3):
	binpmf(1, 10, n[i], p[i])

for i in range(3,5):
	binpmf(1, 100, n[i], p[i])




#k = np.arange(1, 11, 1) #start, stop, step
#pmf = scipy.stats.binom.pmf(k, n[i], p[i])
#plt.stem(k, pmf, '-.', bottom=0)
#plt.show()