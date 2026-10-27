# TP1 - Traduction automatique
> **Morgane Bona-Pellissier**, Master 2 pluriTAL

Comparaison de quatre modèles Hugging Face (T5-small, MarianMT, mBART-50, NLLB-200-distilled) et de trois systèmes en ligne (DeepL, Reverso, Google Translate) sur 18 phrases réparties en 6 genres.

---

## 1. Tweet

### 1.1 This meeting could’ve been an email 🙄 #CorporateLife

| Système | FR |
|---|---|
| T5-small | Cette réunion aurait pu être un courriel #CorporateLife |
| MarianMT | Cette réunion aurait pu être un e-mail #CorporateLife |
| mBART-50 | Cette rencontre aurait pu être un courriel 😉 #CorporateLife |
| NLLB-200 | Cette réunion aurait pu être un courriel 🙄 #CorporateLife |
| DeepL | Cette réunion aurait pu se faire par e-mail 🙄 #CorporateLife |
| Reverso | Cette réunion aurait pu être un e-mail 🙄 #CorporateLife |
| Google Translate | Cette réunion aurait pu être un simple e-mail 🙄 #VieEnEntreprise |

### 1.2 Just spent 3 hours on a 5-minute task. Living the dream! 😅

| Système | FR |
|---|---|
| T5-small | *(sortie vide)* |
| MarianMT | Je viens de passer 3 heures sur une tâche de 5 minutes. Vivre le rêve! |
| mBART-50 | J’ai tout juste passé 3 heures sur une tâche de 5 minutes. |
| NLLB-200 | J’ai passé 3 heures à une tâche de 5 minutes. |
| DeepL | Je viens de passer 3 heures sur une tâche qui aurait dû prendre 5 minutes. C’est vraiment le rêve ! 😅 |
| Reverso | Je viens de passer 3 heures sur une tâche de 5 minutes. Vivre le rêve ! 😅 |
| Google Translate | Je viens de passer 3 heures sur une tâche de 5 minutes. Le rêve ! 😅 |

### 1.3 im so done w/ this rn 😩 #MondayMood

| Système | FR |
|---|---|
| T5-small | #MondayMood |
| MarianMT | C’est ce que j’ai fait. #MondayMood |
| mBART-50 | J’ai bien fait en ce moment . . . #MondayMood |
| NLLB-200 | Je suis tellement en train de faire ça. |
| DeepL | J’en ai vraiment marre de ça là 😩 #MondayMood |
| Reverso | j’ai donc fait avec ce rn 😩 #MondayMood |
| Google Translate | J’en ai tellement marre de tout ça en ce moment 😩 #HumeurDuLundi |

---

## 2. Bible

### 2.1 The spirit is willing, but the flesh is weak.

| Système | FR |
|---|---|
| T5-small | L’esprit est disposé, mais la chair est faible. |
| MarianMT | L’esprit est disposé, mais la chair est faible. |
| mBART-50 | L’esprit est disposé, mais la chair est faible. |
| NLLB-200 | L’esprit est bien disposé, mais la chair est faible. |
| DeepL | L’esprit est bien disposé, mais la chair est faible. |
| Reverso | L’esprit est disposé, mais la chair est faible. |
| Google Translate | L’esprit est bien disposé, mais la chair est faible. |
| **Bible liturgique officielle (AELF)** | L’esprit est ardent, mais la chair est faible. |
| **Bible protestante (Segond, 1910)** | L’esprit est bien disposé, mais la chair est faible. |

### 2.2 In the beginning was the Word, and the Word was with God, and the Word was God.

| Système | FR |
|---|---|
| T5-small | Au début, la Parole était avec Dieu, et la Parole était Dieu. |
| MarianMT | Au commencement était la Parole, et la Parole était avec Dieu, et la Parole était Dieu. |
| mBART-50 | Au début était la Parole, et la Parole était avec Dieu, et la Parole était Dieu. |
| NLLB-200 | Au commencement était la Parole, et la Parole était avec Dieu, et la Parole était Dieu. |
| DeepL | Au commencement était le Verbe, et le Verbe était avec Dieu, et le Verbe était Dieu. |
| Reverso | Au commencement était la Parole, et la Parole était avec Dieu, et la Parole était Dieu. |
| Google Translate | Au commencement était la Parole, et la Parole était avec Dieu, et la Parole était Dieu. |
| **Bible liturgique officielle (AELF)** | Au commencement était le Verbe, et le Verbe était auprès de Dieu, et le Verbe était Dieu |
| **Bible protestante (Segond, 1910)** | Au commencement était la Parole, et la Parole était avec Dieu, et la Parole était Dieu. |

### 2.3 Yea, though I walk through the valley of the shadow of death, I will fear no evil.

