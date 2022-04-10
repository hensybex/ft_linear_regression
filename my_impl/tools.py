def linear_equasion(theta0, theta1, mileage):
	return (theta0 + (theta1 * mileage))

def gradientDiff(theta0, theta1, km, price, m, learningRate):
	sumDiff = 0.0
	i = 0
	while i < m:
		sumDiff += linear_equasion(theta0, theta1, km[i]) - price[i]
		i += 1
	return (learningRate * sumDiff / float(m))

def meanSquaredError(theta0, theta1, km, price, m):
	error = 0.0
	i = 0
	while i < m:
		error += (linear_equasion(theta0, theta1, km[i]) - price[i]) ** 2
		i += 1
	return (error / (m - 1))

def meanAbsoluteError(theta0, theta1, km, price, m):
	error = 0.0
	i = 0
	while i < m:
		error += abs(linear_equasion(theta0, theta1, km[i]) - price[i])
		i += 1
	return (error / (m - 1))

def gradientDirection(theta0, theta1, km, price, m, learningRate):
	sum = 0.0
	i = 0
	while i < m:
		sum += (linear_equasion(theta0, theta1, km[i]) - price[i]) * km[i]
		i += 1
	return (learningRate * sum / float(m))