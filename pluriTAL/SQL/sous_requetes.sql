/*
• Q1 : Quels sont les numéros de compte dont le solde est plus grand que la moyenne des soldes ?
• Q2 : Quels sont les numéros de compte qui ont un solde inférieur à au moins un des soldes des comptes dont le gestionnaire est « Caron » ?
• Q3 : Quels sont les numéros de compte qui ont un solde inférieur à tous les soldes des comptes dont le gestionnaire est « Caron » ?
• Q4 : Quels sont les clients qui n'ont pas de compte ? (les clients dans la table « clients » peuvent ne pas figurer dans la table « titulaires »)
*/

DROP TABLE IF EXISTS Titulaires;
DROP TABLE IF EXISTS Comptes;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Gestionnaires;
DROP TABLE IF EXISTS Agences;

CREATE TABLE Agences (
    nom_agence TEXT PRIMARY KEY,
    adresse_agence TEXT
);

INSERT INTO Agences (nom_agence, adresse_agence) VALUES
('Jussieu', '7 place Jussieu 75005 Paris'),
('Sèvres', '70 rue de Sèvres 75007 Paris'),
('Tolbiac', '150 rue Tolbiac 75013 Paris'),
('Voltaire', '205 bd Voltaire 75011 Paris'),
('Jasmin', '16 rue La Fontaine 75016 Paris');

CREATE TABLE Gestionnaires (
    nom_gestionnaire TEXT PRIMARY KEY,
    adresse_gestionnaire TEXT
);

INSERT INTO Gestionnaires (nom_gestionnaire, adresse_gestionnaire) VALUES
('Caron', '12 bd Blanqui 75013 Paris'),
('Dubois', '121 rue de Vaugirard 75005 Paris'),
('Rocher', '45 rue Buzenval 75020 Paris'),
('Sernin', '8 allée des haies 92000 La forêt');

CREATE TABLE Clients (
    nom_client TEXT PRIMARY KEY,
    adresse_client TEXT
);

INSERT INTO Clients (nom_client, adresse_client) VALUES
('Adam', NULL),
('Curry', '10 rue des matins Bondy'),
('Martin', '24 rue Linné 75005 Paris'),
('Mathias', NULL),
('Simon', '26 bd Raspail 75006 Paris'),
('Valentin', '80 rue Dunois 75013 Paris');

CREATE TABLE Comptes (
    numero_compte TEXT PRIMARY KEY,
    solde REAL,
    nom_gestionnaire TEXT,
    nom_agence TEXT
);

INSERT INTO Comptes (numero_compte, solde, nom_gestionnaire, nom_agence) VALUES
('12730X', -45, 'Rocher', 'Tolbiac'),
('2186G', -200, 'Rocher', 'Sèvres'),
('49772E', 1500, 'Caron', 'Tolbiac'),
('5689A', 300, 'Dubois', 'Jussieu');

CREATE TABLE Titulaires (
    nom_client TEXT,
    numero_compte TEXT,
    PRIMARY KEY (nom_client, numero_compte)
);

INSERT INTO Titulaires (nom_client, numero_compte) VALUES
('Adam', '5689A'),
('Martin', '49772E'),
('Simon', '2186G'),
('Simon', '5689A'),
('Valentin', '49772E');

--  Q1 : Quels sont les numéros de compte dont le solde est plus grand que la moyenne des soldes ?
SELECT Comptes.numero_compte
FROM Comptes
WHERE Comptes.solde > (SELECT AVG(solde) FROM Comptes)
;

-- Q2 : Quels sont les numéros de compte qui ont un solde inférieur à au moins un des soldes des comptes dont le gestionnaire est « Caron » ?
SELECT Comptes.numero_compte
FROM Comptes
WHERE Comptes.solde < (SELECT MAX(solde) FROM Comptes WHERE Comptes.nom_gestionnaire = 'Caron')
;

-- Q3 : Quels sont les numéros de compte qui ont un solde inférieur à tous les soldes des comptes dont le gestionnaire est « Caron » ?
SELECT Comptes.numero_compte
FROM Comptes
WHERE Comptes.solde < (SELECT MIN(solde) FROM Comptes WHERE Comptes.nom_gestionnaire = 'Caron')
;


-- Q4 : Quels sont les clients qui n'ont pas de compte ? (les clients dans la table « clients » peuvent ne pas figurer dans la table « titulaires »)
SELECT Clients.nom_client
FROM Clients
WHERE nom_client NOT IN (SELECT nom_client FROM Titulaires)
;
