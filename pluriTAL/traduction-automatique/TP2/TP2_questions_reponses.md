## 11. Bilan — questions pour votre compte-rendu

1. Comparez les trois scores sacreBLEU obtenus (mot-à-mot, IBM Model 1 + canal bruité, NLLB/LLM).
2. Donnez 3 exemples de phrases de votre corpus où votre système échoue, et reliez chaque échec à une hypothèse précise de IBM Model 1 (ordre des mots ? fertilité ? mot rare ?).
3. Le lexique bilingue extrait en section 6 est-il, lui, réellement utilisable ? Pour quel usage (pas forcément la traduction automatique complète) ?
4. Si vous deviez améliorer ce système sans passer au neuronal, quelle serait votre première piste (plus de données ? meilleur décodeur) ?
5. **Pour aller plus loin (optionnel) :** réentraînez avec plus d’itérations, ou sur un sous-ensemble plus grand de votre corpus — le score sacreBLEU de votre système progresse-t-il, et jusqu’où ?

## Réponses

### Question 1. Comparaison des trois scores sacreBLEU

| Système | sacreBLEU | COMET |
|---|---|---|
| Mot-à-mot | 2,8 | 0,38 |
| IBM Model 1 + canal bruité | 1,3 | 0,37 |
| NLLB-200 (Transformers / Torch) | **13,4** / 13,2 | 0,57 / 0,58 |

On constate que **NLLB est loin devant** (13,4 en sacreBLEU, 0,57 en COMET), alors que les deux autres systèmes restent sous 3 en sacreBLEU et sous 0,4 en COMET. Néanmoins, **un score de 13 reste modeste**, et cela se voit dans les sorties du modèle, du moins celles en français. En effet, si la plupart des traductions de NLLB sont fluides, elles contiennent parfois des erreurs (p. ex. « une stade d’oiseaux »). De manière inattendue, le **canal bruité** fait moins bien que le mot-à-mot (1,3 contre 2,8), et le score COMET va dans le même sens (0,37 contre 0,38 pour le mot-à-mot, et 0,57 pour NLLB).  

Cependant, il ne faudrait pas oublier que 1) IBM Model 1 représentait l’état de l’art en **1993** et que la traduction automatique a fait des bonds de géant depuis et que 2) la **taille du jeu de test est réduite** (30 phrases) et que quelques phrases erronées ont donc un fort impact sur le score global.

### Évaluation par un LLM juge (`Claude Sonnet 5.5`) pour l’évaluation qualitative et sémantique des sorties

Évaluer la justesse des paires du lexique ou la qualité d’une phrase en yiddish nécessite de comprendre le yiddish et ses nuances. L’évaluation qualitative et sémantique a donc été confiée à un LLM utilisé comme juge (« **LLM-as-a-Judge** »), pratique courante en évaluation de traduction, bien que non dénuée de limites. Les consignes données au juge et ses verdicts détaillés figurent en annexes 1 et 2.

**Juge**
- Modèle : `claude-sonnet-5-5` (Claude Sonnet 5.5, Anthropic).
- Mise en œuvre : instances distinctes lancées comme sous-agents depuis Claude Code, sans outil ni accès à la conversation. Les 36 paires ont été soumises en deux lots (22 et 14 paires) ; une troisième instance a servi au diagnostic de trois sorties du système (voir question 2 et annexe 1).

**Échantillon** : 36 paires, construites à partir du lexique de la section 6 (pour chaque mot français, le mot yiddish qui maximise t(f|e)) :
- 18 paires du lexique **tirées au hasard** (`random.seed(0)`) : 6 de probabilité haute (≥ 0,9), 6 de probabilité moyenne (0,5 à 0,9), 6 de probabilité faible (< 0,5) ;
- 10 paires du lexique **choisies à l’avance**, citées dans la réponse à la question 3 : *lune*, *rue*, *pluie*, *larmes*, *ici*, *joachim*, *ursula*, *heure*, *fer*, *dédaigné* ;
- 8 paires **de contrôle** : des paires fabriquées en associant *au hasard* un mot français de l’échantillon avec un mot yiddish. Sauf hasard heureux, il n’y a donc aucune raison pour que ces paires soient correctes ; elles permettent donc de vérifier que le juge ne répond pas « correcte » à tout. Résultat : les 8 paires de contrôle sont bien rejetées, ce qui signifie que le juge ne valide pas n’importe quelle paire.

**Résultats**

