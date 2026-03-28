import parselmouth  # Bibliothèque pour le traitement de la parole (Praat en Python)
import matplotlib.pyplot as plt  # Pour tracer les graphiques (la forme d'onde)
import numpy as np  # Pour manipuler les données audio sous forme de tableaux numériques

import IPython.display as ipd  # Pour l'affichage d'outils interactifs dans un Notebook
from IPython.display import Audio  # Spécifiquement pour créer un lecteur audio

# pitch_tier = call(modif, "") # Ligne de commentaire (probablement un reste de test)

# Définition des noms de fichiers sources
son ="logatomes.wav"
grille = "logatomes.TextGrid"

# Chargement du fichier audio dans un objet Sound de Parselmouth
sound = parselmouth.Sound(son)

# Etape 1 : on coupe au milieu "à la hache" en s'aidant des valeurs approximatives
# Etape 2 : on adapte de façon à ce que ça coupe à 0

# Définition d'une fonction pour afficher un lecteur audio dans l'interface
def audio_player(audio_file):
    return ipd.display(Audio(audio_file))

# Extraction de deux segments spécifiques du son original (en secondes)
# extract_part(début, fin, forme_fenêtre, intensité relative, préserver_temps)
debut1 = sound.extract_part(111.84,112.03,parselmouth.WindowShape.RECTANGULAR, 1, False)
debut2 = sound.extract_part(231.85,232.05,parselmouth.WindowShape.RECTANGULAR, 1, False)

# Fusion (concaténation) des deux segments extraits en un seul objet sonore
son_total = sound.concatenate([debut1,debut2])

# Affichage du graphique de la forme d'onde
# son_total.xs() donne les coordonnées de temps (axe X)
# son_total.values.T donne l'amplitude (axe Y) transposée pour correspondre
plt.plot(son_total.xs(),son_total.values.T)
plt.show()

# Sauvegarde du nouveau son créé sur le disque dur
son_total.save("resultat.wav", "WAV")
print("Le fichier 'resultat.wav' a été créé.")

# Génération d'un lecteur audio interactif pour écouter le résultat directement
ipd.display(Audio(son_total.values, rate=son_total.sampling_frequency))


# --- Deuxième partie du script : Traitement par boucles et tableaux NumPy ---

# Liste de tuples contenant les bornes temporelles (début, fin) de plusieurs segments
segments = [
    (111.84, 112.03),
    (231.85, 232.05),
    (224.37, 224.57),
    (156.37, 156.55),
]

# Liste vide pour stocker les données numériques de chaque segment
extracted = []

# Boucle pour extraire chaque segment défini dans la liste ci-dessus
for start, end in segments:
    # Extraction du segment (preserve_times=False remet le temps du segment à 0s)
    segment = sound.extract_part(from_time=start, to_time=end, preserve_times=False)
    # On ajoute uniquement les valeurs numériques (l'amplitude) à notre liste
    extracted.append(segment.values)

# Fusion de tous les tableaux de données numériques horizontalement (les uns après les autres)
concatenated = np.hstack(extracted)

# Création d'un nouvel objet Sound à partir du tableau NumPy final
# On réutilise la fréquence d'échantillonnage du son d'origine
new_sound = parselmouth.Sound(values=concatenated, sampling_frequency=sound.sampling_frequency)