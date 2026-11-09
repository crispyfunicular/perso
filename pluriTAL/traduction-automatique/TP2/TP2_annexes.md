## Annexes

### Annexe 1 : Consignes données au LLM juge

#### 1.1 Validation des paires du lexique

Les deux lots de paires ont reçu la consigne suivante (messages envoyés tels quels aux sous-agents ; seule la mise en forme Markdown est adaptée : les signes `<`, `>`, `[`, `]`, `*` et `_` sont protégés pour s’afficher).

> « Tu es relecteur/relectrice linguistique (yiddish &lt;-&gt; français) et tu agis comme JUGE dans une évaluation de lexique bilingue construit automatiquement. N'utilise AUCUN outil (pas de lecture de fichier, pas de recherche web, pas de Bash) : réponds uniquement à partir des informations ci-dessous et de tes connaissances. Ne cherche pas à deviner d'où viennent les paires.
>
> CONTEXTE. Un lexique yiddish -&gt; français a été extrait automatiquement d'un petit corpus parallèle littéraire (roman/poèmes, yiddish avec traduction française humaine). Pour chaque paire ci-dessous, on te donne un mot français, un mot yiddish proposé comme équivalent, et jusqu'à deux phrases du corpus contenant le mot yiddish (avec la traduction française humaine de la phrase). Certaines paires sont correctes, d'autres non (ne suppose aucune proportion). Le yiddish est écrit en alphabet hébreu avec points diacritiques (orthographe YIVO) ; les phrases peuvent être tronquées.
>
> TA TÂCHE. Pour chaque paire, juge si le mot yiddish est une traduction correcte du mot français, au sens d'un équivalent de dictionnaire (une différence de flexion — singulier/pluriel, conjugaison — ne rend pas la paire fausse). Appuie-toi sur le contexte fourni ET sur tes connaissances du yiddish. Verdicts autorisés (exactement ces mots) :
> - "correcte" : le mot yiddish est un équivalent direct du mot français ;
> - "partiellement correcte" : sens proche mais pas équivalent exact (hyperonyme, sens secondaire, autre forme grammaticale, mot qui apparaît seulement dans la même expression/phrase) ;
> - "incorrecte" : autre sens, mot grammatical sans rapport, nom propre sans rapport, etc. ;
> - "indéterminable" : tu ne peux pas trancher avec les informations disponibles.
> Ajoute une confiance ("haute", "moyenne" ou "faible") et une justification d'UNE phrase en français (donne le sens du mot yiddish tel que tu le comprends). Sois honnête sur tes incertitudes : le yiddish est une langue peu dotée et tu peux te tromper ; ne valide pas une paire par politesse.
>
> FORMAT DE RÉPONSE. Réponds avec : (1) une première ligne "MODELE: &lt;l'identifiant exact du modèle que tu es, tel que tu le connais, ou 'inconnu' si tu ne le connais pas&gt;" ; (2) puis UN SEUL tableau JSON, sans texte autour, de la forme \[{"id": 1, "verdict": "...", "confiance": "...", "justification": "..."}, ...\] avec une entrée par paire, dans l'ordre ; (3) puis une ligne finale "COMPETENCE: &lt;une ou deux phrases sur ta fiabilité en yiddish pour cette tâche&gt;".
>
> PAIRES À JUGER : »

Chaque paire était ensuite présentée sous la forme suivante (exemple : première paire du premier lot) :

> ### Paire 1
> Mot français : « chêne »
> Mot yiddish proposé : <span dir="rtl">דעמב</span>
> Exemples de phrases du corpus contenant le mot yiddish (yiddish, puis traduction française humaine) :
> - YI : <span dir="rtl">און די זעג בײַסט אײַן די ציינער אינעם דעמב און דער שניי אונטן ווערט באַזיפּט מיט פּורפורנעם זעגמעל.</span>
>   FR : La scie plante ses dents dans le chêne et la neige se crible de sciure pourpre.
> - YI : <span dir="rtl">מיר טרעטן אָפּ עטלעכע שפּאַנען פון דעמב און וואַשן אויס מיט שניי די פאַרביטערטע אויגן.</span>
>   FR : Nous reculons à quelques pas du chêne et lavons avec la neige fraîche l’amertume de nos yeux.

