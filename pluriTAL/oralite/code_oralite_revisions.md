# Révisions code synthèse de la parole
## A
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

Création d'un objet `sound` contenant les données acoustiques du fichier audio --> sera analysé avec les outils de Praat.
```python
sound = parselmouth.Sound("resultat_synthese.wav")
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

`1.2` : modification mathématique des valeurs de la courbe de mélodie --> multiplication des fréquences de la voix par 1,2 (= augmentation de 20%). --> La voix paraîtra plus aiguë.

```python
call(pitch_tier, "Multiply frequencies", sound.xmin, sound.xmax, 1.2)
```

**Replace**  : Remplace le pitch original (`manipulation`) par le nouveau pitch (`pitch_tier`) qu'on vient de rendre plus aigu --> "Replace **pitch** tier"
La variable `manipulation` garde le même nom, mais son contenu a été mis à jour avec les modifications.

```python
call([manipulation, pitch_tier], "Replace pitch tier")
```

Génération d'un nouveau fichier à partir de manipulation
`overlap-add` : l'algorithme PSOLA découpe la voix en toutes petites ondes, les écarte ou les rapproche selon les modifications, puis les superpose en douceur (overlap) et les additionne (add) pour que le résultat soit fluide, sans aucun "clic" désagréable.

```python
resynth = call(manipulation, "Get resynthesis (overlap-add)")
```
***
***

Au lieu d'extraire la mélodie, on extrait la grille du temps (le calque de durée ou "duration tier"). Par défaut, ce calque est une ligne droite horizontale à 1 (vitesse normale, 100% de la durée d'origine)

```python
duration_tier = call(manipulation, "Extract duration tier")
```

### Modification de la vitesse
Modification de la vitesse à un instant précis
- `0.5` (le moment) : on cible la seconde 0,5 du fichier audio.
- `1.5` (l'action) : le multiplicateur de durée. "À ce moment précis, étire le son pour qu'il dure 1,5 fois plus longtemps".
- --> Le résultat : L'audio va ralentir ponctuellement autour de la demi-seconde.

```python
call(duration_tier, "Add point", 0.5, 1.5)
```

**Replace**  
```python
call([manipulation, duration_tier], "Replace duration tier")
```

- `t0` : temps de début
- `t1` : temps de fin
- `t1-t0` : durée totale du fichier en secondes  
--> Permettra de travailler non pas en secondes mais en pourcentages de la durée --> le code fonctionnera quelle que soit la durée de l'audio.

```python
t0 = sound.xmin
t1 = sound.xmax
dur = t1 - t0
```

`t0 + 0.40 * dur` : On se place à 40% de la durée et on force la voix à être à 140 Hz
```python
call(pitch_tier, "Add point", t0 + 0.40 * dur, 140)
```

`t0 + 0.95 * dur, 95` :  juste avant la fin, la voix chute dans les graves --> La phrase est terminée
```python
call(pitch_tier, "Add point", t0 + 0.95 * dur, 95)
```

**Replace**
```python
call([manipulation, pitch_tier], "Replace pitch tier")
```

**Génération**
```python
resynth = call(manipulation, "Get resynthesis (overlap-add)")
```

**Sauvegarde sur l'ordinateur**
```python
resynth.save("toto.wav","WAV")
```

## B
### Chargement des données
Charger un fichier audio avec sa transcription temporelle
Objets Parselmouth :  
- `segmentation` -> `segmentation[phonemes]`, `segmentation[mots]`, `segmentation[syllabes]`.  Les clés sont les Tiers = lignes d'annotation dans Praat
- `diphone = segmentation[phonemes]` ->  liste d'objets `Interval`
- `interval.text` = chaîne de caractères
- `interval.xmin` / `interval.xmax` = début / fin de la case
```python
sound = parselmouth.Sound('logatomes.wav')
segmentation = textgrids.TextGrid('logatomes.TextGrid').
diphones = segmentation['phonemes'] 
```

### Eviter les clics avec le passage à zéro
- `start_idx` = index ou numéro d'échantillon (ex : échantillon no 55125)
- `sr` = fréquence d'échantillonnage (souvent 44100 échantillons par seconde)
- index / fréquence = temps (en secondes) (ex : `55125 / 44100 = 1.25` s)
- `if channel[i] <= 0 < channel[i + 1]:` -> Est-ce que l'échantillon actuel (`channel[i]`) est négatif ou pile à zéro et  est-ce que l'échantillon juste après (`channel[i + 1]`) est strictement positif ?
- `clean_start = i / sr` -> on prend l'index `i` de ce point et le divise par la fréquence d'échantillonnage (`sr`) pour le convertir en secondes

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

#### Concaténation de la phrase
- Grâce à `numpy.concatenate` ou `np.concatenate`
- On obtient une voix synthétisée brute, sans intonation (hauteur et rythme constants "robotiques") --> PSOLA

```python
chaine_sampa = "sEtynafER"
for i in range(len(chaine_sampa) - 1):
    diphone = chaine_sampa[i:i+2]
```

### Modification prosodique (PSOLA)
#### Modification de la hauteur (pitch)
- Extraction de la courbe mélodique de la synthèse et multiplication des fréquences par 1.2 --> voix plus aiguë
```python
pitch_tier = call(manipulation, "Extract pitch tier")
call(pitch_tier, "Multiply frequencies", sound.xmin, sound.xmax, 1.2)
```

#### Modification de la durée (rythme)
- À la seconde 0.5, la voix est ralentie d'un facteur 1.5
```python
duration_tier = call(manipulation, "Extract duration tier")
call(duration_tier, "Add point", 0.5, 1.5)
```

#### contour intonatif manuel

```python
call(pitch_tier, "Add point", t0 + 0.40 * dur, 140)
```

## Résumé PSOLA
PSOLA (Pitch Synchronous Overlap and Add) est un algorithme qui permet de modifier la hauteur (l'intonation) et le rythme d'une voix enregistrée sans en déformer le timbre.
- Pour modifier la *durée* (le rythme), il duplique certaines de ces fenêtres (pour ralentir/rallonger la voix) ou en supprime (pour l'accélérer). -> `call(duration_tier, "Add point", 0.5, 1.5)` + `Replace duration tier`
- Pour modifier la *hauteur* (le pitch), il rapproche ces fenêtres les unes des autres (la voix devient plus aiguë) ou les écarte (la voix devient plus grave). -> `call(pitch_tier, "Add point", t0 + 0.40 * dur, 140)` + `Replace pitch tier`
- Le réassemblage (Overlap and Add) : Il superpose et additionne (fusionne) ces fenêtres réarrangées pour recréer un signal final parfaitement fluide, avec la nouvelle prosodie. -> `resynth = call(manipulation, "Get resynthesis (overlap-add)")`