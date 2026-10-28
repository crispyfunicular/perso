# PSOLA
## Librairies
1. Charger la bibliothèque principale (`parselmouth`) --> *boîte à outils*
2. Créer un raccourci vers `call` (fonction du sous-module `praat`) --> il suffira ensuite de taper `all` --> *tournevis*

```python
import parselmouth
from parselmouth.praat import call
```

Création d'un petit lecteur audio interactif directement dans l'environnement de travail pour écouter le résultat.

```python
import IPython.display as ipd
from IPython.display import Audio
```

## Chargement des données
Charger un fichier audio avec sa transcription temporelle -> création d'**objets Parselmounth** :
- `sound` : contient les données acoustiques du fichier audio --> sera analysé avec les outils de Praat.
- `segmentation` -> `segmentation[phonemes]`, `segmentation[mots]`, `segmentation[syllabes]`.  Les clés `phonemes`, `mots` et `syllabes` correspondent aux Tiers = lignes d'annotation dans Praat
- `diphone = segmentation[phonemes]` ->  liste d'objets `Interval`
- `interval.text` = chaîne de caractères
- `interval.xmin` / `interval.xmax` = début / fin de la case
```python
sound = parselmouth.Sound('logatomes.wav')
segmentation = textgrids.TextGrid('logatomes.TextGrid').
diphones = segmentation['phonemes'] 
```

### Modification de la hauteur (pitch)
Commande **manipulation** : transforme le son brut en objet manipulable --> obligatoire
- `0.01` : le fichier est découpé et analysé toutes les 10 ms.
- `75` / `600` (Hz) : limites de la fréquence fondamentale (F0)  
--> *Cherche la mélodie de la voix entre 75 Hz (très grave) et 600 Hz (très aigu)*

```python
manipulation = call(sound, "To Manipulation", 0.01, 75, 600)
```

`pitch_tier` : couche de données qui contient la mélodie de la voix (correspond à la F0) --> courbe de mélodie  
Liste de coordonnées mathématiques avec deux valeurs : le temps (en secondes) et la fréquence (en hertz). Ex : à 0.1 seconde on est à 120 Hz, à 0.2 seconde on est à 125 Hz, etc.

```python
pitch_tier = call(manipulation, "Extract pitch tier")
```

***
***

### Eviter les clics avec le passage à zéro
- `start_idx` = index ou numéro d'échantillon (ex : échantillon no 55125)
- `sr` = fréquence d'échantillonnage (souvent 44100 échantillons par seconde)
- index / fréquence = temps (en secondes) (ex : `55125 / 44100 = 1.25` s)
- `if channel[i] <= 0 < channel[i + 1]:` -> Est-ce que l'échantillon actuel (`channel[i]`) est négatif ou pile à zéro et est-ce que l'échantillon juste après (`channel[i + 1]`) est strictement positif ?
- `clean_start = i / sr` -> on prend l'index `i` de ce point et on le divise par la fréquence d'échantillonnage (`sr`) pour le convertir en secondes

```python
def zero_crossing_bounds(channel, start_idx, end_idx, sr):
    """Trouve les bornes propres par passage à zéro."""
    clean_start = start_idx / sr
    clean_end = end_idx / sr

    for i in range(start_idx, end_idx - 1):
        if channel[i] <= 0 < channel[i + 1]:
            clean_start = i / sr
            break

    for i in range(end_idx - 1, start_idx, -1):
        if channel[i] <= 0 < channel[i + 1]:
            clean_end = i / sr
            break

    return clean_start, clean_end
```

### Extraction des morceaux
- `milieu1` = centre du premier phonème (en sec)
- La multiplication des secondes (`milieu1`) par la fréquence d'échantillonnage permet d'obtenir une coordonnée spatiale dans le tableau (= index)

```python
def extraire_diphone(sound, interval1, interval2):
    """Extrait un diphone entre deux intervalles."""

    milieu1 = (interval1.xmin + interval1.xmax) / 2
    milieu2 = (interval2.xmin + interval2.xmax) / 2

    start_idx = int(milieu1 * sr)
    end_idx = int(milieu2 * sr)

    clean_start, clean_end = zero_crossing_bounds(channel, start_idx, end_idx, sr)
```

