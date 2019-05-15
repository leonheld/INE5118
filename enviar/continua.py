#Distribuição Contínua baseada em HPs de um Pokemon. Range teórica: Todos os reais positivos

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import collections

#configurações pra usar LaTeX nas legendas
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
sns.set(style = "darkgrid", context = "paper")

#usei regex do vim mais alguns macros. Daria pra usar pandas, mas eu prefiro usar np.array do que dataframes.
total = [45, 60, 80, 80, 39, 58, 78, 78, 78, 44, 59, 79, 79, 45, 50, 60, 40, 45, 65, 65, 40, 63, 83, 83, 30, 55, 40, 65, 35, 60, 35, 60, 50, 75, 55, 70, 90, 46, 61, 81, 70, 95, 38, 73, 1, 5, 1, 0, 40, 75, 45, 60, 75, 35, 60, 60, 70, 10, 35, 40, 65, 50, 80, 40, 65, 55, 90, 40, 65, 90, 25, 40, 55, 55, 70, 80, 90, 50, 65, 80, 40, 80, 40, 55, 80, 50, 65, 90, 95, 95, 25, 50, 52, 35, 60, 65, 90, 80, 1, 5, 30, 50, 30, 45, 60, 60, 35, 60, 85, 30, 55, 40, 60, 60, 95, 50, 60, 50, 50, 90, 40, 65, 80, 1, 5, 2, 0, 65, 1, 5, 1, 5, 30, 55, 45, 80, 30, 60, 40, 70, 65, 65, 65, 65, 65, 75, 20, 95, 95, 1, 0, 48, 55, 1, 0, 65, 65, 65, 35, 70, 30, 60, 80, 80, 1, 0, 90, 90, 90, 41, 61, 91, 1, 6, 1, 6, 1, 6, 1, 0, 45, 60, 80, 39, 58, 78, 50, 65, 85, 35, 85, 60, 1, 0, 40, 55, 40, 70, 85, 75, 1, 5, 20, 50, 90, 35, 55, 40, 65, 55, 70, 90, 90, 75, 70, 1, 0, 70, 90, 35, 55, 75, 55, 30, 75, 65, 55, 95, 65, 95, 60, 95, 60, 48, 1, 0, 70, 50, 75, 1, 0, 65, 75, 75, 60, 90, 65, 70, 70, 20, 80, 80, 55, 60, 90, 40, 50, 50, 1, 0, 55, 35, 75, 45, 65, 65, 45, 75, 75, 75, 90, 90, 85, 73, 55, 35, 50, 45, 45, 45, 95, 2, 5, 90, 1, 5, 1, 0, 50, 70, 1, 0, 1, 0, 1, 6, 1, 6, 1, 0, 40, 50, 70, 70, 45, 60, 80, 80, 50, 70, 1, 0, 1, 0, 35, 70, 38, 78, 45, 50, 60, 50, 60, 40, 60, 80, 40, 70, 90, 40, 60, 40, 60, 28, 38, 68, 68, 40, 70, 60, 60, 60, 80, 1, 0, 31, 61, 1, 64, 84, 1, 4, 72, 1, 4, 50, 30, 50, 70, 50, 50, 50, 50, 50, 60, 70, 70, 30, 60, 60, 40, 70, 70, 60, 60, 65, 65, 50, 70, 1, 0, 45, 70, 70, 1, 0, 1, 0, 60, 70, 70, 70, 60, 80, 60, 45, 50, 80, 50, 70, 45, 75, 75, 73, 73, 70, 70, 50, 1, 0, 43, 63, 40, 60, 66, 86, 45, 75, 20, 95, 70, 60, 44, 64, 64, 20, 40, 99, 65, 65, 65, 95, 50, 80, 80, 70, 90, 1, 0, 35, 55, 55, 1, 0, 43, 45, 65, 95, 95, 40, 60, 80, 80, 80, 80, 80, 80, 80, 80, 80, 1, 0, 1, 0, 1, 0, 1, 0, 1, 5, 1, 5, 1, 0, 50, 50, 50, 50, 55, 75, 95, 44, 64, 76, 53, 64, 84, 40, 55, 85, 59, 79, 37, 77, 45, 60, 80, 40, 60, 67, 97, 30, 60, 40, 60, 60, 60, 70, 30, 70, 60, 55, 85, 45, 70, 76, 1, 1, 75, 90, 1, 0, 55, 65, 65, 60, 1, 0, 49, 71, 45, 63, 1, 3, 57, 67, 50, 20, 1, 0, 76, 50, 58, 68, 1, 8, 1, 8, 1, 5, 40, 70, 70, 68, 1, 8, 40, 70, 48, 83, 74, 49, 69, 45, 60, 90, 90, 70, 70, 1, 0, 1, 5, 1, 0, 75, 75, 85, 86, 65, 65, 75, 1, 0, 85, 68, 68, 60, 45, 70, 50, 50, 50, 50, 50, 50, 75, 80, 75, 1, 0, 90, 91, 1, 0, 1, 0, 1, 0, 1, 0, 80, 1, 0, 70, 1, 0, 1, 0, 1, 0, 1, 0, 45, 60, 75, 65, 90, 1, 0, 55, 75, 95, 45, 60, 45, 65, 85, 41, 64, 50, 75, 50, 75, 50, 75, 76, 1, 6, 50, 62, 80, 45, 75, 55, 70, 85, 55, 67, 60, 1, 0, 1, 3, 1, 3, 75, 85, 1, 5, 50, 75, 1, 5, 1, 0, 75, 45, 55, 75, 30, 40, 60, 40, 60, 45, 70, 70, 50, 60, 95, 70, 1, 5, 1, 5, 75, 50, 70, 50, 65, 72, 38, 58, 54, 74, 55, 75, 50, 80, 40, 60, 55, 75, 45, 60, 70, 45, 65, 1, 0, 62, 75, 36, 51, 71, 60, 80, 55, 50, 70, 69, 1, 4, 55, 1, 0, 1, 5, 50, 70, 44, 74, 40, 60, 60, 35, 65, 85, 55, 75, 50, 60, 60, 46, 66, 76, 55, 95, 70, 50, 80, 1, 9, 45, 65, 77, 59, 89, 45, 65, 95, 70, 1, 0, 70, 1, 0, 85, 58, 52, 72, 92, 55, 85, 91, 91, 91, 79, 79, 79, 79, 1, 0, 1, 0, 89, 89, 1, 5, 1, 5, 1, 5, 91, 91, 1, 0, 1, 0, 71, 56, 61, 88, 40, 59, 75, 41, 54, 72, 38, 85, 45, 62, 78, 38, 45, 80, 62, 86, 44, 54, 78, 66, 1, 3, 67, 95, 75, 62, 74, 74, 45, 59, 60, 60, 78, 1, 1, 62, 82, 53, 86, 42, 72, 50, 65, 50, 71, 44, 62, 58, 82, 77, 1, 3, 95, 78, 67, 50, 45, 68, 90, 57, 43, 85, 49, 44, 54, 59, 65, 55, 75, 85, 55, 95, 40, 85, 1, 6, 1, 6, 1, 8, 50, 50, 80, 80, 80]
#também tirei valores menores do que 10, pois tem vários menores que realmente não importam. O dataset incluiu eles por motivo de completude, apenas
total_filtered = (x for x in total if x > 10)
total = list(total_filtered)

#aproximação pela normal
mu = np.mean(total)
sigma = np.std(total)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

plot_normal = plt.plot(x, stats.norm.pdf(x, mu, sigma)) #plot da aproximação normal
plot_dist = sns.distplot(total, kde=True, norm_hist=1, color = "#3dc1ff") #plot da distribuição, a opção kde=True dá uma aproximação calculada internamente pela função	

plt.xlabel(r'HP')
plt.ylabel(r'frequência relativa')
plt.title(r"Distribuição de HP de Pokémons")
plt.show()