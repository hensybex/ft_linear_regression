import pandas as pd
import sys

def read_csv_normalize(csv_location):
	df = pd.read_csv(csv_location)
	if df.isnull().values.any() == True:
		print("Some values in dataset are missing.")
		sys.exit(0)
	km = (df['km'] / 1000).to_list()
	price = (df['price'] / 1000).to_list()
	m = df.shape[0]
	return km, price, m

def read_csv(csv_location):
	df = pd.read_csv(csv_location)
	if df.isnull().values.any() == True:
		print("Some values in dataset are missing.")
		sys.exit(0)
	km = (df['km']).to_list()
	price = (df['price']).to_list()
	m = df.shape[0]
	return km, price, m

def read_thetas(csv_location):
	dfThetas = pd.read_csv(csv_location)
	theta0 = dfThetas.loc[0]['theta0']
	theta1 = dfThetas.loc[0]['theta1']
	return theta0, theta1

def create_csv(data, location):
	pd.DataFrame(data=data).to_csv(location)