### Concaténation de la phrase
- Grâce à `numpy.concatenate` ou `np.concatenate`
- On obtient une voix synthétisée brute, sans intonation (hauteur et rythme constants "robotiques") --> PSOLA

```python
chaine_sampa = "sEtynafER"
for i in range(len(chaine_sampa) - 1):
    diphone = chaine_sampa[i:i+2]
```

## Modification prosodique (PSOLA)
PSOLA (Pitch Synchronous Overlap and Add) est un algorithme qui permet de modifier la **hauteur** (l'intonation) et le **rythme** d'une voix enregistrée **sans en déformer le timbre**.

### Modification de la hauteur (pitch) - pitch tier
Pour modifier la *hauteur* (le pitch), l'algorithme rapproche ces fenêtres les unes des autres (la voix devient plus aiguë) ou les écarte (la voix devient plus grave).

- `"Extract pitch tier"` : Extraction de la courbe mélodique de la synthèse
- `1.2` : multiplication des fréquences de la voix par 1,2 (= augmentation de 20%) --> voix plus aiguë
```python
pitch_tier = call(manipulation, "Extract pitch tier")
call(pitch_tier, "Multiply frequencies", sound.xmin, sound.xmax, 1.2)
```

- `t0` : temps de début
- `t1` : temps de fin
- `dur = t1-t0` : durée totale du fichier en secondes --> Permet de travailler non pas en secondes mais en pourcentages de la durée --> le code fonctionnera quelle que soit la durée de l'audio.
- `t0 + 0.40 * dur, 140` : On se place à 40% de la durée et on force la voix à être à 140 Hz
- `t0 + 0.95 * dur, 95` :  juste avant la fin, la voix chute dans les graves --> La phrase est terminée
```python
pitch_tier = call(manipulation, "Extract pitch tier")
t0 = sound.xmin
t1 = sound.xmax
dur = t1 - t0
call(pitch_tier, "Add point", t0 + 0.40 * dur, 140)
call(pitch_tier, "Add point", t0 + 0.95 * dur, 95)
call([manipulation, pitch_tier], "Replace pitch tier")
```

### Modification de la durée (vitesse) - duration tier
Pour modifier la *durée* (le rythme), l'algorithme duplique certaines fenêtres (pour ralentir/rallonger la voix) ou au contraire les supprime (pour l'accélérer).  
Au lieu d'extraire la mélodie, on extrait la grille du temps (le calque de durée ou "duration tier"). Par défaut, ce calque est une ligne droite horizontale à 1 (vitesse normale, 100% de la durée d'origine).

La vitesse est modifiée à un instant précis
- `0.5` (le moment) : on cible la seconde 0,5 du fichier audio.
- `1.5` (l'action) : le multiplicateur de durée. "À ce moment précis (`0.5`), étire le son pour qu'il dure 1,5 fois plus longtemps".
- --> À la seconde 0.5 s, la voix est ralentie d'un facteur 1.5

```python
duration_tier = call(manipulation, "Extract duration tier")
call(duration_tier, "Add point", 0.5, 1.5)
call([manipulation, duration_tier], "Replace duration tier")
```

### Overlap-Add
Après avoir écarté ou rapproché les ondes, l'algorithme les superpose (overlap) et les additionne (add) pour que le résultat soit fluide, sans aucun "clic" désagréable. --> réassemblage
```python
resynth = call(manipulation, "Get resynthesis (overlap-add)")
```

## Enregistrement
### Replace
Remplace le pitch original (`manipulation`) par le nouveau pitch (`pitch_tier`) qu'on vient de rendre plus aigu. La variable `manipulation` garde le même nom, mais son contenu a été mis à jour avec les modifications.
```python
call([manipulation, duration_tier], "Replace duration tier")
call([manipulation, pitch_tier], "Replace pitch tier")
```

### Sauvegarde sur l'ordinateur
```python
resynth.save("toto.wav","WAV")
```
