import matplotlib.pyplot as plt
from tools import linear_equasion

def displayData(km, price):
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.set_title('Data graph')

	ax.plot(km, price, 'o')

	plt.pause(10)

def displayResult(t0, t1, km, price):
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.set_title('Resulting graph')

	ax.plot(km, price, 'o', label = 'data')

	lineX = [0, 300000]
	lineY = [linear_equasion(t0, t1, 0), linear_equasion(t0, t1, 300000)]

	ax.plot(lineX, lineY, linewidth=2, color='red', label = 'result')
	ax.legend()
	plt.pause(10)
