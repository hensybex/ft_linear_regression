import pandas as pd
from tools import gradientDiff, gradientDirection, meanAbsoluteError, meanSquaredError
from pandas_tools import read_csv_normalize, create_csv, read_csv
import sys

def GradientDescent(theta0, theta1, learningRate, epochsNum, km, price, m):
	theta0 = 0.0
	theta1 = 0.0

	currentEpoch = 0
	while (currentEpoch < epochsNum):
		tmp_theta0 = gradientDiff(theta0, theta1, km, price, m, learningRate)
		tmp_theta1 = gradientDirection(theta0, theta1, km, price, m, learningRate)
		theta0 = theta0 - tmp_theta0
		theta1 = theta1 - tmp_theta1
		currentEpoch += 1
	
	return (theta0 * 1000, theta1)


theta0 = 0.0
theta1 = 0.0
epochsNum = 300000
learningRate = 0.0001
km, price, m = read_csv_normalize('./data.csv')
theta0, theta1 = GradientDescent(theta0 = theta0, theta1 = theta1, learningRate = learningRate, epochsNum = epochsNum, km = km, price = price, m = m)

if (theta0 != 0.0) and (theta1 != 0.0):
	d = {'theta0': [theta0], 'theta1': [theta1]}
	create_csv(d, './theta_values.csv')
else:
	print("Thetas remained unchanged. Check epochsNum, learning rate and dataset.")

mse = '-mse' in sys.argv
mae = '-mae' in sys.argv

if mse == 1 or mae == 1:
	km, price, m = read_csv('./data.csv')
	if mse == 1:
		print("Mean squared error:", meanSquaredError(theta0, theta1, km, price, m))
	if mae == 1:
		print("Mean absolute error:", meanAbsoluteError(theta0, theta1, km, price, m))