import matplotlib.pyplot as plt
import random as rd
N = 100
random_list = rd.choices(range(1,100), k = N)
print(random_list)

mean = sum(random_list)/len(random_list)
print(mean)

import numpy as np
random_list = np.array(random_list)
mean = random_list.mean()
std = random_list.std()
print(f'random_list.mean is {mean}')
print(f'random_list.std is {std}')

# create basic scatterplot
x = range(N)
y = random_list
plt.plot(x, y, 'o')

# obtain m (slope) and b(intercept) of linear regression line
m, b = np.polyfit(x, y, 1)

# add linear regression line to scatterplot
plt.plot(x, m * x + b)
plt.show()