| Système | FR |
|---|---|
| T5-small | Oui, bien que je me promène dans la vallée de l’ombre de la mort, je ne craindrai pas de mal. |
| MarianMT | Oui, bien que je marche dans la vallée de l’ombre de la mort, je ne crains aucun mal. |
| mBART-50 | Oui, même si je marche dans la vallée de l’ombre de la mort, je n’ai pas peur du mal. |
| NLLB-200 | Même si je marche dans la vallée de l’ombre de la mort, je ne crains aucun mal. |
| DeepL | Même si je marche dans la vallée de l’ombre de la mort, je ne craindrai aucun mal. |
| Reverso | Oui, bien que je marche à travers la vallée de l’ombre de la mort, je ne craindrai aucun mal. |
| Google Translate | Quand je marche dans la vallée de l’ombre de la mort, je ne crains aucun mal. |
| **Bible liturgique officielle (AELF)** | Si je traverse les ravins de la mort, je ne crains aucun mal. |
| **Bible protestante (Segond, 1910)** | Quand je marche dans la vallée de l’ombre de la mort, je ne crains aucun mal. |

---

## 3. Shakespeare

### 3.1 And yet, by heaven, I think my love as rare / As any she belied with false compare.

| Système | FR |
|---|---|
| T5-small | Et pourtant, par le ciel, je pense mon amour comme rare / Comme n’importe quelle elle a lu avec de faux comparaison. |
| MarianMT | Et pourtant, par le ciel, je pense que mon amour est aussi rare / Comme toute autre qu’elle a trahi avec fausse comparaison. |
| mBART-50 | Et pourtant, par Dieu, je pense que mon amour est aussi rare / que tout ce qu’elle a crié avec fausse comparaison. |
| NLLB-200 | Et pourtant, par le ciel, je pense que mon amour est aussi rare que tout ce qu’elle a menti avec une fausse comparaison. |
| DeepL | Et pourtant, par le ciel, je crois que mon amour est aussi rare / Que tous ceux qu’elle a dénigrés par de fausses comparaisons. |
| Reverso | Et pourtant, par le ciel, je pense que mon amour est aussi rare / comme n’importe quelle autre personne qu’elle a démenti avec une fausse comparaison. |
| Google Translate | Et pourtant, par le ciel, je crois mon amour aussi rare / Que celle qu’elle dénigrait par de fausses comparaisons. |
| **Yves Bonnefoy** | Toutefois, et j’en jure : elle les vaut, ces autres / Que travestissent de menteuses comparaisons. |

### 3.2 Whoever hath her wish, thou hast thy Will

| Système | FR |
|---|---|
| T5-small | Quiconque a son souhait, tu ai tu sa volonté |
| MarianMT | Celui qui a son désir, tu as ta volonté |
| mBART-50 | Quiconque le souhaite, tu a tes volontés. |
| NLLB-200 | Qui a son désir, tu as ta volonté |
| DeepL | Quiconque exprime un vœu, tu as ta volonté |
| Reverso | Quiconque a son souhait, tu as ta volonté |
| Google Translate | Celui qui a son désir, tu as ta volonté |
| **Yves Bonnefoy** | D’autres ont d’autres biens, toi tu as ton *Will* |

### 3.3 That time of year thou mayst in me behold / When yellow leaves, or none, or few, do hang / Upon those boughs which shake against the cold.

| Système | FR |
|---|---|
| T5-small | Cette période de l’année tu peux en moi voici / Quand des feuilles jaunes, ou aucune, ou peu, tu s’appât / Sur les bougies qui s’ébranlent contre le froid. |
| MarianMT | Cette période de l’année, tu peux voir en moi / Quand les feuilles jaunes, ou aucune, ou peu, accrochent / Sur les branches qui secouent contre le froid. |
| mBART-50 | Quand les feuilles jaunes, voire aucune, voire quelques-unes, sont suspendues sur les bourgeons qui s’écoulent contre le froid, c’est un moment de l’année. |
| NLLB-200 | Tu me verras en cette saison, quand les feuilles jaunes, ou les unes, ou les autres, pendent sur les rameaux qui tremblent contre le froid. |
| DeepL | À cette époque de l’année, tu pourras me contempler / Quand des feuilles jaunes, ou aucune, ou quelques-unes, pendent / Aux branches qui tremblent sous l’effet du froid. |
| Reverso | Cette période de l’année, tu peux la contempler en moi / Quand des feuilles jaunes, ou aucune, ou peu, ne pendent / Sur ces branches qui tremblent contre le froid. |
| Google Translate | Tu peux voir en moi cette saison de l’année où des feuilles jaunes — ou bien peu, ou aucune — pendent aux branches qui frissonnent sous le froid. |
| **Yves Bonnefoy** | Contemple en moi ce moment de l’année / Où ont jauni puis sont tombées les feuilles, / Et peu en restent, [chapelle en ruine, nue,] |