| Catégorie | Paires | correcte | partiellement correcte | incorrecte |
|---|---|---|---|---|
| Lexique, probabilité haute (≥ 0,9) | 13 | 12 | 1 | 0 |
| Lexique, probabilité moyenne (0,5 à 0,9) | 9 | 4 | 0 | 5 |
| Lexique, probabilité faible (< 0,5) | 6 | 0 | 1 | 5 |
| Contrôles (paires tirées au hasard) | 8 | 0 | 0 | 8 |

**Limites :**
- Le juge est un LLM : il peut se tromper en yiddish, langue peu dotée, et ses verdicts n’ont pas été relus par une personne lisant le yiddish. Il indique lui-même une fiabilité plus faible pour les locutions (notamment celle de la question 2b) et pour l’un des mots de la question 2a.
- L’échantillon est petit (28 paires du lexique, 8 paires de contrôle) et chaque paire est jugée une fois. Seules 18 des 28 paires du lexique sont tirées au hasard. Les proportions par catégorie sont donc indicatives.

### Question 2

L’analyse ci-dessous est faite d’après 1) le code, 2) les traductions de référence et 3) le diagnostic du LLM juge pour le sens des mots yiddish, sans que cela n’ait été relu par une personne lisant le yiddish. Le détail mot à mot figure en annexe 3.

**a) Mots rares ou absents de l’entraînement**

- SRC : *<span dir="rtl">שטראַליקע טויבן האָבן מיך געבראַכט אַהיים.</span>*
- HYP : « six “ voraces pupilles mansarde ” … . »
- REF : « Sept colombes nimbées de rayons m’ont ramené à la maison. »

**Hypothèses** :
- Trois mots n’apparaissent jamais dans les 430 phrases d’entraînement : <span dir="rtl">שטראַליקע</span> (« rayonnantes » selon le juge), <span dir="rtl">געבראַכט</span> (« apporté ») et <span dir="rtl">אַהיים</span> (« à la maison »). Puisque le modèle n’a appris aucune traduction pour eux, leur probabilité vaut 0 pour tous les mots français. Comme tous les candidats sont à égalité, le décodeur retient les derniers mots de son vocabulaire dans l’ordre des caractères, qui sont des signes de ponctuation (« … », « ” », « “ »). Ces trois mots porteurs de sens sont donc rendus par « “ », « ” » et « … ».
- Sur les 30 phrases de test, 85 des 506 mots source (17 %) n’apparaissent jamais à l’entraînement, et 66 (13 %) y apparaissent une ou deux fois.

**b) Un mot source ne correspond pas toujours à un seul mot cible (fertilité)**

- SRC : *<span dir="rtl">דער רעגן טוט אַ זעץ אין שויב מיט זײַנע בלײַענע פויסטן.</span>*
- HYP : « éclair pluie reste un coup rouge carreau près moisissure plomb “ . »
- REF : « La pluie cogne au carreau de ses poings de plomb. »

Selon le juge, les mots <span dir="rtl">טוט אַ זעץ</span> forment une locution (littéralement « fait un coup ») que la référence rend par le seul verbe « cogne ». La sortie « reste un coup » traduit manifestement chaque mot séparément et ne la reconstitue pas.  

**Hypothèse** : IBM Model 1 associe chaque mot source à un seul mot cible : il ne peut ni regrouper plusieurs mots source, ni en omettre, ni ajouter un mot sans équivalent dans la source.

**c) Ordre des mots**

- SRC : *<span dir="rtl">און ער האָט דערפילט, אַז דער קאָפּ, וואָס ער טראָגט שוין אַזוי פיל יאָרן אויף די אַקסלען, איז ניט זײַנער.</span>*
- HYP : « et sauver eut ressenti tu rien étoile tête , bas sauver voûtée pommes cela pourquoi années tord les épaules , est pas “ . »
- REF : « Et il a senti que la tête qu’il portait sur les épaules depuis tant d’années n’était pas la sienne. »

La sortie suit l’ordre des mots yiddish : « tête », « années » et « épaules » sont produits pour <span dir="rtl">קאָפּ</span>, <span dir="rtl">יאָרן</span> et <span dir="rtl">אַקסלען</span>, dans cet ordre, alors que la référence place « épaules » avant « années ».

**Hypothèse** : IBM Model 1 semble ne pas tenir compte de la position des mots et d’accorder la même probabilité à tous les alignements sont équiprobables, tandis que le décodeur conserve l’ordre de la source.

