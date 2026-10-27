# Annexe TP1 - Relevé et décompte des erreurs de traduction

Cette annexe détaille le relevé des erreurs résumé dans la partie B du TP1. Les erreurs sont classées selon la typologie présentée en B.1 (Delisle et MQM), avec trois niveaux de gravité (critique, majeure, mineure). Chaque ligne décrit une erreur, indique le numéro de l’exemple du TP1 et les systèmes de traduction automatique concernés. Les trois pertes communes à tous les systèmes (*Will*, *GOAT*, *taste / waste*), mentionnées au point B.2. du TP1, ne sont pas comptées ici, afin de ne pas fausser la comparaison entre les modèles.

Le décompte (section 4) compte une erreur par système et par exemple. Il est brut, sans pondération, et la liste n’est pas exhaustive.

## 1. Fautes de traduction (rapport au texte source)

**Contresens** (MQM : *Accuracy › Mistranslation*)

| Gravité | Ex. | Description | Systèmes |
|---|---|---|---|
| Critique | 4.1 | *Lessee* et *Lessor* confondus : le même acteur s’indemnise lui-même (« Le Locateur indemnisera le Locateur », « le preneur… le preneur », « le locataire indemnisera… le locataire ») | MarianMT, mBART-50, NLLB-200 |

**Faux sens** (MQM : *Accuracy › Mistranslation*)

| Gravité | Ex. | Description | Systèmes |
|---|---|---|---|
| Critique | 5.1 | *Tighten* devient « Tisser » | mBART-50 |
| Majeure | 5.1 | « Resserrer » (= serrer de nouveau) au lieu de « serrer » | NLLB-200 |
| Majeure | 5.1 | « Vis serrée A à 5 Nm » : la consigne devient un groupe nominal | MarianMT |
| Majeure | 5.3 | *Press* devient « Cliquez » (vocabulaire d’interface logicielle) | mBART-50 |
| Majeure | 5.3 | *turn on* devient « appuyer sur le dispositif » | T5-small |
| Majeure | 1.3 | *done* lu comme *faire* (« C’est ce que j’ai fait », « J’ai bien fait », « j’ai donc fait ») | MarianMT, mBART-50, NLLB-200, Reverso |
| Majeure | 3.1 | *belied* devient « a lu », « a trahi », « a crié », « a menti » | T5-small, MarianMT, mBART-50, NLLB-200 |
| Majeure | 3.3 | *boughs* devient « bougies » ou « bourgeons » | T5-small, mBART-50 |
| Majeure | 3.3 | *shake* devient « s’écoulent » | mBART-50 |
| Majeure | 3.3 | *or none, or few* devient « ou les unes, ou les autres » | NLLB-200 |
| Majeure | 4.1 | *hold harmless* devient « garder inoffensif » | mBART-50 |
| Majeure | 6.3 | *Finger Lickin’ good* devient « C’est bon, le doigt » | MarianMT |
| Mineure | 3.3 | « qui secouent contre le froid » (verbe transitif employé sans objet) | MarianMT |
| Mineure | 1.1 | *meeting* devient « rencontre » | mBART-50 |
| Mineure | 1.1 | 🙄 remplacé par 😉 (le ton change) | mBART-50 |
| Mineure | 2.3 | *walk* devient « se promène » | T5-small |
| Mineure | 2.3 | *Yea, though* remplacé par « Quand » : la concession disparaît (mais le texte est celui de Segond) | Google Translate |

**Non-sens** (MQM : *Linguistic conventions › Unintelligible*)

| Gravité | Ex. | Description | Systèmes |
|---|---|---|---|
| Critique | 5.1 | boucle « 2.2.1.2.1.2… » à la place de la phrase | T5-small |
| Critique | 6.3 | « l’aise, il y a eu un accroissement de la pression et de la pression » | T5-small |
| Majeure | 6.3 | « Le "Démarrer les doigts" va bien » | NLLB-200 |
| Majeure | 3.3 | « tu peux en moi voici », « tu s’appât » | T5-small |
| Majeure | 3.2 | « tu ai tu sa volonté » | T5-small |

**Omission** (MQM : *Accuracy › Omission*)

| Gravité | Ex. | Description | Systèmes |
|---|---|---|---|
| Critique | 1.2 | sortie vide | T5-small |
| Critique | 1.3 | tout le texte omis, seul le hashtag reste | T5-small |
| Critique | 4.1 | le bailleur (*Lessor*) disparaît | T5-small |
| Majeure | 1.2 | « Living the dream! » omis | mBART-50, NLLB-200 |
| Majeure | 2.2 | la première proposition (« In the beginning was the Word ») est omise | T5-small |
| Majeure | 3.3 | *thou mayst in me behold* omis : la phrase devient « c’est un moment de l’année » | mBART-50 |
| Majeure | 6.2 | « Taste » omis, il ne reste que « Pas la taille. » | MarianMT |
| Mineure | 1.3 | hashtag omis | NLLB-200 |
| Mineure | 1.1 | émoji 🙄 omis | T5-small, MarianMT |
| Mineure | 1.2 | émoji 😅 omis | MarianMT, mBART-50, NLLB-200 |
| Mineure | 1.3 | émoji 😩 omis | MarianMT, mBART-50, NLLB-200 |
| Mineure | 6.1 | marque entre parenthèses omise | NLLB-200, DeepL |
| Mineure | 6.2 | marque entre parenthèses omise | MarianMT, NLLB-200, DeepL |
| Mineure | 6.3 | marque entre parenthèses omise | MarianMT, NLLB-200, DeepL |