---

## 4. Contrat juridique

### 4.1 The Lessee shall indemnify and hold harmless the Lessor from and against any and all claims.

| Système | FR |
|---|---|
| T5-small | Le preneur indemnise et tient à l’abri de toute réclamation et contre celle-ci. |
| MarianMT | Le Locateur indemnisera le Locateur et le mettra à l’abri de toute réclamation. |
| mBART-50 | Le preneur doit indemniser le preneur et le garder inoffensif à l’égard de toute réclamation ou contre toute réclamation. |
| NLLB-200 | Le locataire indemnisera et indemnisera le locataire de toute réclamation et contre toute réclamation. |
| DeepL | Le locataire s’engage à indemniser et à dégager le bailleur de toute responsabilité à l’égard de toute réclamation. |
| Reverso | Le locataire indemnisera et dégagera de toute responsabilité le bailleur contre toute réclamation. |
| Google Translate | Le preneur devra indemniser le bailleur et le dégager de toute responsabilité à l’égard de toute réclamation. |

### 4.2 This Agreement shall be governed by and construed in accordance with the laws of the State of New York.

| Système | FR |
|---|---|
| T5-small | Le présent accord est réglementé et interprété conformément aux lois de l’État de New York. |
| MarianMT | Le présent Accord sera régi et interprété conformément aux lois de l’État de New York. |
| mBART-50 | Le présent Accord est régi et interprété conformément aux lois de l’État de New York. |
| NLLB-200 | Le présent accord est régi par les lois de l’État de New York et interprété conformément à celles-ci. |
| DeepL | Le présent contrat est régi par les lois de l’État de New York et doit être interprété conformément à celles-ci. |
| Reverso | Le présent Contrat sera régi et interprété conformément aux lois de l’État de New York. |
| Google Translate | Le présent accord est régi par les lois de l’État de New York et interprété conformément à celles-ci. |

### 4.3 The parties hereto agree that any dispute arising hereunder shall be resolved by binding arbitration.

| Système | FR |
|---|---|
| T5-small | Les parties conviennent que tout différend qui s’ensuit est réglé par arbitrage contraignant. |
| MarianMT | Les parties conviennent que tout différend découlant des présentes dispositions sera réglé par arbitrage contraignant. |
| mBART-50 | Les parties conviennent que tout différend découlant des présentes sera résolu par arbitrage contraignant. |
| NLLB-200 | Les parties conviennent que tout litige découlant de la présente disposition sera résolu par un arbitrage contraignant. |
| DeepL | Les parties conviennent que tout litige découlant du présent contrat sera tranché par voie d’arbitrage exécutoire. |
| Reverso | Les parties aux présentes conviennent que tout litige découlant des présentes sera résolu par arbitrage exécutoire. |
| Google Translate | Les parties conviennent que tout différend découlant des présentes sera tranché par voie d’arbitrage exécutoire. |

---

## 5. Notice technique

### 5.1 Tighten screw A to 5 Nm.

| Système | FR |
|---|---|
| T5-small | 2.2.1.2.1.2.1.2.1.2.1.2.1.2.1.2.1.2.1.2.1.2.1.2.1.2.1.2.1.2.1.2.… |
| MarianMT | Vis serrée A à 5 Nm. |
| mBART-50 | Tisser le vis A jusqu’à 5 Nm. |
| NLLB-200 | Resserrer la vis A à 5 Nm. |
| DeepL | Serrez la vis A à 5 Nm. |
| Reverso | Serrez la vis A à 5 Nm. |
| Google Translate | Serrez la vis A à 5 Nm. |

### 5.2 Do not immerse the device in water.

| Système | FR |
|---|---|
| T5-small | Ne pas plonger l’appareil dans l’eau. |
| MarianMT | Ne pas immerger l’appareil dans l’eau. |
| mBART-50 | Ne pas immerger l’appareil dans l’eau. |
| NLLB-200 | Ne plongez pas l’appareil dans l’eau. |
| DeepL | Ne plongez pas l’appareil dans l’eau. |
| Reverso | N’immergez pas l’appareil dans l’eau. |
| Google Translate | Ne pas immerger l’appareil dans l’eau. |

### 5.3 Press the power button for 3 seconds to turn on the device.

| Système | FR |
|---|---|
| T5-small | Appuyez sur le bouton de puissance pendant 3 secondes pour appuyer sur le dispositif. |
| MarianMT | Appuyez sur le bouton d’alimentation pendant 3 secondes pour activer l’appareil. |
| mBART-50 | Cliquez sur le bouton d’alimentation pendant 3 secondes pour activer l’appareil. |
| NLLB-200 | Appuyez sur le bouton d’alimentation pendant 3 secondes pour allumer l’appareil. |
| DeepL | Appuyez sur le bouton d’alimentation pendant 3 secondes pour allumer l’appareil. |
| Reverso | Appuyez sur le bouton d’alimentation pendant 3 secondes pour allumer l’appareil. |
| Google Translate | Appuyez sur le bouton d’alimentation pendant 3 secondes pour allumer l’appareil. |

