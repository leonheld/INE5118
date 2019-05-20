import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import collections

poke_table = pd.read_csv('Pokemon.csv')
numb = poke_table.Num
hp = poke_table.HP
total = poke_table.Total
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
sns.set(style = "darkgrid", context = "paper")

sns.distplot(total, kde=False, rug=False, hist=True, norm_hist=True)
plt.xlabel(r'\textbf{time} (s)')
plt.ylabel(r'\textbf{time} (s)')
plt.title(r"\TeX\ is Number "
          r"$\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!",
          fontsize=16, color='gray')
plt.show()