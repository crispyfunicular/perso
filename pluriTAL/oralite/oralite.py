import parselmouth
import matplotlib.pyplot as plt
import numpy as np

import IPython.display as ipd
from IPython.display import Audio

import soundfile as sf
import sounddevice as sd

# pitch_tier = call(modif, "")

son ="logatomes.wav"
grille = "logatomes.TextGrid"
sound = parselmouth.Sound(son)

# Etape 1 : on coupe au milieu "à la hache" en s'aidant des valeurs approximatives
# Etape 2 : on adapte de façon à ce que ça coupe à 0

def audio_player(audio_file):
    return ipd.display(Audio(audio_file))


debut1 = sound.extract_part(111.84,112.03,parselmouth.WindowShape.RECTANGULAR, 1, False)
debut2 = sound.extract_part(231.85,232.05,parselmouth.WindowShape.RECTANGULAR, 1, False)

son_total = sound.concatenate([debut1,debut2])
plt.plot(son_total.xs(),son_total.values.T)
plt.show()
son_total.save("resultat.wav", "WAV")
print("Le fichier 'resultat.wav' a été créé.")
ipd.display(Audio(son_total.values, rate=son_total.sampling_frequency))


segments = [
    (111.84, 112.03),
    (231.85, 232.05),
    (224.37, 224.57),
    (156.37, 156.55),
]

extracted = []

for start, end in segments:
    segment = sound.extract_part(from_time=start, to_time=end, preserve_times=False)
    extracted.append(segment.values)

concatenated = np.hstack(extracted)
new_sound = parselmouth.Sound(values=concatenated, sampling_frequency=sound.sampling_frequency)