#### 1.2 Diagnostic de trois sorties du système

> « Tu es relecteur/relectrice linguistique (yiddish &lt;-&gt; français) et tu agis comme JUGE dans l'analyse d'erreurs d'un système de traduction automatique yiddish -&gt; français très rudimentaire (IBM Model 1 + modèle de langue bigramme, entraîné sur un petit corpus littéraire). N'utilise AUCUN outil (pas de lecture de fichier, pas de recherche web, pas de Bash) : réponds uniquement à partir des informations ci-dessous et de tes connaissances.
>
> TA TÂCHE. Pour chacun des 3 exemples ci-dessous, tu reçois : la phrase source en yiddish, la traduction de référence humaine en français, la sortie du système, et l'alignement position par position (le système produit exactement un mot français par mot yiddish, dans le même ordre). Fais un diagnostic mot à mot puis global :
> 1. Pour CHAQUE position, juge le mot français produit par rapport au mot yiddish, dans ce contexte : "correct" (traduction juste du mot), "partiel" (sens proche ou forme différente), "incorrect" (autre sens ou sans rapport), ou "ponctuation" pour un signe de ponctuation traduit par un signe identique. Donne en quelques mots le sens du mot yiddish tel que tu le comprends. Si le mot yiddish n'a pas d'équivalent à lui seul dans la référence (par exemple s'il fait partie d'une locution rendue par un seul mot français, ou si la référence l'omet), indique-le.
> 2. Identifie ensuite les erreurs principales de la sortie par rapport à la référence et classe-les parmi : "mot incorrect", "locution ou plusieurs mots yiddish rendus par un seul mot français (ou l'inverse)", "mot omis ou ajouté par rapport à la référence", "ordre des mots", "traduction libre de la référence (pas une erreur du système mais un écart de style)", "ponctuation", "autre". Pour chaque erreur, cite les positions concernées et explique en une phrase.
> 3. Donne un jugement global d'une phrase par exemple (la sortie est-elle compréhensible ? que reste-t-il du sens de la référence ?).
> Sois factuel, ne valide pas par politesse, et signale tes incertitudes : le yiddish est une langue peu dotée et tu peux te tromper. Ne fais aucune hypothèse sur le fonctionnement interne du système (il ne s'agit pas d'expliquer pourquoi il se trompe, mais de décrire ce qui est juste ou faux).
>
> FORMAT DE RÉPONSE. (1) première ligne "MODELE: &lt;l'identifiant exact du modèle que tu es, tel que tu le connais, ou 'inconnu'&gt;" ; (2) puis UN SEUL objet JSON, sans texte autour, de la forme {"exemples": \[{"n": 1, "mots": \[{"pos": 1, "yiddish": "...", "produit": "...", "verdict": "...", "sens": "...", "remarque": "..."}, ...\], "erreurs": \[{"type": "...", "positions": \[..\], "explication": "..."}\], "global": "..."}, ...\]} ; (3) puis une ligne finale "COMPETENCE: &lt;une ou deux phrases sur ta fiabilité en yiddish pour cette tâche&gt;". Garde les champs "sens" et "remarque" courts (moins de 15 mots).
>
> DONNÉES : »

Les données étaient présentées sous la forme suivante (exemple : troisième phrase) :

> ### Exemple 3
> Phrase source (yiddish) : <span dir="rtl">און אפשר איז גאָר שולדיק זײַן פּאַליטרע, האַ ?</span>
> Traduction de référence (humaine) : Et si la coupable était sa palette ?
> Sortie du système automatique : et maternelle est … “ son palette sans hein ?
> Alignement position par position produit par le système (mot yiddish -&gt; mot français produit) :
>    1. <span dir="rtl">און</span> -&gt; et
>    2. <span dir="rtl">אפשר</span> -&gt; maternelle
>    3. <span dir="rtl">איז</span> -&gt; est
>    4. <span dir="rtl">גאָר</span> -&gt; …
>    5. <span dir="rtl">שולדיק</span> -&gt; “
>    6. <span dir="rtl">זײַן</span> -&gt; son
>    7. <span dir="rtl">פּאַליטרע</span> -&gt; palette
>    8. <span dir="rtl">,</span> -&gt; sans
>    9. <span dir="rtl">האַ</span> -&gt; hein
>   10. <span dir="rtl">?</span> -&gt; ?

### Annexe 2 : Verdicts détaillés du LLM juge

#### 2.1 Les 36 paires jugées

**Détail des verdicts** (verdicts et justifications reproduits tels que rendus par le juge ; la probabilité est t(f|e)) :

| Mot français | Mot yiddish | Type | t(f\|e) | Verdict (confiance) | Justification du juge |
|---|---|---|---|---|---|
| ursula | <span dir="rtl">אורשוליאַ</span> | lexique, probabilité haute | 0,99 | correcte (haute) | <span dir="rtl">אורשוליאַ</span> est la translittération yiddish du prénom Ursula, et la traduction française de chaque phrase donne bien « Ursula ». |
| rue | <span dir="rtl">גאַס</span> | lexique, probabilité haute | 0,98 | correcte (haute) | <span dir="rtl">גאַס</span> signifie « rue », comme le montrent « de l'autre côté de la rue » et « par-dessus la rue noire ». |
| ici | <span dir="rtl">דאָ</span> | lexique, probabilité haute | 0,98 | correcte (haute) | <span dir="rtl">דאָ</span> est l'adverbe de lieu « ici », et les deux phrases le traduisent ainsi. |
| joachim | <span dir="rtl">יאָאַכים</span> | lexique, probabilité haute | 0,98 | correcte (haute) | <span dir="rtl">יאָאַכים</span> est la translittération yiddish du prénom Joachim, et la traduction française de chaque phrase donne bien « Joachim ». |
| vitre | <span dir="rtl">שויב</span> | lexique, probabilité haute | 0,97 | correcte (haute) | <span dir="rtl">שויב</span> signifie « vitre, carreau » en yiddish, ce que confirment les deux phrases. |
| lune | <span dir="rtl">לבנה</span> | lexique, probabilité haute | 0,97 | correcte (haute) | <span dir="rtl">לבנה</span> (levone) signifie « lune », et les deux phrases la traduisent par « lune ». |
| pluie | <span dir="rtl">רעגן</span> | lexique, probabilité haute | 0,97 | correcte (haute) | <span dir="rtl">רעגן</span> signifie « pluie » (regn), et les deux phrases le confirment. |
| main | <span dir="rtl">האַנט</span> | lexique, probabilité haute | 0,96 | correcte (haute) | <span dir="rtl">האַנט</span> signifie « main » en yiddish, ce que confirment les deux phrases. |
| larmes | <span dir="rtl">טרערן</span> | lexique, probabilité haute | 0,96 | correcte (haute) | <span dir="rtl">טרערן</span> est le pluriel de <span dir="rtl">טרער</span>, « larmes », confirmé par « deux larmes jumelles » et « ses larmes brûlantes ». |
| chêne | <span dir="rtl">דעמב</span> | lexique, probabilité haute | 0,95 | correcte (haute) | <span dir="rtl">דעמב</span> (demb) signifie « chêne » en yiddish, et le contexte confirme la traduction « chêne ». |
| souffle | <span dir="rtl">אָטעם</span> | lexique, probabilité haute | 0,95 | correcte (haute) | <span dir="rtl">אָטעם</span> signifie « souffle, haleine, respiration » en yiddish, ce que confirment les deux phrases. |
| kto | <span dir="rtl">קטאָ</span> | lexique, probabilité haute | 0,93 | partiellement correcte (moyenne) | <span dir="rtl">קטאָ</span> est la transcription du russe/polonais « kto » (qui) utilisée comme citation dans le texte ; c'est la même forme mais un mot étranger cité, pas un mot yiddish proprement dit. |
| ruelle | <span dir="rtl">געסל</span> | lexique, probabilité haute | 0,92 | correcte (haute) | <span dir="rtl">געסל</span> est le diminutif de <span dir="rtl">גאַס</span> (rue) et signifie « ruelle, petite rue », ce que confirment les deux phrases. |
| dédaigné | <span dir="rtl">בית-עלמין</span> | lexique, probabilité moyenne | 0,85 | incorrecte (haute) | <span dir="rtl">בית-עלמין</span> signifie « cimetière », alors que « dédaigné » correspond à <span dir="rtl">פאַרשעמט</span> dans la même phrase. |
| âme | <span dir="rtl">נשמה</span> | lexique, probabilité moyenne | 0,84 | correcte (haute) | <span dir="rtl">נשמה</span> signifie « âme » (hébreu <span dir="rtl">נשמה</span>), ce que confirment les deux phrases. |
| fer | <span dir="rtl">ס'האָט</span> | lexique, probabilité moyenne | 0,72 | incorrecte (haute) | <span dir="rtl">ס'האָט</span> est la contraction de « es hot » (« il/cela a »), un mot grammatical sans rapport avec « fer » (en yiddish, eyzn ou <span dir="rtl">ברזל</span>). |
| nom | <span dir="rtl">נאָמען</span> | lexique, probabilité moyenne | 0,66 | correcte (haute) | <span dir="rtl">נאָמען</span> signifie « nom », sans ambiguïté. |
| immense | <span dir="rtl">ריזיקע</span> | lexique, probabilité moyenne | 0,65 | correcte (haute) | <span dir="rtl">ריזיקע</span> est la forme fléchie de <span dir="rtl">ריזיק</span> « gigantesque, immense », qui traduit bien « immense ». |
| fleur | <span dir="rtl">אַרום</span> | lexique, probabilité moyenne | 0,64 | incorrecte (haute) | <span dir="rtl">אַרום</span> signifie « autour de » (préposition/adverbe) ; « fleur » se dit <span dir="rtl">בלום</span> ou <span dir="rtl">בלימעלע</span>, qui est le mot voisin dans la phrase. |
| heure | <span dir="rtl">זאָל</span> | lexique, probabilité moyenne | 0,61 | incorrecte (haute) | <span dir="rtl">זאָל</span> est l'auxiliaire du subjonctif ou de l'optatif (« que... », « devoir »), alors que « heure » se dit <span dir="rtl">שעה</span> ou <span dir="rtl">זייגער</span> selon le sens. |
| poussière | <span dir="rtl">קלאַנגען</span> | lexique, probabilité moyenne | 0,55 | incorrecte (haute) | <span dir="rtl">קלאַנגען</span> signifie « sons, notes » ; « poussière » se dit <span dir="rtl">שטויב</span>, qui apparaît dans les phrases (<span dir="rtl">שטויבזײַלן, שטויב</span>). |
| danser | <span dir="rtl">טאַנצן</span> | lexique, probabilité moyenne | 0,52 | correcte (haute) | <span dir="rtl">טאַנצן</span> est l'infinitif « danser » (substantif <span dir="rtl">טאַנץ</span> = danse), confirmé par la phrase. |
| vois | <span dir="rtl">זעסטו</span> | lexique, probabilité faible | 0,37 | partiellement correcte (haute) | <span dir="rtl">זעסטו</span> est la forme verbale « zest-u » (tu vois) avec le pronom clitique « tu » accolé ; le sens est correct mais ce n'est pas le verbe seul (<span dir="rtl">זען</span> / <span dir="rtl">זעסט</span>). |
| combien | <span dir="rtl">ליגן</span> | lexique, probabilité faible | 0,25 | incorrecte (haute) | <span dir="rtl">ליגן</span> signifie « être couché, gésir » ; « combien » correspond à <span dir="rtl">װיפֿל</span>, et <span dir="rtl">ליגן</span> n'apparaît que dans la traduction « gisant ». |
| lancinant | <span dir="rtl">שפּילט</span> | lexique, probabilité faible | 0,13 | incorrecte (haute) | <span dir="rtl">שפּילט</span> est la forme verbale « il joue » ; « lancinant » correspond ici à <span dir="rtl">נאָגנדיק</span> (nagnd'ik, qui ronge), pas à <span dir="rtl">שפּילט</span>. |
| délicats | <span dir="rtl">רעכטע</span> | lexique, probabilité faible | 0,08 | incorrecte (haute) | <span dir="rtl">רעכטע</span> signifie « droit(e) » (côté droit) ; « délicats » correspond à <span dir="rtl">איידעלע</span> (adjectif fin, délicat). |
| militaire | <span dir="rtl">אַמאָל</span> | lexique, probabilité faible | 0,07 | incorrecte (haute) | <span dir="rtl">אַמאָל</span> signifie « autrefois, un jour, parfois » ; « militaire » correspond à <span dir="rtl">סאָלדאַטסקן</span> (de soldat) dans la phrase. |
| déluge | <span dir="rtl">קעסל</span> | lexique, probabilité faible | 0,06 | incorrecte (haute) | <span dir="rtl">קעסל</span> signifie « chaudron, marmite » ; « déluge » correspond à <span dir="rtl">מבול</span> (verbe <span dir="rtl">מבולט</span>), pas à <span dir="rtl">קעסל</span>. |
| main | <span dir="rtl">איז</span> | contrôle (paire tirée au hasard) | 0,00 | incorrecte (haute) | <span dir="rtl">איז</span> est le verbe « est » (être) ; « main » se dit <span dir="rtl">האַנט</span>, qui apparaît à côté dans la phrase. |
| âme | <span dir="rtl">דעם</span> | contrôle (paire tirée au hasard) | 0,00 | incorrecte (haute) | <span dir="rtl">דעם</span> est l'article défini à l'accusatif/datif masculin (« le/au »), et « âme » se dit <span dir="rtl">נשמה</span> ; ici <span dir="rtl">דעם</span> précède seulement « <span dir="rtl">בר-מיננס</span> ». |
| combien | <span dir="rtl">ראָם</span> | contrôle (paire tirée au hasard) | 0,00 | incorrecte (haute) | <span dir="rtl">ראָם</span> est le nom propre Romm (imprimerie Veuve & Frères Romm) et n'a aucun rapport avec « combien » (qui se dit <span dir="rtl">װיפֿל</span>). |
| déluge | <span dir="rtl">איבעריק</span> | contrôle (paire tirée au hasard) | 0,00 | incorrecte (haute) | <span dir="rtl">איבעריק</span> signifie « superflu, de trop » ; « déluge » se dit <span dir="rtl">מבול</span>, et l'exemple fourni ne contient pas de déluge (décalage d'alignement). |
| pluie | <span dir="rtl">שלאַכט</span> | contrôle (paire tirée au hasard) | 0,00 | incorrecte (haute) | <span dir="rtl">שלאַכט</span> signifie « bataille » (la traduction française dit « cette bataille »), pas « pluie ». |
| rue | <span dir="rtl">וואָס</span> | contrôle (paire tirée au hasard) | 0,00 | incorrecte (haute) | <span dir="rtl">וואָס</span> est le pronom relatif ou interrogatif « que/qui/quoi », tandis que « rue » se dit <span dir="rtl">גאַס</span>. |
| lune | <span dir="rtl">זענט</span> | contrôle (paire tirée au hasard) | 0,00 | incorrecte (haute) | <span dir="rtl">זענט</span> est la forme « vous êtes » du verbe <span dir="rtl">זײַן</span>, sans rapport avec « lune » (<span dir="rtl">לבנה</span>). |
| ici | <span dir="rtl">קוקט</span> | contrôle (paire tirée au hasard) | 0,00 | incorrecte (haute) | <span dir="rtl">קוקט</span> est la forme verbale « regarde » (de <span dir="rtl">קוקן</span>), alors que « ici » correspond à <span dir="rtl">דאָ</span> dans la phrase, juste à côté. |

#### 2.2 Phrases fournies au juge pour les paires citées dans la question 2

**Phrases du corpus fournies au juge pour les paires citées dans la question 2** (reproduites telles qu’elles figuraient dans la consigne : phrase yiddish, puis traduction française humaine) :

| Mot français | Mot yiddish | Phrases fournies au juge |
|---|---|---|
| pluie | <span dir="rtl">רעגן</span> | YI : <span dir="rtl">גרינקייט פון מאָכיקע שטיינער אין אַ רעגן ;</span><br>FR : Vert de pierres moussues sous la pluie…<br><br>YI : <span dir="rtl">— מענטש, וואָס טוסטו, ביסטו בלינד, זעסטו ניט אַז אין רעגן איז גאָט ?</span><br>FR : — Homme, que fais-tu, tu es aveugle, tu ne vois pas Dieu dans cette pluie ? |
| joachim | <span dir="rtl">יאָאַכים</span> | YI : <span dir="rtl">— וואָס איז געשען, יאָאַכים ?</span><br>FR : — Que se passe-t-il, Joachim ?<br><br>YI : <span dir="rtl">— יאָאַכים, דער בוים איז אטנגעהילט אין רויך, עס טרערן מיר די אויגן.</span><br>FR : — Joachim, cet arbre est voilé de fumée, les yeux me piquent. |
| ursula | <span dir="rtl">אורשוליאַ</span> | YI : <span dir="rtl">אורשוליאַ פאַלט צו זײַנע פיס מיט אַ געוויין :</span><br>FR : Ursula tombe à ses pieds, en pleurs :<br><br>YI : <span dir="rtl">— אורשוליאַ, ניט דײַנע די זינד, קאָנסט זיך איבערצײַגן.</span><br>FR : — Ursula, ces péchés ne sont pas les tiens, tu peux t’en convaincre. |

#### 2.3 Diagnostic de trois sorties : décompte des verdicts mot à mot

| Exemple | Phrase du jeu de test | Positions | correct | partiel | incorrect | ponctuation |
|---|---|---|---|---|---|---|
| 1 | 14 | 22 | 5 | 2 | 13 | 2 |
| 2 | 21 | 12 | 4 | 1 | 6 | 1 |
| 3 | 6 | 10 | 5 | 0 | 4 | 1 |

### Annexe 3 : détail mot à mot des exemples de la question 2

Pour chaque mot source : sens selon le LLM juge, nombre d’occurrences dans les 430 phrases d’entraînement, mot produit par le décodeur et trois meilleurs candidats selon t(f|e).

**a) Mots rares** (phrase 14 du jeu de test, huit derniers mots sur 22)

