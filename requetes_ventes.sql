1)Requête chiffre d'affaire total

SELECT SUM(prix_unitaire * quantite) AS chiffre_affaires_total
FROM ventes;

2)Requête vente par produit

SELECT produit, SUM(quantite) AS total_ventes
FROM ventes
GROUP BY produit
ORDER BY total_ventes DESC;

3)Requête vente par région

SELECT region, SUM(quantite) AS ventes_par_region
FROM ventes
GROUP BY region
ORDER BY ventes_par_region DESC;