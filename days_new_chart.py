import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('worlddata_2015.csv')
country = df["Country"]
code = df["Code"]
time = df["Time"]
gdp = df["GDP"]
tax = df["tax"]
ease = df["ease"]
new = df["new business registered"]

plt.scatter(new, time, color='green', marker='o')
for code, new1, time1 in zip(code, new, time):
	plt.annotate(code, xy=(new1,time1), xytext=(5,-5), textcoords='offset points')
plt.title("Days to Start a Business versus New Business registered per year")
plt.ylabel("Days to Start a Business")
plt.ylim((1,160))
plt.xlabel("New Businesses registered per year")
plt.xlim((1,600000))
plt.show()
plt.close()
