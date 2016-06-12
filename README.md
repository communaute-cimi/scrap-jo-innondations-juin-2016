# Communes inondées en juin 2016
Constituer un fichier des communes classées en état de catastrophe naturelles (inondations juin 2016)

<img src="/img/communesCat_Nat_dpt_qgis_ortho.jpg" width="800">

## Source 
* [Journal Officiel](https://www.legifrance.gouv.fr/affichTexte.do?cidTexte=JORFTEXT000032669529&dateTexte=&categorieLien=id)

## Scrap des données en python
* Avec BeautifulSoup et un peu de RegExp extraire les communes
* Produit un fichier csv
* Code :  scrapJO.py

## Amélioration manuelle (édition du CSV)
* Ajouter la colonne département

## Récupérer les INSEE par jointure PostgreSQL
* Importer le fichier dans postgreSQL
* Joindre avec un fichier de communes (nom+departement)
* Ajout manuel des insee manquants (accents)
* Export du fichier csv avec codes insee

## Ouverture et jointure insee dans QGIS

Résultat en ouvrant le projet QGIS : 

<img src="/img/communesCat_Nat_dpt_qgis.jpg" width="800">

Données : 
* Fichier département OSM 
* Fichier communes OSM
* Fichier communes en état de catastrophe naturelle

La jointure se fait en ouvrant le fichier de communes > jointure > joindre sur insee.