---

## 6. Slogans

### 6.1 Be a goat. (Columbia Sportswear)

| Système | FR |
|---|---|
| T5-small | tre une chèvre (Columbia Sportswear) |
| MarianMT | Soyez une chèvre. (Columbia Sportswear) |
| mBART-50 | Soyez une chèvre. (Columbia Sportswear) |
| NLLB-200 | Sois une chèvre. |
| DeepL | Fais comme une chèvre. |
| Reverso | Sois une chèvre. (Columbia Sportswear) |
| Google Translate | Soyez une chèvre. (Columbia Sportswear) |

### 6.2 Taste. Not waist. (Weight Watchers)

| Système | FR |
|---|---|
| T5-small | Taste, pas waist. (Veilleurs de poids) |
| MarianMT | Pas la taille. |
| mBART-50 | Taste. Non Taille. (Vérificateurs de la taille) |
| NLLB-200 | Le goût, pas la taille. |
| DeepL | Le goût. Pas la taille. |
| Reverso | Le goût. Pas la taille. (Weight Watchers) |
| Google Translate | Le goût. Pas la taille. (Weight Watchers) |

### 6.3 Finger Lickin’ good. (KFC)

| Système | FR |
|---|---|
| T5-small | l’aise, il y a eu un accroissement de la pression et de la pression. |
| MarianMT | C’est bon, le doigt. |
| mBART-50 | Finger Lickin’ bon. (KFC) |
| NLLB-200 | Le "Démarrer les doigts" va bien. |
| DeepL | À s’en lécher les doigts. |
| Reverso | Finger Lickin’ good. (KFC) |
| Google Translate | À s’en lécher les doigts. (KFC) |

---
## Étape 2
### A. La stratégie de traduction
#### A.1. Le système a-t-il conservé les références culturelles ou les a-t-il adaptées ?

En général, les systèmes conservent ou calquent plutôt qu’ils n’adaptent. Quand une référence culturelle est bien attestée en français, les meilleurs systèmes la retrouvent, mais les petits modèles et les jeux de mots se perdent.

- **Citations bibliques** : Les tableaux comparent les systèmes à la version liturgique officielle (AELF).
  - 2.1 : « l’esprit est *bien* disposé, mais la chair est faible » est la formule de la tradition protestante (Segond), devenue proverbiale. NLLB, DeepL et Google la reproduisent. T5, MarianMT, mBART et Reverso donnent « est disposé », correct mais moins proche de la formule établie. La liturgie catholique (AELF) dit au contraire « l’esprit est *ardent* », plus fort que *willing*. C'est aussi la formule choisie par <a href="https://fr.wikipedia.org/wiki/L%27esprit_est_ardent_mais_la_chair_est_faible">Wikipedia</a>. Aucun système ne reprend la formulation catholique : il n’y a pas une seule « bonne » formule, mais des traditions confessionnelles différentes, et les systèmes suivent celle de la formule la plus répandue.
  - 2.2 : DeepL est le seul à écrire « le *Verbe* », à l'instar de l’AELF. Les autres systèmes choisissent « la Parole », comme Segond. Aucun ne rend l’AELF « *auprès de* Dieu » (ils écrivent « avec »). T5 supprime la première proposition (« Au début, la Parole était avec Dieu, et la Parole était Dieu »).
  - 2.3 : l’AELF reformule nettement : « Si je traverse les *ravins* de la mort, je ne crains aucun mal ». Elle n’a ni *Yea* ni « l’ombre de la mort » comme image de la vallée. Tous les systèmes gardent la « vallée de l’ombre de la mort ». Google (« Quand je marche… ») reprend mot pour mot la version Segond, mais perd le *Yea, though* concessif. Les autres systèmes restent plus proches de l’anglais.
  - Cependant, il convient de préciser que les phrases anglaises suivent la tradition de la *King James Bible*, alors que l’AELF et Segond traduisent directement de l’hébreu et du grec. Leurs écarts avec les systèmes viennent donc en partie d’un texte source différent. Ces traductions servent de point de comparaison, et des traductions fidèles à l’anglais peuvent légitimement s’en écarter.