| Position | Mot source | Sens selon le juge | Occurrences à l’entraînement | Mot produit | Trois meilleurs candidats selon t(f\|e) |
|---|---|---|---|---|---|
| 15 | <span dir="rtl">זיבן</span> | sept | 2 | six | six (0,19), sept (0,16), septième (0,15) |
| 16 | <span dir="rtl">שטראַליקע</span> | rayonnantes, à rayons | 0 | “ | … (0,00), ” (0,00), “ (0,00) |
| 17 | <span dir="rtl">טויבן</span> | colombes, pigeons | 3 | voraces | éveillent (0,06), étouffer (0,06), voraces (0,06) |
| 18 | <span dir="rtl">האָבן</span> | ont (auxiliaire) | 40 | pupilles | ont (0,87), pupilles (0,54), avons (0,38) |
| 19 | <span dir="rtl">מיך</span> | me | 14 | mansarde | mansarde (0,60), m’ (0,39), avais (0,27) |
| 20 | <span dir="rtl">געבראַכט</span> | apporté, amené | 0 | ” | … (0,00), ” (0,00), “ (0,00) |
| 21 | <span dir="rtl">אַהיים</span> | à la maison, chez soi | 0 | … | … (0,00), ” (0,00), “ (0,00) |
| 22 | <span dir="rtl">.</span> | point | 602 | . | . (0,81), heures (0,44), bonjour (0,32) |

