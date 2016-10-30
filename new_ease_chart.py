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

plt.scatter(new, ease, color='red', marker='o')
for code, new1, ease1 in zip(code, new, ease):
	plt.annotate(code, xy=(new1,ease1), xytext=(5,-5), textcoords='offset points')
plt.title("Ease of Doing Business versus New Business registered per year")
plt.ylabel("Ease of Doing Business")
plt.ylim((1,200))
plt.xlabel("New Businesses registered per year")
plt.xlim((1,600000))
plt.show()
plt.close()
