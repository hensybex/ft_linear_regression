import pandas as pd
import matplotlib.pyplot as plt
import random as rand

df = pd.read_csv(r'./data.csv')

""" def train_test_split(data, target):
    
    return train, test

X_train, X_test, y_train, y_test = train_test_split(df['km'], df['price']) """

estimatePrice = 0
tmpTheta0 = 0
tmpTheta1 = 0


for i in df['km']:
    tmpTheta0 = 