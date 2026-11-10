import pandas as pd

ventes = pd.read_csv("data/ventes.csv")

chiffre_affaires = ventes['quantite'] * ventes['prix_unitaire']

ca_total = sum(chiffre_affaires)

print(f"Ca total : {ca_total} €")