import pandas as pd

ventes = pd.read_csv("data/ventes.csv")

print(ventes.head())

print(ventes.shape)

ventes.isna().sum()