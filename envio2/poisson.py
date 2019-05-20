import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import collections
import scipy
from scipy.stats import poisson
from scipy.stats import norm

sns.set(style = "darkgrid", context = "paper")

def poi(start, stop, λ):
	k = np.arange(start, stop, 1)
	pmf = scipy.stats.poisson.pmf(k, λ)

	mu = np.mean(pmf)
	sigma = np.std(pmf)

	x = np.linspace(start, stop, 1000)
	#x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

	plt.plot(x, scipy.stats.norm.pdf(x, mu, sigma))
	plt.stem(k, pmf, '-.', bottom=0)
	plt.show()

λ = [1, 5, 10, 200]

poi(0, 13, λ[0]) 
poi(0, 17, λ[1]) 
poi(0, 25, λ[2]) 
poi(0, 200, λ[3]) 