- **Jeux de mots shakespeariens** : « Whoever hath her wish, thou hast thy *Will* » joue sur *will*, qui désigne à la fois le prénom du poète, la volonté et le désir. Tous les systèmes le rendent par le seul nom commun « volonté », et le jeu de mots disparaît ; DeepL propose même « exprime un vœu » pour *wish*. Les traducteurs humains répartissent ces sens entre plusieurs mots ou, comme Bonnefoy, gardent *Will* comme nom propre, ce qu’aucun système ne fait (Lacroix, 2024). Les systèmes traduisent phrase par phrase et ne peuvent pas compenser une perte en la rattrapant ailleurs dans le poème.
- **Slogans** :
  - 6.1 : *GOAT* (*Greatest Of All Time*) est traduit littéralement par « chèvre » par tous les systèmes. La référence au « meilleur de tous les temps » est perdue.
  - 6.2 : le jeu *taste / waste* (homophone de *waist*) disparaît partout. NLLB, DeepL, Reverso et Google conservent le sens littéral (« le goût, pas la taille »).
  - 6.3 : seuls DeepL et Google retrouvent l’équivalent français (« À s’en lécher les doigts »).
  - Les noms de marque sont traités de façon inégale. Les systèmes les gardent (Marian, mBART, Reverso, Google), ou les suppriment (NLLB, DeepL). T5 et mBART traduisent « Weight Watchers » littéralement : « Veilleurs de poids » et « Vérificateurs de la taille ». C’est une erreur sur une entité nommée.
- **Hashtags** : Les systèmes gardent `#CorporateLife` et `#MondayMood` tels quels quand ils les reproduisent (NLLB omet le second), sauf Google, qui les traduit : `#VieEnEntreprise`, `#HumeurDuLundi`. C’est une adaptation à la langue cible et une posture résolumment naturaliste (voir *infra*). Elle est lisible en français, mais un hashtag est un identifiant partagé : traduit, il ne renvoie plus à la même conversation.
- **Termes juridiques** : « State of New York » est conservé partout (« l’État de New York »). *Lessee* et *Lessor* sont rendus en « preneur », « bailleur » ou « locataire », et les mauvais systèmes confondent les deux (voir « Erreurs de traduction » plus bas).

### 2.2. Le registre (familier, soutenu, archaïque) est-il préservé ?

Le registre soutenu et technique est bien préservé. Le familier l’est beaucoup moins, et l’archaïsme n’est préservé par aucun système.

- **Familier (tweets)** : Le registre est préservé seulement par DeepL et Google dans l’exemple 1.3 « im so done w/ this rn » : DeepL « J’en ai vraiment marre de ça là » et Google « J’en ai tellement marre de tout ça en ce moment » gardent le ton oral. MarianMT, mBART, NLLB et Reverso lisent *done* comme un verbe d’action (T5 ne produit que le hashtag) (voir 2.3). L’abréviation *rn* (*right now*) n’est comprise que de Google et de DeepL ; Reverso la laisse telle quelle.
- **Émojis (tweets)** :
  - 1.1 : T5 et MarianMT suppriment l’émoji. mBART le remplace par 😉, ce qui change le ton (de l’exaspération à la complicité). NLLB, DeepL, Reverso et Google conservent 🙄.
  - 1.2 : seuls DeepL, Reverso et Google conservent 😅. Les autres le suppriment.
- **Soutenu et archaïque (Bible, Shakespeare)** :
  - 2.3 : « *Yea* » est un archaïsme solennel. T5, MarianMT, mBART et Reverso le traduisent par un « Oui » moderne, qui sonne comme une réponse à une question. NLLB, DeepL et Google l’ignorent. L’AELF elle-même n’a aucun archaïsme (« Si je traverse… »), car le français liturgique est contemporain : l’absence d’archaïsme n’est donc pas forcément une faute pour un texte biblique.
  - 3.1 à 3.3 : le *thou* est rendu par « tu » partout, ce qui rend l’adresse intime, mais aucune forme archaïque du français n’est utilisée pour *hath*, *hast* et *mayst*. La solennité poétique devient un français moderne neutre. À l’inverse, T5 rend *walk* par « se promène » (2.3), un verbe trop banal pour un texte solennel.
  - 3.3 : la **versification** est conservée en trois vers par MarianMT, DeepL et Reverso (avec « / »). Elle est perdue par mBART, NLLB et Google, qui réécrivent une phrase en prose, plus fluide mais qui n’est plus un poème. mBART déplace même « c’est un moment de l’année » à la fin.
  - 3.1 : mBART traduit *by heaven* par « par Dieu ». C’est fidèle à la valeur de serment du mot, mais plus explicite.
- **Soutenu juridique** : « Aux présentes », « des présentes » (Reverso, Google, mBART), « tranché par voie d’arbitrage exécutoire » (DeepL, Google, Reverso) : le registre contractuel est bien préservé, surtout par les systèmes en ligne. NLLB et mBART restent corrects pour 4.2 mais se perdent dans 4.1 (redondances).
- **Slogans** : *Be a goat* peut se traduire en « Soyez » (Marian, mBART, Google) ou « Sois » (NLLB, Reverso). Le choix entre vouvoiement et tutoiement change l’image de la marque (plus ou moins jeune).

