import sys
import pandas as pd

def get_km():
	return ((pd.read_csv('data.csv')['km'] / 1000).to_list())

def get_price():
	return ((pd.read_csv('data.csv')['price'] / 1000).to_list())

def hypothesis(theta0, theta1, x):
	return (theta0 + (theta1 * x))

def SumTheta0(theta0, theta1, km, price, m):
	value = 0.
	for i in range(0, m):
		value += hypothesis(theta0, theta1, km[i]) - price[i]
	return (value)

def SumTheta1(theta0, theta1, km, price, m):
	value = 0.
	for i in range(0, m):
		value += (hypothesis(theta0, theta1, km[i]) - price[i]) * km[i]
	return (value)

def GradientDescent(theta0, theta1, LearningRate, LearningRate2, km, price, m, graph):
	theta0 = 0.0
	theta1 = 0.0

	i = 0

	while (True):
		sum0 = SumTheta0(theta0, theta1, km, price, m) / float(m)
		sum1 = SumTheta1(theta0, theta1, km, price, m) / float(m)
		tmp_theta0 = LearningRate * sum0
		tmp_theta1 = LearningRate2 * sum1

		if abs(tmp_theta0) < float(0.0000001) and abs(tmp_theta1) < float(0.0000001):
			return (theta0 * 1000, theta1)

		if graph:
			if i == 2000:
				i = 0
				displayGraph(theta0 * 1000, theta1, km, price, True)
			else:
				i += 1

		theta0 = theta0 - tmp_theta0
		theta1 = theta1 - tmp_theta1