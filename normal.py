#envio4
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:52:39 2019

@author: Leon
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from scipy import stats
import pandas as pd
import random

bw = []

with open('bodyweight.txt') as inputfile:
    for line in inputfile:
        bw.append(float(line.strip()))
        
#parâmetros de normal da mediaAmostraCinco
mubw = np.mean(bw)
sigmabw = np.std(bw)

mediaAmostraCinco = []
for i in range(1, 1000):
	amostraCinco = random.sample(population = bw, k = 5)
	mediaAmostraCinco.append(np.mean(amostraCinco))
    
#parâmetros de normal da mediaAmostraCinco
muAmostraCinco = np.mean(mediaAmostraCinco)
sigmaAmostraCinco = np.std(mediaAmostraCinco)

mediaAmostraCinquenta = []
for i in range(1, 1000):
	amostraCinquenta = random.sample(population = bw, k = 50)
	mediaAmostraCinquenta.append(np.mean(amostraCinquenta))

#parâmetros de normal da mediaAmostraCinquenta
muAmostraCinquenta = np.mean(mediaAmostraCinquenta)
sigmaAmostraCinquenta = np.std(mediaAmostraCinquenta)

plt.figure(1)
sns.distplot(bw, kde=False, norm_hist=1, color = "#3dc1ff")
             
axes = plt.gca()
axes.set_xlim([0, 40])
axes.set_ylim([0, 0.175])
plt.figure(2)
sns.distplot(mediaAmostraCinco, kde=False, norm_hist=1, color = "#3dc1ff")
             
axes = plt.gca()
axes.set_xlim([0, 40])
axes.set_ylim([0, 0.3])
plt.figure(3)
sns.distplot(mediaAmostraCinquenta, kde=False, norm_hist=1, color = "#3ddacf")
             
axes = plt.gca()
axes.set_xlim([0, 40])
axes.set_ylim([0, 1])
             
             
plt.show()
