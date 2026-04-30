# Rapport — TTS par concaténation + WORLD (extension)

## Objectif
Mettre en œuvre une chaîne TTS de type **unit selection** à partir d’alignements MFA (phones) et d’une resynthèse WORLD légère pour lisser les discontinuités.

## Fichiers
- Notebook rendu (copie + section ajoutée) : `rendu_TTS/Vocodeurs_M1_TAL_version_finale.ipynb`
- Phrases + métadonnées : `rendu_TTS/manifest.json`
- Audios + TextGrids : `rendu_TTS/synthese_01.*` … `synthese_05.*`
- Code : `projet_tts.py` et `rendu_TTS/build_rendu_outputs.py`

## Modifications du notebook (principe “minimum”)
- Le fichier original `Vocodeurs_M1_TAL_version_finale.ipynb` à la racine du projet **n’est pas modifié**.
- Le rendu utilise une **copie** dans `rendu_TTS/` avec quelques cellules **ajoutées en fin** pour pointer vers les sorties.

## Amélioration proposée
- **Coarticulation / jonctions** : fenêtrage en bords de clips + **crossfade** entre unités + **WORLD resynth** sur la chaîne concaténée pour réduire les à-coups spectraux.

## Limites / problèmes rencontrés
- La sélection d’unités est **aléatoire** parmi les occurrences d’un phone : la qualité varie.
- Le placement temporel des phones dans le `TextGrid` de sortie est **approximatif** après resynthèse (normalisation longueur).

## Note environnement (reproductibilité)
Pour exécuter la chaîne WORLD hors notebook, l’environnement conda `mfa` a dû inclure `pyworld` et une version de `setuptools` compatible avec l’import `pkg_resources` requis par `pyworld` sur Python 3.14.

## Combescure (100 phrases)
Dans ce projet, les **100 phrases Combescure** correspondent aux enregistrements **`1-1` … `20-2`** : **20 listes × 2 fichiers**, chaque fichier `.lab` contenant **5 phrases** (donc **20 × 2 × 5 = 100**).

Les transcriptions orthographiques sont dans `corpus/*.lab` et les alignements MFA correspondants dans `aligned_one/*.TextGrid` (avec le tier `words` + `phones`).