### 2.3. Les idiomes sont-ils traduits littéralement ou fonctionnellement ?

Les systèmes traduisent littéralement par défaut. Seuls DeepL et Google utilisent des solutions fonctionnelles, lorsque l’équivalent français est répandu.

| Expression | Traduction littérale (ou ratée) | Traduction fonctionnelle |
|---|---|---|
| *I’m so done w/ this* (1.3) | « C’est ce que j’ai fait » (Marian), « J’ai bien fait » (mBART), « Je suis tellement en train de faire ça » (NLLB), « j’ai donc fait avec ce rn » (Reverso) | « J’en ai vraiment marre de ça » (DeepL), « J’en ai tellement marre » (Google) |
| *Living the dream!* (1.2) | « Vivre le rêve ! » (Marian, Reverso) ; phrase supprimée (T5, mBART, NLLB) | « C’est vraiment le rêve ! » (DeepL), « Le rêve ! » (Google) |
| *This meeting could’ve been an email* (1.1) | « aurait pu être un courriel / un e-mail » (T5, Marian, NLLB, Reverso, mBART) | « aurait pu se faire par e-mail » (DeepL), « un simple e-mail » (Google) |
| *Finger Lickin’ good* (6.3) | « C’est bon, le doigt » (Marian), « Le "Démarrer les doigts" va bien » (NLLB), non traduit (mBART, Reverso), hallucination (T5) | « À s’en lécher les doigts » (DeepL, Google) |
| *hold harmless* (4.1) | « garder inoffensif » (mBART) | « dégager de toute responsabilité » (DeepL, Reverso, Google) |
| *from and against any and all claims* (4.1) | « de toute réclamation et contre celle-ci » (T5), « ou contre toute réclamation » (mBART), « de toute réclamation et contre toute réclamation » (NLLB) : le doublet juridique est traduit mot à mot | « à l’égard de toute réclamation » (DeepL, Google), « contre toute réclamation » (Reverso) : le doublet est condensé |
| *The spirit is willing…* (2.1) | — | La formule figée existe à l’identique en français : tous les systèmes la retrouvent |

- Pourquoi la traduction littérale réussit quand l’expression existe aussi en français, mais échoue lorsque le calque n'est pas possible (ex. *Finger Lickin’ good*). Les modèles les plus petits (T5, Marian) restent sur le sens le plus fréquent du mot polysémique (*done* → *faire* et non *finir*).
- **Les jeux de mots** (*Taste / waste*, *Will*, *GOAT*) ne sont traduits fonctionnellement par aucun système.

### B. Les erreurs de traduction

Notre typologie combine deux sources : la terminologie de **Delisle** (1993, 1999) pour les fautes de sens et le mal-dit, et le cadre Multidimensional Quality Metrics (**MQM**) (2014, 2015) pour le classement en dimensions et sous-types et la notion de gravité. Les noms des catégories MQM suivent la version actuelle publiée sur themqm.org, qui diffère en partie de celle de l’article de 2014 (par exemple *Fluency* devenu *Linguistic conventions*). La correspondance entre les deux grilles, les définitions reformulées, la liste des erreurs et leur gravité sont de notre fait. Les exemples renvoient aux numéros des tableaux ci-dessus.

#### B.1. Cadre d’analyse

| Notion (Delisle) | Définition retenue | Équivalent MQM |
|---|---|---|
| Contresens | sens opposé à celui de la source, ou rôle inversé | *Accuracy › Mistranslation* |
| Faux sens | mot ou segment pris dans un sens qui n’est pas celui du contexte, sans être le contraire | *Accuracy › Mistranslation* |
| Non-sens | segment qui ne veut rien dire en français | *Linguistic conventions › Unintelligible* |
| Omission | élément de la source absent de la traduction | *Accuracy › Omission* |
| Ajout, surtraduction | élément ajouté, ou précision rendue explicite alors que la source la laisse implicite | *Accuracy › Addition, Overtranslation* |
| Mal-dit | sens correct, mais formulation maladroite, calquée ou non idiomatique | *Style › Awkward style, Unidiomatic style* |

MQM ajoute les catégories suivantes : terminologie (*Wrong term*), éléments non traduits ou traduits à tort (*Untranslated*, *Do not translate*), grammaire, orthographe et ponctuation, registre, et perte de sens comme celle d’un jeu de mots (*Undertranslation*).

**Précision** : Une erreur étant un écart par rapport à ce qu’on attend de la traduction, nous retenons ces hypothèses pour ce TP : traduire vers le français courant en conservant le sens, le registre et, si possible, l’effet du texte source ; ne pas traduire les noms propres, les marques et les hashtags ; conserver les émojis et la ponctuation.

