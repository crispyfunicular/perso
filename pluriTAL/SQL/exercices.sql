SELECT numero_compte
FROM Comptes
WHERE solde > 0;

SELECT numero_compte, nom_agence
FROM Comptes
WHERE nom_agence='Jussieu';

SELECT adresse_client
FROM Clients
WHERE adresse_clients IS NOT NULL AND nom_client LIKE 'Simon';

SELECT solde, nom_agence
FROM Comptes
WHERE nom_agence="Jussieu"
AND solde > 0;

SELECT nom, salaire
FROM employes
WHERE salaire >
    ALL (SELECT salaire
    FROM employes
    WHERE n_dept=30);

SELECT nom, fonction
FROM employes
WHERE n_dept=20 AND fonction IN
    (SELECT fonction
    FROM employes
    WHERE n_dept=(
        SELECT n_dept
        FROM employesWHERE nom='dupont')
    );



CREATE TABLE IF NOT EXISTS mutations (
    lettre_initiale TEXT PRIMARY KEY,
    durcissante TEXT,
    adoucissante TEXT,
    spirante TEXT
);


-- articles (NOART, LIBELLE, STOCK, PRIXINVENT)
-- fournisseurs (NOFOUR, NOMFOUR, ADRFOUR, VILLEFOUR)
-- acheter (NOFOUR#, NOART#, PRIXACHAT, DELAI)

-- Question 1 : numéros et libellés des articles dont le stock est inférieur à 10 ?
SELECT noart, libelle
FROM articles
WHERE stock < 10;

-- Question 2 : Liste des articles dont le prix d'inventaire est compris entre 100 et 300 ?
SELECT noart, prixinvent
FROM articles
WHERE prixinvent BETWEEN 100 AND 300;

-- Question 3 : Liste des fournisseurs dont on ne connaît pas l'adresse ?
SELECT nofour, nomfour
FROM fournisseurs
WHERE adrfour IS NULL;

-- Question 4 : Liste des fournisseurs dont le nom commence par "STE" ?
SELECT nofour, nomfour
FROM fournisseurs
WHERE nomfour LIKE 'STE%';

-- Question 5 : Nombre d'articles référencés ?
SELECT count(*)
FROM articles;

-- Question 6 : La moyenne des prix d’achat ?
SELECT avg(prixachat)
FROM acheter;

-- Question 7 : numéros et libellés des articles triés dans l'ordre décroissant des stocks ?
SELECT noart, libelle
FROM articles
ORDER BY stock DESC;

-- Question 8 : afficher les fournisseurs se situant à Paris par leur nom.
-- Attention à GROUP BY
SELECT nomfour
FROM fournisseurs
WHERE villefour = 'Paris'
GROUP BY nomfour;


-- Liste des noms de clients avec leur adresse et leur numéro de compte
SELECT nom_client, numero_compte, adresse_client
FROM Titulaires INNER JOIN Clients ON
Titulaires.nom_client = Clients.nom_client;

-- Syntaxe 2
SELECT ...
FROM Clients, Titulaires
WHERE Clients.nom = Titulaires.nom ;

-- Liste des noms de gestionnaires avec le nom de leur agence et l'adresse de l'agence
SELECT nom_gestionnaire
FROM Gestionnaires INNER JOIN Comptes ON
nom_agence = Clients.nom_client;

-- Liste des noms de clients qui ont un solde négatif
SELECT nom_client
FROM Titulaires INNER JOIN Comptes ON
Titulaires.numero_compte = Comptes.numero_compte
WHERE Comptes.solde < 0;

-- Liste des noms de clients avec leur numéro de compte et leur solde qui possèdent un compte à l'agence « Tolbiac »
SELECT nom_client, solde
FROM Titulaires INNER JOIN Comptes ON
Titulaires.numero_compte = Comptes.numero_compte
WHERE nom_agence = 'Tolbiac';

-- Liste des noms de clients avec leur numéro de compte, leur solde, leur nom de gestionnaire et leur nom d'agence
SELECT nom_client, numero_compte, solde, nom_gestionnaire, nom_agence
FROM Titulaires INNER JOIN Comptes ON
Titulaires.numero_compte = Comptes.numero_compte;

-- Liste des noms de clients avec leur numéro de compte, leur solde, leur nom de gestionnaire, leur nom d'agence et leur adresse
SELECT Titulaires.nom_client, Titulaires.numero_compte, solde, nom_gestionnaire, nom_agence, Clients.adresse_client
FROM Titulaires INNER JOIN Comptes ON
Titulaires.numero_compte = Comptes.numero_compte
INNER JOIN Clients ON
Titulaires.nom_client = Clients.nom_client;

