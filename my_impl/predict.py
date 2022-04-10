from tools import linear_equasion
from pandas_tools import read_csv, read_thetas
import sys

dData = '-data' in sys.argv
dResult = '-result' in sys.argv

mileage = input("Enter mileage: ")
try:
	mileage = float(mileage)
except ValueError as e:
	print(e, "\nA number is needed!")
	sys.exit(0)

try:
	theta0, theta1 = read_thetas('./theta_values.csv')
except:
	theta0 = 0
	theta1 = 0
print("Predicted price:", linear_equasion(float(theta0), float(theta1), mileage), "dollarov se she a")

if dData == 1:
	km, price, m = read_csv('./data.csv')
	from graph_tools import displayData
	displayData(km, price)

if dResult == 1:
	km, price, m = read_csv('./data.csv')
	from graph_tools import displayResult
	displayResult(theta0, theta1, km, price)