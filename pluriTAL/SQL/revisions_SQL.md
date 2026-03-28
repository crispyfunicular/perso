# Révisions commandes SQL

Ce document synthétise les commandes et concepts SQL abordés dans le cours.

## Structure globale d'une requête
L'ordre SQL `SELECT` est composé de 6 clauses, dont 4 sont optionnelles. 

| Clause | Rôle et description |
| :--- | :--- |
| **SELECT** | Spécification des colonnes du résultat. Le mot clé **AS** offre la possibilité de nommer le résultat. |
| **FROM** | Spécification des tables sur lesquelles porte l'ordre. |
| **WHERE** | Filtre portant sur les données (conditions à remplir pour que les lignes soient présentes dans le résultat). |
| **GROUP BY** | Définition d'un groupe (sous-ensemble). |
| **HAVING** | Filtre portant sur les résultats (conditions de regroupement des lignes). |
| **ORDER BY** | Tri des données du résultat. |


## Fonctions d'agrégation
Ces fonctions s'utilisent pour effectuer des calculs sur un ensemble de données regroupées :

* **`SUM(nom_attribut)`** : calcule la **somme** des valeurs des attributs.
* **`MIN(nom_attribut)`** : recherche **la plus petite valeur** de l'attribut.
* **`MAX(nom_attribut)`** : recherche **la plus grande valeur** de l'attribut.
* **`COUNT(nom_attribut)`** : compte le **nombre d'occurrences** de l'attribut.
* **`AVG(nom_attribut)`** : calcule la **moyenne** des valeurs des attributs.


## Opérateurs
Les opérateurs permettent de comparer une valeur à un ensemble de valeurs ou d'effectuer des calculs :

* **`IN`** : Compare à une liste de valeurs.
* **`ANY`** : la comparaison est vraie si elle est vraie pour au moins un des éléments de l'ensemble.
* **`ALL`** : la comparaison est vraie si elle est vraie pour tous les éléments de l'ensemble.
* **Opérateurs arithmétiques** : `+`, `-`, `*`, `/`.


## Création de tables (DDL)

* **`CREATE TABLE`** : Permet de créer la structure d'une table[184].
* **Types de données** : **`INT`** pour les entiers, **`VARCHAR()`** pour les chaînes de caractères variables [186], **`CHAR()`**.
* **Contraintes** : **`PRIMARY KEY`** pour la clé primaire, **`AUTO INCREMENT`** pour l'incrémentation automatique.