**Ajout et surtraduction** (MQM : *Accuracy › Addition / Overtranslation*)

| Gravité | Ex. | Description | Systèmes |
|---|---|---|---|
| Mineure | 1.2 | « qui aurait dû prendre 5 minutes » : explicitation de l’implicite | DeepL |
| Mineure | 3.2 | *wish* devient « exprime un vœu » : interprétation absente de la source | DeepL |
| Mineure | 3.1 | *by heaven* devient « par Dieu » : plus explicite que « par le ciel » | mBART-50 |

**Non-traduction et traduction à tort** (MQM : *Accuracy › Untranslated / Do not translate*)

| Gravité | Ex. | Description | Systèmes |
|---|---|---|---|
| Majeure | 6.2 | « Taste, pas waist » ; « Taste. Non Taille. » : mots anglais laissés | T5-small, mBART-50 |
| Majeure | 6.3 | « Finger Lickin’ » non traduit | mBART-50, Reverso |
| Majeure | 6.2 | *Weight Watchers* traduit (« Veilleurs de poids », « Vérificateurs de la taille ») | T5-small, mBART-50 |
| Mineure | 1.3 | *rn* laissé tel quel (« ce rn ») | Reverso |
| Mineure | 1.1 | hashtag traduit (`#VieEnEntreprise`) | Google Translate |
| Mineure | 1.3 | hashtag traduit (`#HumeurDuLundi`) | Google Translate |

## 2. Fautes de langue et de style (rédaction en français)

**Mal-dit** (MQM : *Style › Awkward / Unidiomatic*)

| Gravité | Ex. | Description | Systèmes |
|---|---|---|---|
| Majeure | 4.1 | doublet *from and against* traduit mot à mot et répété (« indemnisera et indemnisera… et contre toute réclamation ») | NLLB-200, mBART-50 |
| Mineure | 1.2 | « Vivre le rêve ! » littéral : l’ironie se perd | MarianMT, Reverso |
| Mineure | 4.1 | « de toute réclamation et contre celle-ci » : doublet mot à mot | T5-small |
| Mineure | 3.3 | versification perdue : le poème devient une phrase en prose | mBART-50, NLLB-200, Google Translate |

**Grammaire et orthographe** (MQM : *Linguistic conventions › Grammar / Spelling*)

| Gravité | Ex. | Description | Systèmes |
|---|---|---|---|
| Mineure | 3.1 | « de faux comparaison » (accord) | T5-small |
| Mineure | 3.2 | « tu a tes volontés » (accord sujet-verbe) | mBART-50 |
| Mineure | 5.1 | « le vis » (genre) | mBART-50 |
| Mineure | 6.1 | « tre une chèvre » : initiale perdue | T5-small |

**Ponctuation et typographie** (MQM : *Linguistic conventions › Punctuation*)

| Gravité | Ex. | Description | Systèmes |
|---|---|---|---|
| Mineure | 1.1 | espaces doubles | T5-small, mBART-50 |
| Mineure | 1.2 | « rêve! » sans espace avant le point d’exclamation | MarianMT |
| Mineure | 1.3 | ponctuation inhabituelle « . . . » | mBART-50 |

**Registre** (MQM : *Style › Language register*)

| Gravité | Ex. | Description | Systèmes |
|---|---|---|---|
| Mineure | 2.3 | *Yea* rendu par un « Oui » moderne | T5-small, MarianMT, mBART-50, Reverso |

## 3. Terminologie

**Terminologie** (MQM : *Terminology › Wrong term*)

| Gravité | Ex. | Description | Systèmes |
|---|---|---|---|
| Majeure | 5.3 | « bouton de puissance » pour *power button* (on attend « d’alimentation ») | T5-small |
| Mineure | 4.3 | « arbitrage contraignant » (calque de *binding*) plutôt qu’« exécutoire » | T5-small, MarianMT, mBART-50, NLLB-200 |
| Mineure | 4.2 | « accord » plutôt que « contrat » pour *Agreement* | T5-small, MarianMT, mBART-50, NLLB-200, Google Translate |

## 4. Décompte par système

| Système | Critiques | Majeures | Mineures | Total |
|---|---|---|---|---|
| T5-small | 5 | 9 | 9 | 23 |
| MarianMT | 1 | 5 | 11 | 17 |
| mBART-50 | 2 | 12 | 13 | 27 |
| NLLB-200 | 1 | 7 | 9 | 17 |
| DeepL | 0 | 0 | 5 | 5 |
| Reverso | 0 | 2 | 3 | 5 |
| Google Translate | 0 | 0 | 5 | 5 |

| Système | Contresens | Faux sens | Non-sens | Omission | Ajout / surtrad. | Non-trad. | Mal-dit | Gramm. | Ponct. | Registre | Terminologie |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T5-small | 0 | 4 | 4 | 5 | 0 | 2 | 1 | 2 | 1 | 1 | 3 |
| MarianMT | 1 | 5 | 0 | 6 | 0 | 0 | 1 | 0 | 1 | 1 | 2 |
| mBART-50 | 1 | 9 | 0 | 4 | 1 | 3 | 2 | 2 | 2 | 1 | 2 |
| NLLB-200 | 1 | 4 | 1 | 7 | 0 | 0 | 2 | 0 | 0 | 0 | 2 |
| DeepL | 0 | 0 | 0 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| Reverso | 0 | 1 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 1 | 0 |
| Google Translate | 0 | 1 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 1 |
