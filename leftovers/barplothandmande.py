import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import collections
from collections import Counter

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
sns.set(style = "darkgrid", context = "paper")

#usei regex do vim pra criar esse vetor, pouca coisa pra usar pandas
#Total
#total = [318, 405, 525, 625, 309, 405, 534, 634, 634, 314, 405, 530, 630, 195, 205, 395, 195, 205, 395, 495, 251, 349, 479, 579, 253, 413, 262, 442, 288, 438, 320, 485, 300, 450, 275, 365, 505, 273, 365, 505, 323, 483, 299, 505, 270, 435, 245, 455, 320, 395, 490, 285, 405, 305, 450, 265, 405, 290, 440, 320, 500, 305, 455, 350, 555, 300, 385, 510, 310, 400, 500, 590, 305, 405, 505, 300, 390, 490, 335, 515, 300, 390, 495, 410, 500, 315, 490, 590, 325, 465, 352, 310, 460, 325, 475, 325, 500, 305, 525, 310, 405, 500, 600, 385, 328, 483, 325, 475, 330, 480, 325, 520, 320, 425, 455, 455, 385, 340, 490, 345, 485, 450, 435, 490, 590, 295, 440, 320, 450, 340, 520, 460, 500, 455, 490, 495, 500, 600, 490, 200, 540, 640, 535, 288, 325, 525, 525, 525, 395, 355, 495, 355, 495, 515, 615, 540, 580, 580, 580, 300, 420, 600, 680, 780, 780, 600, 318, 405, 525, 309, 405, 534, 314, 405, 530, 215, 415, 262, 442, 265, 390, 250, 390, 535, 330, 460, 205, 218, 210, 245, 405, 320, 470, 280, 365, 510, 610, 490, 250, 420, 410, 500, 250, 340, 460, 360, 180, 425, 390, 210, 430, 525, 525, 405, 490, 435, 336, 405, 455, 290, 465, 415, 430, 510, 610, 300, 450, 430, 500, 600, 505, 500, 600, 430, 330, 500, 250, 410, 250, 450, 380, 300, 480, 330, 465, 465, 330, 500, 600, 540, 330, 500, 515, 465, 250, 210, 455, 305, 360, 365, 490, 540, 580, 580, 580, 300, 410, 600, 700, 680, 680, 600, 310, 405, 530, 630, 310, 405, 530, 630, 310, 405, 535, 635, 220, 420, 240, 420, 195, 205, 395, 205, 385, 220, 340, 480, 220, 340, 480, 270, 430, 270, 430, 198, 278, 518, 618, 269, 414, 295, 460, 280, 440, 670, 266, 456, 236, 240, 360, 490, 237, 474, 190, 375, 260, 380, 380, 480, 380, 480, 330, 430, 530, 630, 280, 410, 510, 295, 475, 575, 405, 405, 400, 400, 400, 302, 467, 305, 460, 560, 400, 500, 305, 460, 560, 470, 330, 470, 360, 290, 340, 520, 335, 475, 310, 490, 590, 458, 458, 440, 440, 288, 468, 308, 468, 300, 500, 355, 495, 355, 495, 200, 540, 420, 440, 295, 455, 555, 295, 455, 460, 425, 465, 565, 260, 300, 480, 580, 290, 410, 530, 345, 485, 485, 485, 330, 300, 420, 600, 700, 300, 420, 600, 700, 580, 580, 580, 600, 700, 600, 700, 670, 770, 670, 770, 680, 780, 600, 600, 600, 600, 600, 318, 405, 525, 309, 405, 534, 314, 405, 530, 245, 340, 485, 250, 410, 194, 384, 263, 363, 523, 280, 515, 350, 495, 350, 495, 224, 424, 424, 424, 424, 244, 474, 405, 330, 495, 275, 450, 325, 475, 482, 348, 498, 350, 480, 580, 495, 505, 310, 452, 285, 329, 479, 300, 500, 290, 310, 220, 411, 485, 300, 410, 600, 700, 390, 285, 525, 625, 330, 525, 330, 500, 300, 490, 454, 330, 460, 345, 334, 494, 594, 510, 535, 515, 535, 535, 540, 540, 545, 515, 525, 525, 510, 530, 535, 518, 618, 525, 525, 480, 440, 520, 520, 520, 520, 520, 580, 580, 580, 680, 680, 600, 670, 680, 680, 600, 480, 600, 600, 600, 600, 720, 600, 308, 413, 528, 308, 418, 528, 308, 413, 528, 255, 420, 275, 370, 500, 281, 446, 316, 498, 316, 498, 316, 498, 292, 487, 264, 358, 488, 295, 497, 280, 390, 515, 313, 425, 328, 508, 445, 545, 305, 405, 505, 294, 384, 509, 465, 465, 310, 380, 500, 260, 360, 485, 280, 480, 280, 480, 460, 292, 351, 519, 315, 480, 540, 461, 325, 475, 348, 488, 490, 303, 483, 355, 495, 401, 567, 329, 474, 330, 510, 300, 470, 290, 390, 490, 290, 370, 490, 305, 473, 305, 395, 535, 335, 475, 428, 315, 495, 294, 464, 335, 480, 470, 319, 472, 305, 489, 300, 440, 520, 275, 405, 515, 335, 485, 275, 370, 520, 320, 410, 540, 305, 485, 485, 305, 495, 471, 350, 510, 485, 303, 483, 340, 490, 490, 350, 510, 370, 510, 484, 484, 300, 420, 600, 360, 550, 580, 580, 580, 580, 580, 580, 580, 680, 680, 600, 600, 660, 700, 700, 580, 580, 600, 600, 600, 313, 405, 530, 307, 409, 534, 314, 405, 530, 237, 423, 278, 382, 499, 200, 213, 411, 369, 507, 303, 371, 552, 350, 531, 348, 495, 472, 355, 466, 466, 325, 448, 520, 520, 341, 462, 341, 480, 288, 482, 306, 500, 320, 494, 330, 500, 289, 481, 362, 521, 362, 521, 525, 500, 431, 500, 300, 452, 600, 470, 309, 474, 335, 335, 335, 335, 494, 494, 494, 494, 304, 514, 245, 535, 680, 680, 600, 600, 700, 600, 680, 600]
#HP
total = [45, 60, 80, 80, 39, 58, 78, 78, 78, 44, 59, 79, 79, 45, 50, 60, 40, 45, 65, 65, 40, 63, 83, 83, 30, 55, 40, 65, 35, 60, 35, 60, 50, 75, 55, 70, 90, 46, 61, 81, 70, 95, 38, 73, 1, 5, 1, 0, 40, 75, 45, 60, 75, 35, 60, 60, 70, 10, 35, 40, 65, 50, 80, 40, 65, 55, 90, 40, 65, 90, 25, 40, 55, 55, 70, 80, 90, 50, 65, 80, 40, 80, 40, 55, 80, 50, 65, 90, 95, 95, 25, 50, 52, 35, 60, 65, 90, 80, 1, 5, 30, 50, 30, 45, 60, 60, 35, 60, 85, 30, 55, 40, 60, 60, 95, 50, 60, 50, 50, 90, 40, 65, 80, 1, 5, 2, 0, 65, 1, 5, 1, 5, 30, 55, 45, 80, 30, 60, 40, 70, 65, 65, 65, 65, 65, 75, 20, 95, 95, 1, 0, 48, 55, 1, 0, 65, 65, 65, 35, 70, 30, 60, 80, 80, 1, 0, 90, 90, 90, 41, 61, 91, 1, 6, 1, 6, 1, 6, 1, 0, 45, 60, 80, 39, 58, 78, 50, 65, 85, 35, 85, 60, 1, 0, 40, 55, 40, 70, 85, 75, 1, 5, 20, 50, 90, 35, 55, 40, 65, 55, 70, 90, 90, 75, 70, 1, 0, 70, 90, 35, 55, 75, 55, 30, 75, 65, 55, 95, 65, 95, 60, 95, 60, 48, 1, 0, 70, 50, 75, 1, 0, 65, 75, 75, 60, 90, 65, 70, 70, 20, 80, 80, 55, 60, 90, 40, 50, 50, 1, 0, 55, 35, 75, 45, 65, 65, 45, 75, 75, 75, 90, 90, 85, 73, 55, 35, 50, 45, 45, 45, 95, 2, 5, 90, 1, 5, 1, 0, 50, 70, 1, 0, 1, 0, 1, 6, 1, 6, 1, 0, 40, 50, 70, 70, 45, 60, 80, 80, 50, 70, 1, 0, 1, 0, 35, 70, 38, 78, 45, 50, 60, 50, 60, 40, 60, 80, 40, 70, 90, 40, 60, 40, 60, 28, 38, 68, 68, 40, 70, 60, 60, 60, 80, 1, 0, 31, 61, 1, 64, 84, 1, 4, 72, 1, 4, 50, 30, 50, 70, 50, 50, 50, 50, 50, 60, 70, 70, 30, 60, 60, 40, 70, 70, 60, 60, 65, 65, 50, 70, 1, 0, 45, 70, 70, 1, 0, 1, 0, 60, 70, 70, 70, 60, 80, 60, 45, 50, 80, 50, 70, 45, 75, 75, 73, 73, 70, 70, 50, 1, 0, 43, 63, 40, 60, 66, 86, 45, 75, 20, 95, 70, 60, 44, 64, 64, 20, 40, 99, 65, 65, 65, 95, 50, 80, 80, 70, 90, 1, 0, 35, 55, 55, 1, 0, 43, 45, 65, 95, 95, 40, 60, 80, 80, 80, 80, 80, 80, 80, 80, 80, 1, 0, 1, 0, 1, 0, 1, 0, 1, 5, 1, 5, 1, 0, 50, 50, 50, 50, 55, 75, 95, 44, 64, 76, 53, 64, 84, 40, 55, 85, 59, 79, 37, 77, 45, 60, 80, 40, 60, 67, 97, 30, 60, 40, 60, 60, 60, 70, 30, 70, 60, 55, 85, 45, 70, 76, 1, 1, 75, 90, 1, 0, 55, 65, 65, 60, 1, 0, 49, 71, 45, 63, 1, 3, 57, 67, 50, 20, 1, 0, 76, 50, 58, 68, 1, 8, 1, 8, 1, 5, 40, 70, 70, 68, 1, 8, 40, 70, 48, 83, 74, 49, 69, 45, 60, 90, 90, 70, 70, 1, 0, 1, 5, 1, 0, 75, 75, 85, 86, 65, 65, 75, 1, 0, 85, 68, 68, 60, 45, 70, 50, 50, 50, 50, 50, 50, 75, 80, 75, 1, 0, 90, 91, 1, 0, 1, 0, 1, 0, 1, 0, 80, 1, 0, 70, 1, 0, 1, 0, 1, 0, 1, 0, 45, 60, 75, 65, 90, 1, 0, 55, 75, 95, 45, 60, 45, 65, 85, 41, 64, 50, 75, 50, 75, 50, 75, 76, 1, 6, 50, 62, 80, 45, 75, 55, 70, 85, 55, 67, 60, 1, 0, 1, 3, 1, 3, 75, 85, 1, 5, 50, 75, 1, 5, 1, 0, 75, 45, 55, 75, 30, 40, 60, 40, 60, 45, 70, 70, 50, 60, 95, 70, 1, 5, 1, 5, 75, 50, 70, 50, 65, 72, 38, 58, 54, 74, 55, 75, 50, 80, 40, 60, 55, 75, 45, 60, 70, 45, 65, 1, 0, 62, 75, 36, 51, 71, 60, 80, 55, 50, 70, 69, 1, 4, 55, 1, 0, 1, 5, 50, 70, 44, 74, 40, 60, 60, 35, 65, 85, 55, 75, 50, 60, 60, 46, 66, 76, 55, 95, 70, 50, 80, 1, 9, 45, 65, 77, 59, 89, 45, 65, 95, 70, 1, 0, 70, 1, 0, 85, 58, 52, 72, 92, 55, 85, 91, 91, 91, 79, 79, 79, 79, 1, 0, 1, 0, 89, 89, 1, 5, 1, 5, 1, 5, 91, 91, 1, 0, 1, 0, 71, 56, 61, 88, 40, 59, 75, 41, 54, 72, 38, 85, 45, 62, 78, 38, 45, 80, 62, 86, 44, 54, 78, 66, 1, 3, 67, 95, 75, 62, 74, 74, 45, 59, 60, 60, 78, 1, 1, 62, 82, 53, 86, 42, 72, 50, 65, 50, 71, 44, 62, 58, 82, 77, 1, 3, 95, 78, 67, 50, 45, 68, 90, 57, 43, 85, 49, 44, 54, 59, 65, 55, 75, 85, 55, 95, 40, 85, 1, 6, 1, 6, 1, 8, 50, 50, 80, 80, 80]

#values: vezes das ocorrencias
total_counter = Counter(total) #te dá qual o total e quantos desses foram encontrados

organized_total = dict(sorted(total_counter.items())) #organiza o dicionário por ordem de: TOTAL (crescente) - Ocorrências desse total

print(organized_total.values())
sum_of_values = sum(organized_total.values())

for value in organized_total:    #divide o número de ocorrencias pelo número total de ocorrencias, obtem as ocorrencias relativas
    organized_total[value] = organized_total[value]/sum_of_values 


#plt.bar(list(organized_total.keys()), organized_total.values(), width = 1, color='g')
plt.hist(organized_total.keys(), bins=5)



plt.xlabel(r'\textbf{time} (s)')
plt.ylabel(r'\textbf{time} (s)')
plt.title(r"\TeX\ is Number "
          r"$\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!",
          fontsize=16, color='gray')
plt.show()