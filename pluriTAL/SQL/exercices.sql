CREATE TABLE IF NOT EXISTS emp (
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


SELECT SUM(salaire), n_dept
FROM emp
GROUP BY n_dept
;


SELECT nom_gestionnaire, AVG(solde) AS solde_moyen
FROM comptes
-- WHERE solde IS NOT NULL
GROUP BY nom_gestionnaire
HAVING AVG(solde) > 300
;



-- Exercice 1
SELECT nom, salaire, commission
FROM employes
WHERE comm < salaire
WHERE salaire BETWEEN 9000 AND 15000

WHERE function LIKE '%commercial%' OR function LIKE '%directeur%'
WHERE function IN ('commercial', 'directeur')

WHERE n_dept = 30 AND salaire > 25000
WHERE commission IS NULL
;


SELECT sum(salaire)
FROM employes
WHERE n_dept = 30
;

SELECT count(nom_client)
FROM client
;

SELECT sum(salaire), n_dept
FROM elployes
GROUP BY n_dept
