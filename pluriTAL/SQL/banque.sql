/*Q1: Liste des clients ?
Q2: Liste des clients qui ont un compte
Q3: Liste des clients avec leur adresse
Q4: Quelle est l'adresse du client de nom 'Simon '
Q5: Liste des comptes créditeurs (solde positif)
Q6: Quels sont les numéros de compte de l’agence « Jussieu »
Q7: Sélectionner dans la table Comptes les tuples dont le  solde est créditeur (>0) et dont le nom d’agence est «Jussieu »

Fonctions d'agrégation :
Quel est le nombre de clients ?
Quel est le solde moyen de tous les comptes ?

Regroupement :
Quel est le solde moyen de tous les comptes de toutes les agences regrou^pées par gestionnaire ?
Quels sont les soldes moyens supérieurs à 300, regroupés par gestionnaire ?
*/

-- Tables
CREATE TABLE Agences (
    nom_agence TEXT PRIMARY KEY,
    adresse_agence TEXT
);

CREATE TABLE Clients (
    nom_client TEXT PRIMARY KEY,
    adresse_client TEXT
);

CREATE TABLE Gestionnaires (
    nom_gestionnaire TEXT PRIMARY KEY,
    adresse_gestionnaire TEXT
);

-- Table Comptes (dépend de Gestionnaires et Agences)
CREATE TABLE Comptes (
    numero_compte TEXT PRIMARY KEY,
    solde INTEGER,
    nom_gestionnaire TEXT,
    nom_agence TEXT,
    FOREIGN KEY (nom_gestionnaire) REFERENCES Gestionnaires(nom_gestionnaire),
    FOREIGN KEY (nom_agence) REFERENCES Agences(nom_agence)
);

-- Table Titulaires (Table de liaison entre Clients et Comptes)
-- Sa clé primaire est composée des deux colonnes car un client peut avoir plusieurs comptes et inversement.
CREATE TABLE Titulaires (
    nom_client TEXT,
    numero_compte TEXT,
    PRIMARY KEY (nom_client, numero_compte),
    FOREIGN KEY (nom_client) REFERENCES Clients(nom_client),
    FOREIGN KEY (numero_compte) REFERENCES Comptes(numero_compte)
);

-- Remplissage de la table Agences
INSERT INTO Agences (nom_agence, adresse_agence) VALUES
    ('Jussieu', '7 place Jussieu 75005 Paris'),
    ('Sèvres', '70 rue de Sèvres 75007 Paris'),
    ('Tolbiac', '150 rue Tolbiac 75013 Paris'),
    ('Voltaire', '205 bd Voltaire 75011 Paris'),
    ('Jasmin', '16 rue La Fontaine 75016 Paris');

-- Remplissage de la table Clients (NULL est utilisé pour les adresses vides)
INSERT INTO Clients (nom_client, adresse_client) VALUES
    ('Adam', NULL),
    ('Curry', '10 rue des matins Bondy'),
    ('Martin', '24 rue Linné 75005 Paris'),
    ('Mathias', NULL),
    ('Simon', '26 bd Raspail 75006 Paris'),
    ('Valentin', '80 rue Dunois 75013 Paris');

-- Remplissage de la table Gestionnaires
INSERT INTO Gestionnaires (nom_gestionnaire, adresse_gestionnaire) VALUES
    ('Caron', '12 bd Blanqui 75013 Paris'),
    ('Dubois', '121 rue de Vaugirard 75005 Paris'),
    ('Rocher', '45 rue Buzenval 75020 Paris'),
    ('Sernin', '8 allée des haies 92000 La forêt');

-- Remplissage de la table Comptes
INSERT INTO Comptes (numero_compte, solde, nom_gestionnaire, nom_agence) VALUES
    ('12730X', -45, 'Rocher', 'Tolbiac'),
    ('2186G', -200, 'Rocher', 'Sèvres'),
    ('49772E', 1500, 'Caron', 'Tolbiac'),
    ('5689A', 300, 'Dubois', 'Jussieu');

-- Remplissage de la table Titulaires
INSERT INTO Titulaires (nom_client, numero_compte) VALUES
    ('Adam', '5689A'),
    ('Martin', '49772E'),
    ('Simon', '2186G'),
    ('Simon', '5689A'),
    ('Valentin', '49772E');

