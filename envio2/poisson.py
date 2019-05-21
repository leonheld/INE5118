import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import collections
import scipy
from scipy.stats import poisson
from scipy.stats import norm
from math import sqrt

sns.set(style = "darkgrid", context = "paper")
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def poipmf(start, stop, lamb):
	k = np.arange(start, stop, 1)
	pmf = scipy.stats.poisson.pmf(k, lamb)

	mu = lamb
	sigma = sqrt(lamb)

	x = np.linspace(mu - 5*sigma, mu + 5*sigma, 100)

	plt.plot(x, scipy.stats.norm.pdf(x, mu, sigma), color = '#353131')
	plt.stem(k, pmf, '--', bottom=0)
	plt.title(r"Poisson Normal Appr. with $\lambda$ = %d" % (lamb))
	plt.show()

lamb = [1, 5, 10, 200]

poipmf(0, 13, lamb[0]) 
poipmf(0, 17, lamb[1]) 
poipmf(0, 25, lamb[2]) 
poipmf(0, 200, lamb[3]) 