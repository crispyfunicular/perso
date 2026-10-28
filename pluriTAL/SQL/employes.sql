/*
Total des salaires pour chaque département
Quels sont les employés gagnant plus que tous les employés du département 30 ?
Liste des employés du département 20 ayant la même fonction qu'un employé du département de DUPONT.
Donner pour chaque commercial son revenu (salaire+commission)
Donner la liste des empoyés dont la commission est inférieure à 5% du salaire.
Donner la liste des administratifs classée par commission sur salaire (commission/salaire) décroissant

*/

-- Création de la table
CREATE TABLE IF NOT EXISTS Employes (
    nom TEXT,
    num INTEGER PRIMARY KEY,
    fonction TEXT,
    n_sup INTEGER,
    embauche DATE,
    salaire INTEGER,
    comm INTEGER,
    n_dept INTEGER
);

-- Insertion des données
INSERT INTO Employes (nom, num, fonction, n_sup, embauche, salaire, comm, n_dept)
VALUES
    ('martin', 16712, 'directeur', 257187, '1990-05-23', 40000, 4000, 30),
    ('dupont', 17574, 'administratif', 16712, '1995-05-03', 9000, 500, 30),
    ('lambert', 25012, 'administratif', 27047, '1991-04-14', 12000, 150, 20),
    ('dupond', 26691, 'commercial', 27047, '1988-04-04', 25000, 2500, 20);