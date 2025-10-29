import pandas as pd
import plotly.express as px

# Charge les données
df = pd.read_csv("ventes.csv")

# Vérifie les 5 premières lignes
print(df.head())

# Graphique a : Ventes par produit 

ventes_par_produit = df.groupby("produit", as_index=False)["qte"].sum()

fig1 = px.bar(
    ventes_par_produit,
    x="produit",
    y="qte",
    title="Ventes par produit (en unités)",
    text="qte"
)
fig1.update_traces(textposition="outside")
fig1.update_layout(xaxis_title="Produit", yaxis_title="Quantité vendue")
fig1.show()

# Graphique b : Chiffre d'affaires par produit 

df["chiffre_affaires"] = df["prix"] * df["qte"]
ca_par_produit = df.groupby("produit", as_index=False)["chiffre_affaires"].sum()

fig2 = px.bar(
    ca_par_produit,
    x="produit",
    y="chiffre_affaires",
    title="Chiffre d'affaires par produit (€)",
    text="chiffre_affaires"
)
fig2.update_traces(texttemplate="%{text:.2f}", textposition="outside")
fig2.update_layout(xaxis_title="Produit", yaxis_title="Chiffre d'affaires (€)")
fig2.show()
