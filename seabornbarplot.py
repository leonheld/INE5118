import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import collections

poke_table = pd.read_csv('Pokemon.csv')
numb = poke_table.Num
hp = poke_table.HP
total = poke_table.Total
sns.set(style = "darkgrid", context = "paper")
#ax = sns.distplot(hp, kde=True, rug=False)

sns.distplot(total, kde=True, rug=False)
#ax.set_xlabel('Group')
#ax.set_ylabel('Scores')
#ax.set_title('Scores by group and gender')
#ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
#ax.legend()
plt.show()
