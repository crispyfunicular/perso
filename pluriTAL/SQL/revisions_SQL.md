# Révisions commissionandes SQL

Ce document synthétise les commissionandes et concepts SQL abordés dans le cours.

## Création de tables (DDL)

* `CREATE TABLE` : Permet de créer la structure d'une table.
* **Types de données** : `INT` pour les entiers, `VARCHAR()` pour les chaînes de caractères variables, `CHAR()`.
* **Contraintes** : `PRIMARY KEY` pour la clé primaire, `AUTO INCREMENT` pour l'incrémentation automatique.

```sql
CREATE TABLE IF NOT EXISTS Employes (
    id INTEGER NOT NULL PRIMARY KEY, -- Auto-incrémentation
    nom TEXT,
    num INTEGER,
    fonction TEXT,
    n_sup INTEGER,
    embauche DATE,
    salaire INTEGER,
    commission INTEGER,
    n_dept INTEGER
);

INSERT INTO Employes (nom, num, fonction, n_sup, embauche, salaire, commission, n_dept)
VALUES
    ('martin', 16712, 'directeur', 257187, '1990-05-23', 40000, 4000, 30),
    ('dupont', 17574, 'administratif', 16712, '1995-05-03', 9000, 500, 30),
    ('lambert', 25012, 'administratif', 27047, '1991-04-14', 12000, 150, 20),
    ('dupond', 26691, 'commissionercial', 27047, '1990-04-04', 25000, 2500, 20)
    ;
```

### Clé étrangère
```sql
CREATE TABLE IF NOT EXISTS Adresses (
    adresse_id INTEGER PRIMARY KEY, -- Clé primaire propre à cette table
    employe_id INTEGER, -- 1) On crée d'abord de la colonne
    adresse TEXT,
    code_postal INTEGER,
    ville TEXT,
    FOREIGN KEY (employe_id) REFERENCES Employes(id) -- 2) On indique que la colonne est une clé étrangère
);
```

## Requête `SELECT` 

| Clause | Rôle et description |
| :--- | :--- |
| **SELECT** | Spécification des colonnes du résultat. Le mot clé **AS** offre la possibilité de nommer le résultat. |
| **SELECT \*** | Toutes les colonnes sont sélectionnées. |
| **FROM** | Spécification des tables sur lesquelles porte l'ordre. |
| **ORDER BY** | **ASC** ou **DESC** |
| **WHERE** | Filtre portant sur les données (conditions à remplir pour que les lignes soient présentes dans le résultat). |
| **GROUP BY** | Définition d'un groupe (sous-ensemble). |
| **HAVING** | Filtre portant sur les résultats (conditions de regroupement des lignes). |
| **ORDER BY** | Tri des données du résultat. |
| | |
| **= != < > <= >=** | |
| **BETWEEN** | |
| **AND OR** | `WHERE salaire BETWEEN 9000 AND 15000` |
| **IS (NOT) NULL** | |


```sql
SELECT nom, salaire, commission
FROM Employes
ORDER BY nom_client ASC
WHERE commission < salaire

WHERE salaire BETWEEN 9000 AND 15000

WHERE n_dept = 30 AND salaire > 25000

WHERE commission IS NULL
WhERE adresse IS NOT NULL

WHERE nom LIKE 'M%'
WHERE nom LIKE 'M*' -- Access
WHERE nom LIKE '[A-D]*' -- Access uniquement
;
```

## Fonctions d'agrégation + regroupement
Ces fonctions s'utilisent pour effectuer des calculs sur un ensemble de données regroupées :

* **`SUM(nom_attribut)`** : calcule la **somme** des valeurs des attributs.
* **`MIN(nom_attribut)`** : recherche **la plus petite valeur** de l'attribut.
* **`MAX(nom_attribut)`** : recherche **la plus grande valeur** de l'attribut.
* **`COUNT(nom_attribut)`** : compte le **nombre d'occurrences** de l'attribut.
* **`AVG(nom_attribut)`** : calcule la **moyenne** des valeurs des attributs.

- `GROUP BY` : définition d'un groupe (sous-ensemble)
- `HAVING` : filtre portant sur les résultats (regroupement des lignes)
- `ORDER BY` : tri des données du résultat; ex : `ORDER BY nom`
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
SELECT nom, salaire, commissionission
FROM Employes
WHERE fonction IN ('commissionercial', 'directeur')
WHERE adresse IS NOT NULL
;
```

## Jointures

Les jointures permettent d'interroger simultanément plusieurs tables liées entre elles par des attributs commissionuns (généralement une clé primaire et une clé étrangère).

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

**Note :** Si un attribut porte le même nom dans plusieurs des tables interrogées (commissione `nom_client` ou `numero_compte`), il faut obligatoirement préciser de quelle table il provient en le préfixant (`Table.attribut`, par exemple `Titulaires.nom_client`), tant dans le `SELECT` que dans le `ON` ou `WHERE`, afin d'éviter toute ambiguïté.
