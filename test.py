import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import pylab as pl
import random

# графики отобразим в Jupyter
#%matplotlib inline

# укажем размер графиков
from pylab import rcParams
rcParams['figure.figsize'] = 12, 6

# отключим предупреждения Anaconda
import warnings
warnings.simplefilter('ignore')

# загрузим значения
#table_zero = pd.read_csv('test_data.csv', header=0, sep=',')
table_zero = pd.read_csv('data.csv', header=0, sep=',')

# посмотрим информацию о таблице и на саму таблицу
#print(table_zero.info())
#print('********************************************')
#print(table_zero)
#print('********************************************')

# подготовим данные без использования NumPy

month = []
#[month.append(float(i)) for i in table_zero['month']]
[month.append(float(i)) for i in table_zero['km']]

#print(month)
#print(type(month))
#print('********************************************')

revenue = []
#[revenue.append(float(i)) for i in table_zero['revenue']]
[revenue.append(float(i)) for i in table_zero['price']]

#print(revenue)
#print(type(revenue))
#print('********************************************')

# подготовим данные с использованием NumPy

""" x_np = table_zero[['x']].values
print(x_np)
print(type(x_np))
print(x_np.shape)
print('********************************************')

y_np = table_zero[['y']].values
print(y_np)
print(type(y_np))
print(y_np.shape)
print('********************************************') """




def test_kramer(x, y):
    #Сумма x
    sumX = sum(x)
    #Сумма y
    sumY = sum(y)

    #Сумма x*y
    sumXY = 0
    for i in range(len(x)):
        sumXY += x[i] * y[i]

    #Сумма x^2
    sum_x_sq = 0
    for i in range(len(x)):
        sum_x_sq += x[i] * x[i]

    #Количество значений
    n = len(x)

    det = n * sum_x_sq - sumX * sumX

    detA = n * sumXY - sumY * sumX

    detB = sumY * sum_x_sq - sumXY * sumX

    a = detA / det
    b = detB / det
    return a, b

print(test_kramer(month, revenue), "ERROR")

a = test_kramer(month, revenue)[0]
b = test_kramer(month, revenue)[1]

print("\n\n")

#for i in range(len(month)):
#    print(a * month[i] + b)

print("\n\n")

monthSol = []
for i in range(len(month)):
    monthSol.append(month[i])

revenueSol = []

for i in range(len(month)):
    revenueSol.append(a * month[i] + b)

plt.plot(month, revenue)

plt.plot(monthSol, revenueSol)

plt.show()

#print(3**2)