**b) Fertilité, premier exemple** (phrase 21 du jeu de test, mots 3 à 5)

| Position | Mot source | Sens selon le juge | Occurrences à l’entraînement | Mot produit | Trois meilleurs candidats selon t(f\|e) |
|---|---|---|---|---|---|
| 3 | <span dir="rtl">טוט</span> | fait (verbe 'tun') | 4 | reste | reste (0,25), tremble (0,13), savonne (0,13) |
| 4 | <span dir="rtl">אַ</span> | un | 512 | un | une (0,85), un (0,69), humaine (0,45) |
| 5 | <span dir="rtl">זעץ</span> | coup, heurt | 8 | coup | coup (0,64), cogne (0,43), offre (0,19) |

**b) Fertilité, second exemple** (phrase 6 du jeu de test)

| Position | Mot source | Sens selon le juge | Occurrences à l’entraînement | Mot produit | Trois meilleurs candidats selon t(f\|e) |
|---|---|---|---|---|---|
| 1 | <span dir="rtl">און</span> | et | 259 | et | et (0,89), vieux (0,47), propre (0,38) |
| 2 | <span dir="rtl">אפשר</span> | peut-être | 2 | maternelle | seriné (0,13), plainte (0,13), maternelle (0,13) |
| 3 | <span dir="rtl">איז</span> | est | 118 | est | est (0,72), caniveau (0,63), coffret (0,43) |
| 4 | <span dir="rtl">גאָר</span> | tout à fait, vraiment | 0 | … | … (0,00), ” (0,00), “ (0,00) |
| 5 | <span dir="rtl">שולדיק</span> | coupable | 0 | “ | … (0,00), ” (0,00), “ (0,00) |
| 6 | <span dir="rtl">זײַן</span> | son, sa (possessif) | 90 | son | son (0,62), mettre (0,48), laisser (0,45) |
| 7 | <span dir="rtl">פּאַליטרע</span> | palette | 2 | palette | palette (0,48), vit (0,02), âmes (0,02) |
| 8 | <span dir="rtl">,</span> | virgule | 856 | sans | , (0,77), tu (0,50), sans (0,40) |
| 9 | <span dir="rtl">האַ</span> | hein ? (particule interrogative) | 2 | hein | hein (0,81), trancher (0,02), envie (0,02) |
| 10 | <span dir="rtl">?</span> | point d’interrogation | 64 | ? | ? (0,99), kto (0,07), tu (0,05) |

**Chiffres complémentaires** (30 phrases de test, 430 phrases d’entraînement)

| Mesure | Valeur |
|---|---|
| Mots source du test (hors ponctuation) jamais vus à l’entraînement | 85 sur 506 (17 %) |
| Mots source du test vus une ou deux fois à l’entraînement | 66 sur 506 (13 %) |
| Mots source distincts vus une seule fois à l’entraînement | 1625 sur 2618 (62 %) |
| Jetons « … », « ” », « “ » parmi les mots produits | 87 sur 616 (14 %) |
| Phrases où la référence est plus longue / aussi longue / plus courte que la source | 21 / 2 / 7 |
| Longueur moyenne (en mots) : source / référence | 20,5 / 22,7 |
| Phrases où la sortie a la même longueur que la source | 30 sur 30 |
