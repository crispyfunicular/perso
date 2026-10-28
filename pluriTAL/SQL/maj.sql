-- L'employé Dupont aura son salaire fixé à 2300 euros
UPDATE Employes
SET salaire = 2300
WHERE nom = 'Dupont'
;

-- Tous les salaires sont augmentés de 5 %
UPDATE Employes
SET salaire = salaire * 1,05
;

-- Seuls les cadres sont augmentés de 5 %
UPDATE Employes
SET salaire = salaire * 1,05
WHERE fonction = 'cadre'
;
