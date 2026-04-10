# Révisions commandes SQL

Ce document synthétise les commandes et concepts SQL abordés dans le cours.

## Création de tables (DDL)

* `CREATE TABLE` : Permet de créer la structure d'une table.
* **Types de données** : `INT` pour les entiers, `VARCHAR()` pour les chaînes de caractères variables, `CHAR()`.
* **Contraintes** : `PRIMARY KEY` pour la clé primaire, `AUTO INCREMENT` pour l'incrémentation automatique.

```sql
CREATE TABLE IF NOT EXISTS employes (
    mut_nom TEXT PRIMARY KEY,
    num INTEGER,
    fonction TEXT,
    n_sup INTEGER,
    embauche DATE,
    salaire INTEGER,
    comm INTEGER,
    n_dept INTEGER
);

INSERT INTO emp (mut_nom, num, fonction, n_sup, embauche, salaire, comm, n_dept)
VALUES
    ('martin', 16712, 'directeur', 257187, '23/05/1990', 40000, 4000, 30),
    ('dupont', 17574, 'administratif', 16712, '03/05/1995', 9000, 500, 30),
    ('lambert', 25012, 'administratif', 27047, '14/04/1991', 12000, 150, 20),
    ('dupond', 26691, 'commercial', 27047, '04/04/1990', 25000, 2500, 20)
    ;
```


## Requête `SELECT`
L'ordre SQL `SELECT` est composé de 6 clauses, dont 4 sont optionnelles. 

| Clause | Rôle et description |
| :--- | :--- |
| **SELECT** | Spécification des colonnes du résultat. Le mot clé **AS** offre la possibilité de nommer le résultat. |
| **FROM** | Spécification des tables sur lesquelles porte l'ordre. |
| **WHERE** | Filtre portant sur les données (conditions à remplir pour que les lignes soient présentes dans le résultat). |
| **GROUP BY** | Définition d'un groupe (sous-ensemble). |
| **HAVING** | Filtre portant sur les résultats (conditions de regroupement des lignes). |
| **ORDER BY** | Tri des données du résultat. |


```sql
SELECT nom, salaire, commission
FROM employes
WHERE comm < salaire

WHERE salaire BETWEEN 9000 AND 15000

WHERE n_dept = 30 AND salaire > 25000

WHERE commission IS NULL
;
```

## Fonctions d'agrégation
Ces fonctions s'utilisent pour effectuer des calculs sur un ensemble de données regroupées :

* **`SUM(nom_attribut)`** : calcule la **somme** des valeurs des attributs.
* **`MIN(nom_attribut)`** : recherche **la plus petite valeur** de l'attribut.
* **`MAX(nom_attribut)`** : recherche **la plus grande valeur** de l'attribut.
* **`COUNT(nom_attribut)`** : compte le **nombre d'occurrences** de l'attribut.
* **`AVG(nom_attribut)`** : calcule la **moyenne** des valeurs des attributs.

```sql
SELECT nom_gestionnaire, AVG(solde) AS solde_moyen
FROM comptes
GROUP BY nom_gestionnaire
HAVING AVG(solde) > 300
;
```

## Opérateurs
Les opérateurs permettent de comparer une valeur à un ensemble de valeurs ou d'effectuer des calculs :

* **`IN`** : Compare à une liste de valeurs.
* **`ANY`** : la comparaison est vraie si elle est vraie pour au moins un des éléments de l'ensemble.
* **`ALL`** : la comparaison est vraie si elle est vraie pour tous les éléments de l'ensemble.
* **Opérateurs arithmétiques** : `+`, `-`, `*`, `/`.

```sql
SELECT nom, salaire, commission
FROM employes
WHERE function IN ('commercial', 'directeur')
;
```

## Jointures

Les jointures permettent d'interroger simultanément plusieurs tables liées entre elles par des attributs communs (généralement une clé primaire et une clé étrangère).

### Syntaxe explicite (`INNER JOIN`)
- `INNER JOIN` : assembler deux tables
- `ON` : spécifier la condition de jointure (l'égalité entre les champs correspondants).

```sql
-- Exemple : Liste des noms de clients avec leur adresse et leur numéro de compte
SELECT Titulaires.nom_client, Titulaires.numero_compte, Clients.adresse_client
FROM Titulaires 
INNER JOIN Clients ON Titulaires.nom_client = Clients.nom_client;
```

### Syntaxe implicite (`WHERE`)
- `FROM` : indiquer toutes les tables séparées par des virgules
- `WHERE` : définir la condition d'égalité

```sql
SELECT nom, adresse_client
FROM Clients, Titulaires
WHERE Clients.nom = Titulaires.nom;
```

### Jointures multiples
Il est possible de croiser les données de plus de deux tables en enchaînant simplement les `INNER JOIN`.

```sql
-- Exemple entre 3 tables : Titulaires, Comptes et Clients
SELECT Titulaires.nom_client, Titulaires.numero_compte, Comptes.solde, Comptes.nom_gestionnaire, Comptes.nom_agence, Clients.adresse_client
FROM Titulaires 
INNER JOIN Comptes ON Titulaires.numero_compte = Comptes.numero_compte
INNER JOIN Clients ON Titulaires.nom_client = Clients.nom_client;
```

**Note :** Si un attribut porte le même nom dans plusieurs des tables interrogées (comme `nom_client` ou `numero_compte`), il faut obligatoirement préciser de quelle table il provient en le préfixant (`Table.attribut`, par exemple `Titulaires.nom_client`), tant dans le `SELECT` que dans le `ON` ou `WHERE`, afin d'éviter toute ambiguïté.