### Question 3 : Utilité du lexique bilingue

D’après les données issues du code (calcul de probabilités) et de l’analyse sémantique du LLM juge, le lexique bilingue est utilisable en tant que glossaire, à condition de fixer un seuil de fiabilité.

- Concernant **les mots fréquents et les noms propres**, les probabilités sont élevées et les paires jugées correctes (confiance haute) : *lune* (0,97), *rue* (0,98), *pluie* (0,97), *larmes* (0,96), *ici* (0,98), *joachim* (0,98), *ursula* (0,99).
- Concernant **les mots rares**, ceux-ci sont peu fiables, étant donné qu’un mot français vu une ou deux fois peut recevoir une probabilité élevée sur la base d’un nombre très limité d’exemples. Le juge déclare incorrectes, avec une confiance haute, ces trois paires portant sur des mots français vus 1 à 3 fois à l’entraînement : *heure → <span dir="rtl">זאָל</span>* (0,61), *fer → <span dir="rtl">ס’האָט</span>* (0,72), *dédaigné → <span dir="rtl">בית-עלמין</span>* (0,85). Parmi les 12 paires du lexique jugées non correctes ou partiellement correctes, 7 concernent un mot français vu une seule fois et 3 un mot vu deux fois.

Sur les 28 paires du lexique jugées, aucune des 13 paires de probabilité supérieure ou égale à 0,9 n’est jugée incorrecte (12 correctes et 1 partiellement correcte). À l’inverse, parmi les 15 paires de probabilité inférieure à 0,9, 10 sont jugées incorrectes et 4 correctes. Ainsi, fixer le **seuil à 0,9** et ne retenir que les paires de probabilité ≥ 0,9 écarte toutes les paires jugées incorrectes, au prix de perdre 4 paires correctes. 
Ce lexique pourrait présenter un intérêt (limité) s’il était révisé (ou du moins les paires sous le seuil de 0,9) par un expert humain capable de parler yiddish, ou pour une simple translittération des noms propres.

### Question 4 : Pistes d’amélioration sans passer au neuronal

1. **Le décodeur**  

Notre décodeur tire 200 combinaisons au hasard : le canal bruité n’a donc aucune garantie de faire au moins aussi bien que le mot-à-mot. Une recherche en faisceau (*beam search*), ou au minimum l’ajout systématique de la combinaison gloutonne parmi les candidats, est peu coûteuse et vérifiable rapidement.

2. **Plus de données**  

430 paires d’entraînement sont très peu : IBM Model 1 s’entraîne normalement sur des dizaines de milliers de phrases, et une grande partie du vocabulaire de test est inconnue. Un corpus plus grand réduirait les mots inconnus, cause majeure des échecs (question 2a).

### Question 5 (optionnelle) : Plus d’itérations ou plus de données

sacreBLEU sur les 30 phrases de test, en ne changeant que `N_ITER`.  
- Mot-à-mot : déterministe
- Canal bruité (décodeur aléatoire) : moyenne de 5 tirages et (min – max).  

| `N_ITER` | Mot-à-mot | Canal bruité : moyenne (min – max) |
|---|---|---|
| 1 | 0,1 | 0,1 (0,1 – 0,1) |
| 2 | 1,0 | 1,1 (0,8 – 1,4) |
| 5 | 2,5 | 1,9 (1,7 – 2,6) |
| 10 | 2,8 | 1,9 (1,0 – 2,7) |
| 20 | 2,8 | 1,8 (0,7 – 2,8) |
| 50 | 2,5 | 1,6 (1,3 – 1,8) |

**Conclusion.** Le score progresse très vite au début, puis plafonne : on passe de 0,1 avec une seule itération à 2,5 avec 5 itérations (mot-à-mot), puis à 2,8 avec 10 ou 20 itérations. Pour le canal bruité, les moyennes à 5, 10 et 20 itérations sont presque identiques (1,9 ; 1,9 ; 1,8) ; le décodeur, lui, est aléatoire et avec le même réglage, deux tirages peuvent donner des scores très différents (de 0,7 à 2,8 à 20 itérations). On ne peut donc pas dire que l’un de ces réglages est meilleur que les autres.

Cependant, là encore, la petite taille du corpus vient limiter la portée de nos conclusions car, avec 430 paires d’entraînement, beaucoup de mots du jeu de test sont inconnus ou trop rares pour que le modèle apprenne leur traduction, quel que soit le nombre d’itérations.
