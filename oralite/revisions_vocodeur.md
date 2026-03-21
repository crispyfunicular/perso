# Vocodeur

## Librairie Librosa
`sr=None` : on force Librosa à conserver la fréquence d'origine, sans rééchantillonnage (pour pouvoir analyser les hautes fréquences pour /s/ et /f/)
```python
signal, sr = librosa.load("PTSVOX_LG007_F_session1_mic_S_1_extrait1.wav", sr=None)
```
On divise le nombre d'échantillons par la fréquence d'échantillonnage (nbr d'échantillons par secondaire) pour obtenir l'axe t des secondes => **Le temps `t` est égal au numéro de l'échantillon divisé par la fréquence d'échantillonnage (`sr`)**
```python
t = np.arange(len(signal))/sr
```

## Transformée de Fourier
La fonction FFT renvoie des nombres complexes --> `np.abs(fft)` pour ne conserver que la magnitude de chaque fréquence (perte de l'information temporelle)
```python
from numpy.fft import fft
fft = fft(signal)
freqs = np.fft.fftfreq(len(signal), 1/sr)
plt.plot(freqs, np.abs(fft))
```
## Spectrogramme
- `librosa.stft()` : Au lieu de faire une FFT sur tout le fichier d'un coup, l'algorithme découpe l'audio en toutes petites "fenêtres" (par exemple de 20 millisecondes) qui se chevauchent et fait une FFT sur chacune d'entre elles. --> **trame** = photo instantanée du conduit vocal
- `.amplitude_to_db()` : L'oreille humaine ne perçoit pas le volume de manière linéaire, mais de manière logarithmique --> Convertir l'amplitude mathématique en décibels (dB) permet d'avoir une image qui correspond à ce que l'on entend vraiment.
```python
S = librosa.stft(signal)
S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='hz')
```

## PAS
- Intervalle de temps qui sépare le début d'une trame de la suivante.
- Par défaut, le vocodeur WORLD utilise un PAS de 5 ms (0.005 s). Cela signifie qu'il calcule une nouvelle valeur de pitch (`f0`), d'enveloppe (`sp`) et de souffle (`ap`) exactement toutes les 5 millisecondes. --> L'ordinateur fait son calcul, avance de 5 ms sur le fichier audio, et refait un calcul.
- Le PAS permet de passer du temps réel (secondes) au temps informatique (trames) --> Un phonème de 80 ms occupera 16 trames.
- => Le *taux d'échantillonnage* crée les milliards de petits points du fichier audio (non modifiable a posteriori) et le *PAS* est la vitesse à laquelle l'algorithme avance au milieu de ces points pour prendre ses photos (modifiable a posteriori).

## Enveloppe spectrale
### Trame (frame) et fenêtre de Hamming
- On isole une fraction de seconde pendant laquelle on considère que la bouche est figée (une voyelle)
- 12048-10000 = 2048 = 2^11 : L'algorithme de la FFT travaille de manière optimale sur les puissances de 2.
- `np.hamming` : création d'une courbe mathématique en forme de cloche
- `frame * window` : multiplication de la trame par la cloche --> adoucit les extrémités --> évite les sauts et les "clics" abrupts aux extrémités
```python
frame = signal[10000:12048]
window = np.hamming(len(frame))
frame = frame * window
```
- `plt.plot(x, y)` : trace une courbe avec x en abscisses et y en ordonnées
- `20*np.log10(np.abs(fft_frame))` : conversion en décibels
- `np.log10()` : écrase les valeurs pour reproduire la façon dont l'oreille humaine entend les sons (elle est plus sensible aux variations dans les sons faibles que dans les sons forts).
```python
plt.plot(freqs, 20*np.log10(np.abs(fft_frame)))
```
```python
plt.xlim(0, 5000)
plt.title("Spectre d'une trame")
plt.show()
```

### Filtre gaussien
`gaussian_filter1d` 
Pour trouver la forme de la bouche, on ne veut pas voir chaque petite harmonique, on veut voir la forme globale (les formants). --> il faut lisser les harmoniques pour voir les formants --> moyenne glissante des petits pics --> Les dents de scie sont lissées pour ne laisser apparaître qu'une courbe globale et continue = enveloppe spectrale (= empreinte de la bouche et de la langue)
```python
from scipy.ndimage import gaussian_filter1d
envelope = gaussian_filter1d(np.abs(fft_frame), sigma=10)
```

## WORLD
- Synthèse vocale TTS
- Repose sur le modèle source-filtre
- N'accepte que des flottants de 64 bits (`np.float64`)
```python
signal = signal.astype(np.float64)
```

### Extraction de la source (`f0`)
```python
_f0, t = pw.dio(signal, sr)
f0 = pw.stonemask(signal, _f0, t, sr)
```

### Extraction du filtre (`sp`)
L'enveloppe spectrale EST la représentation mathématique visuelle du filtre.
```python
sp = pw.cheaptrick(signal, f0, t, sr)
```

### Apériodicité / souffle (`ap`)
- Pour l'effet naturel
- `d4C` analyse le bruit dans la voix (ex : léger souffle d'air qui passe à travers les cordes vocales)
- `ap` = ratio son voisé / son non voisé pour chaque bande de fréquence
- --> En découpant le signal en bandes, WORLD arrive à synthétiser une voix extrêmement naturelle, car il sait exactement à quelle "hauteur" se trouve la mélodie, et à quelle "hauteur" se trouve le souffle
- Empêche la voix de sonner métallique ou robotique
```python
ap = pw.d4c(signal, f0, t, sr)
```

## TextGrid et concaténation
Lecture du TextGrid généré par Praat, qui indique pour chaque phonème un temps de début et de fin.
```python
tg = textgrids.TextGrid(NOM + '.corr.textgrid')
```
- `fd_ss` : début de la frame du phonème /s/
- `ff_ss` : fin de la frame du phonème /s/
```python
fd_ss, ff_ss = extraire_carac_phoneme(tier,'ss')
fd_aa, ff_aa = extraire_carac_phoneme(tier,'aa')
```

Concaténation de toutes les trames du phonème /s/ et de toutes les trames du phonème /a/ --> saccadé car pas de coarticulation
```python
f0_total = np.concatenate([f0[fd_ss:ff_ss],f0[fd_aa:ff_aa]])
sp_total = np.concatenate([sp[fd_ss:ff_ss],sp[fd_aa:ff_aa]])
ap_total = np.concatenate([ap[fd_ss:ff_ss],ap[fd_aa:ff_aa]])
```

## Synthèse paramétrique
- Le code cherche tous les /a/ prononcés par la locuteurice dans le corpus.
- `np.mean` : calcul du phonème moyen
  - enveloppe spectrale moyenne (`sp`)
  - apériodicité moyenne (`ap`)
  - pitch moyen (`f0`)
  - durée moyenne (`duree`) : la durée n'est pas enregistrée en secondes mais en nombre de trames.
```python
phonemes_corpus = {
    'aa', 'ai', 'an', 'au', 'bb', 'ch', 'dd', 'ei', 'eu', 'ff', 'gg', 'ii',
    'in', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'oe', 'on', 'ou', 'pp', 'rr',
    'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz', 'uy'
}
dico_sp, dico_ap, dico_f0, dico_duree = defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)
dico = {}
# dico_moyennes = {}
for phoneme in phonemes_corpus:
    dico[phoneme] = {
        "sp": np.mean(dico_sp[phoneme], axis = 0),
        "ap": np.mean(dico_ap[phoneme], axis = 0),
        "f0": np.mean(dico_f0[phoneme]),
        "duree": np.mean(dico_duree[phoneme])
    }
```

- Pour dire "soleil" (["ss", "oo", "ll", "ei", "jj"]), la fonction cherche dans le dictionnaire la "moyenne" de chaque phonème. Comme la recette ne dure qu'une seule trame (5 millisecondes), le code la multiplie/répète (extend([...]*n)) pour atteindre la durée moyenne normale de ce phonème.
- `n` = nombre de trames nécessaires pour le phonème dure le bon temps. Recalculé pour chaque phonème (plus court pour les occlusives et plus long pour les fricatives et les voyelles)
- `n = max(1,int(dico[phoneme]["duree"]))` : chaque phonème demandé durera au moins 1 trame (5 ms)
- si `n` = 16, la ligne `f0_total.extend([dico[phoneme]["f0"]]*n)` crée une liste de 16 fois la valeur 150 (`.extend()`) puis l'ajoute à la liste finale --> La voix est figée pendant toute la durée du phonème --> effet robot
- => La voix de synthèse sonne robotique mais le rythme de parole est naturel.
```python
def synthetiseur(sequence):
  f0_total, sp_total, ap_total = [], [], []
  for phoneme in sequence:
    n = max(1,int(dico[phoneme]["duree"]))
    f0_total.extend([dico[phoneme]["f0"]]*n)
    sp_total.extend([dico[phoneme]["sp"]]*n)
    ap_total.extend([dico[phoneme]["ap"]]*n)

y = synthetiseur(["ss", "oo", "ll", "ei", "jj"])
```