**Gravité** (trois niveaux, qui reprennent la terminologie MQM *Critical*, *Major*, *Minor* ; les définitions sont les nôtres) :
- **Critique** : le sens est inversé ou perdu, ou la sortie est inutilisable (et, dans le domaine juridique, potentiellement dangereuse).
- **Majeure** : le sens est altéré mais reste globalement compréhensible.
- **Mineure** : défaut sans conséquence sur le sens.

#### B.2. Pertes communes à tous les systèmes

Trois pertes touchent les sept systèmes de la même façon. Elles relèvent de *Accuracy › Undertranslation* (MQM) : le sens littéral est rendu, mais la fonction du texte est perdue. MQM précise d’ailleurs qu’il identifie des problèmes dans un texte sans attribuer de faute à celui qui l’a produit : ces pertes sont réelles, mais elles tiennent à la tâche (traduire une phrase isolée) autant qu’aux systèmes.
- **3.2** : le jeu de mots sur *Will* (voir « Jeux de mots shakespeariens » en A.1).
- **6.1** : *GOAT* (« meilleur de tous les temps ») devient « chèvre ».
- **6.2** : le jeu *taste / waste* (*waist*) disparaît.

#### B.3. Bilan

Le relevé détaillé et le décompte figurent dans l’[annexe](annexe_erreurs.md). Ce qu’ils montrent :
- **mBART-50 (27) et T5-small (23)** cumulent le plus d’erreurs. Chez T5, les erreurs critiques sont des omissions et des non-sens (sortie vide, boucle, hallucination) ; chez mBART, ce sont surtout des faux sens (9).
- **MarianMT et NLLB-200 (17 chacun)** ont chacun une seule erreur critique, le contresens sur *Lessee* et *Lessor* (4.1). NLLB cumule surtout des omissions (7), souvent mineures (marques, émojis).
- **Les trois systèmes en ligne (5 erreurs chacun)** ne font aucune erreur critique. Les erreurs de DeepL sont des omissions de marque (3) et des surtraductions (2) : ce sont plus des choix de traduction que des fautes de compréhension. Google a des erreurs de non-traduction (hashtags traduits à tort) et de mal-dit (la poésie mise en prose). Reverso a deux erreurs majeures : *done* mal compris (1.3) et *Finger Lickin’* laissé en anglais (6.3).

Limites de ce bilan :
- Notre décompte des erreurs de traduction n'a pas fait l'objet ni d'une double annotation ni d'un accord inter-annotateurs.
- Le décompte est brut. MQM calcule normalement un score pondéré (une erreur critique pèse plus qu’une erreur mineure), ce qui n’est pas fait ici.
- La typologie de Delisle a été pensée pour corriger des traductions humaines. Pour la traduction automatique, certaines erreurs (boucles, hallucinations) n’y ont pas de place propre et sont rangées dans « non-sens » ou « omission » faute de mieux.
- Cette synthèse repose sur 18 phrases, une seule traduction par système, et sans traductions de référence ; elle reste donc subjective

## Etape 3 : rapport

| Système | Remarques |
|---|---|
| T5-small | Incohérent, hallucine, supprime des segments (1.2, 5.1, 6.3). Déconseillé pour cette tâche. |
| MarianMT | Correct sur les textes soutenus et sur des phrases simples. Lit trop littéralement les registres familiers et les noms. Confond *Lessee* et *Lessor* (4.1). |
| mBART-50 | Fluide mais prend des libertés (émoji, réordonnancement du vers 3.3, « Cliquez »). |
| NLLB-200 | Meilleur des modèles open-source sur le soutenu (seul modèle open-source à reproduire la formule établie en 2.1). Dégrade sur les tweets. Confond *Lessee* et *Lessor*. |
| DeepL | Le plus souvent fonctionnel : tweets, juridique, slogans. Il explicite parfois (« aurait dû prendre 5 minutes », « exprime un vœu »). |
| Reverso | Fidèle, mais assez littéral : ne comprend ni *rn* ni *Finger Lickin’ good*. |
| Google Translate | Souvent fonctionnel et naturel, mais adapte beaucoup (hashtags, Psaume 23) et réécrit la poésie en prose. |

- **Les erreurs critiques** sont concentrées sur trois cas : la boucle et l’hallucination de T5 (5.1, 6.3), la confusion bailleur/preneur dans le contrat (4.1, par MarianMT, mBART et NLLB) et « Tisser » pour *tighten* (mBART). Dans les trois cas, une post-révision humaine est indispensable.
- **Les systèmes en ligne** (DeepL, Reverso, Google Translate) ne font aucune erreur critique sur ce corpus. Leurs défauts sont surtout des choix de traduction (adaptation des hashtags, explicitation) plutôt que des erreurs de sens. La seule erreur majeure de sens est le contresens de Reverso sur *done*.
- **Les genres les plus exposés** sont le tweet, la poésie et les slogans du fait des double sens et des jeux de mots. Les textes standardisés (technique, juridique) donnent de meilleurs résultats, sauf pour les petits modèles.

