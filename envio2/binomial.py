import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from scipy.stats import binom	
from math import pi
from math import exp
from math import sqrt
from scipy import stats

sns.set(style = "darkgrid", context = "paper")
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def binpmf(start, stop, n, p):
	k = np.arange(start, stop, 1)
	pmf = scipy.stats.binom.pmf(k, n, p)

	mu = n*p;
	sigma = sqrt((n*p*(1 - p)))

	x = np.linspace(mu - 5*sigma, mu + 5*sigma, 1000)
	plt.stem(k, pmf, '--', bottom=0, basefmt = 'C0-')
	plot_normal = plt.plot(x, scipy.stats.norm.pdf(x, mu, sigma), linestyle='-', color = '#353131')
	plt.title(r"Binomial Normal Appr. with n = %d, p = %f" % (n, p))
	plt.show()

n = [10, 10, 10, 100, 100]
p = [0.95, 0.05, 0.5, 0.05, 0.95] 

for i in range(0, 3):
	binpmf(1, 12, n[i], p[i])

for i in range(3,5):
	binpmf(1, 100, n[i], p[i])