# Révisions code synthèse de la parole
## PSOLA
1. Charger la bibliothèque principale (`parselmouth`) --> *boîte à outils*
2. Créer un raccourci vers `call` (fonction du sous-module `praat`) --> il suffira ensuite de taper `all` --> *tournevis*

```python
import parselmouth
from parselmouth.praat import call
```

Création d'un petit lecteur audio interactif directement dans l'environnement de travail pour écouter le résultat (spécifique à ).

```python
import IPython.display as ipd
from IPython.display import Audio
```

Création d'un objet `sound` contenant les données acoustiques du fichier audio --> sera analysé avec les outils de Praat.
```python
sound = parselmouth.Sound("resultat_synthese.wav")
```
Commande **manipulation** : transforme le son brut en objet manipulable --> obligatoire
- `0.01` : le fichier est découpé et analysé toutes les 10 ms.
- `75` / `600` (Hz) : limites de la fréquence fondamentale (F0)  
--> *Cherche la mélodie de la voix entre 75 Hz (très grave) et 600 Hz (très aigu)*

```python
manipulation = call(sound, "To Manipulation", 0.01, 75, 600)
```

`pitch_tier` : couche de données qui contient la mélodie de la voix (correspond à la F0) --> courbe de mélodie  
Liste de coordonnées mathématiques avec deux valeurs : le temps (en secondes) et la fréquence (en hertz). Ex : à 0.1 seconde on est à 120 Hz, à 0.2 seconde on est à 125 Hz, etc.
- `1.2` : modification mathématique des valeurs de la courbe de mélodie --> multiplication des fréquences de la voix par 1,2 (= augmentation de 20%). --> La voix paraîtra plus aiguë.

```python
call(pitch_tier, "Multiply frequencies", sound.xmin, sound.xmax, 1.2)
```

- `manipulation`
- `pitch_tier`  
--> *Remplace le pitch original (`manipulation`) par le nouveau pitch (`pitch_tier`) qu'on vient de rendre plus aigu*

```python
call([manipulation, pitch_tier], "Replace pitch tier")
```

```python
resynth.save("toto.wav","WAV")
```

```python

```

```python

```

```python

```