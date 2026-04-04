"""
Une maîtresse de maison veut construire une base de données sur les personnes
qu’elle invite et les plats qu’elle leur sert. Elle identifie pour cela les trois relations
suivantes :
· REPAS, dont le schéma est REPAS(INVITÉ , DATE) et qui contient la liste des
invités reçus et à quelle date.
· MENU, dont le schéma est MENU (PLAT, DATE) et qui contient le menu servi à
chaque date.
· PRÉFÉRENCE, dont le schéma est PRÉFÉRENCE (PERSONNE, PLAT) donne
et qui contient, pour chaque personne, ses plats préférés. Les attributs
PERSONNE et INVITÉ ont le même domaine de valeurs.
**Trouver des informations suivantes
- en traduisant cette opération par une requête SQL
⇒ les invités du repas du 02/10/2009
⇒ les dates auxquelles un « Boeuf Bourguignon » a été servi.
⇒ Les plats préférés de « Mme Machine ».
⇒ Les plats qui ont été servis à « Mr Machin ».
⇒ Les personnes invitées qui ont été servies par leurs plats préférés.
⇒ Les personnes qui n’ont jamais été invitées.
"""

CREATE TABLE IF NOT EXISTS repas (
    invite TEXT PRIMARY KEY,
    date_repas DATE
);

CREATE TABLE IF NOT EXISTS menu (
    plat TEXT,
    date_menu DATE PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS preference (
    personne TEXT PRIMARY KEY,
    plat TEXT
);


-- les invités du repas du 02/10/2009
SELECT invite
FROM repas
WHERE date_repas = '2009-10-02';

-- les dates auxquelles un « Boeuf Bourguignon » a été servi.
SELECT date_menu
FROM menu
WHERE plat = 'Boeuf Bourguignon';

-- Les plats préférés de « Mme Machine »
SELECT plat
FROM preference
WHERE personne = 'Mme Machine';

-- Les plats qui ont été servis à « Mr Machin »
SELECT menu.plat
FROM menu
INNER JOIN repas ON menu.date = repas.date
WHERE repas.invite = 'Mr Machin';

-- Les personnes invitées qui ont été servies par leurs plats préférés
SELECT repas.invite
FROM repas
INNER JOIN preference ON repas.invite = preference.personne
INNER JOIN menu ON repas.date_repas = menu.date_menu
WHERE menu.plat = preference.plat;