### Étrangéisation et naturalisation

Face aux écarts culturels, un traducteur choisit entre deux stratégies. L’**étrangéisation** (approche « sourcière ») préserve l’identité du texte source et demande au lecteur de faire le voyage, quitte à le dérouter. La **naturalisation** (approche « cibliste ») remplace les éléments de la culture source par ceux de la culture cible, au risque d’effacer la première.

| Stratégie | Exemples observés dans le corpus |
|---|---|
| Naturalisation | « le Verbe » (DeepL, 2.2) ; « À s’en lécher les doigts » (DeepL, Google, 6.3) ; hashtags traduits (Google, 1.1 et 1.3) ; la prose de Google en 3.3 |
| Étrangéisation ou littéralité | *Will* gardé comme nom propre (Bonnefoy, 3.2) ; hashtags, marques et émojis conservés ; calques : « Soyez une chèvre » (6.1), « Vivre le rêve ! » (1.2) ; « Finger Lickin’ » laissé en anglais (mBART, Reverso, 6.3) |

D'après les exemples du TP1, chacun des systèmes semble alterner entre ces deux pôles, entre équivalence et calque, emprunt voire non-traduction. Ainsi, Google traduit les hashtags mais calque « Soyez une chèvre ». Les traducteurs humains, comme Yves Bonnefoy, semblent quant à eux plus constants dans leurs stratégies de traduction. Notre propre grille d'évaluation (partie B), en pénalisant les hashtags traduits, adopte une posture étrangéisante.

### Systèmes en ligne et modèles Hugging Face

Sur la base de ce TP1, nous pouvons affirmer que les trois systèmes en ligne ne font aucune erreur critique (cinq erreurs relevées chacun, dont deux majeures, toutes chez Reverso), alors que les quatre modèles Hugging Face en cumulent de 17 à 27, avec des erreurs critiques chez les quatre. La nature des défauts diffère aussi : ceux des systèmes en ligne sont surtout des choix (naturalisation, explicitation, adaptation), ceux des modèles Hugging Face des fautes (omissions, faux sens, non-sens). L’écart est le plus net sur le registre familier et les idiomes, sur les émojis et sur la terminologie juridique (*preneur* / *bailleur*) ; il se réduit sur les phrases courtes et standardisées. Toutefois, là encore, ces résultats seraient à confronter à un autre corpus et à un-e autre annotateur-ice.


## Références
> Mylène, Lacroix, « Whoever hath her wish, thou hast thy Will : traduire le substrat pornographique du Sonnet 135 de Shakespeare », in : Buisson, Françoise, Daguerre, Blandine, dir., Traduire le double langage : double jeu et double sens, Pau, PUPPA, Collection Alm@e Linguae 1, 2024, p. 83-102, [en ligne] https://una-editions.fr/whoever-hath-her-wish-thou-hast-thy-will/.

> Delisle, Jean (1993 / rééd. 2003). *La traduction raisonnée : manuel d’initiation à la traduction professionnelle de l’anglais vers le français*. Ottawa : Presses de l’Université d’Ottawa, coll. « Pédagogie de la traduction ».

> Delisle, Jean, Hannelore Lee-Jahnke et Monique C. Cormier (dir.) (1999). *Terminologie de la traduction / Translation Terminology / Terminología de la traducción / Terminologie der Übersetzung*. Amsterdam / Philadelphie : John Benjamins Publishing Company, coll. « FIT Monograph Series » (vol. 1), 433 p.

> Lommel, Arle, Hans Uszkoreit et Aljoscha Burchardt (2014). « Multidimensional Quality Metrics (MQM) : A Framework for Declaring and Describing Translation Quality Metrics ». *Revista Tradumàtica : tecnologies de la traducció*, n° 12, p. 455-463. DOI : 10.5565/rev/tradumatica.77.

> Mariana, Valerie, Troy L. Cox et Alan Melby (2015). « The Multidimensional Quality Metrics (MQM) framework : A new framework for translation quality assessment ». *The Journal of Specialised Translation (JoSTrans)*, vol. 23, p. 137-161.

> Consortium QT21 / W3C Community Group, *MQM : Multidimensional Quality Metrics*, https://themqm.org (typologie des erreurs MQM Core ; consulté le 4 octobre 2026).

> Schleiermacher, Friedrich (conférence de 1813). *Des différentes méthodes du traduire*, trad. Antoine Berman, Paris : Seuil, 1999.

> Venuti, Lawrence (1995). *The Translator’s Invisibility : A History of Translation*. Londres / New York : Routledge.
