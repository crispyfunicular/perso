"""
Docstring pour exercice_1

- fréquence = logatomes.wav est mono et sa fréquence d’échantillonnage est :
            Fs= 44 100 Hz (donc 44 100 échantillons par seconde)

- la conversion en indices = temps x fréquence donc : 
ex : 
     n = 111.84 x 44100 = 4 932 144

     
- la boucle : 

- channel : contient des amplitudes : x[0], x[1] ...
- à chaque pas on teste deux échantillons consécutifs : x[i] et x[i+1] 
            critère "intersection montante avec 0" : x[i]<0 et x[i+1]≥0
            dès que c'est vrai : new_start = i + 1

"""





start, end = 111.44, 112.03 # on va reconvertir deux segments
channel = sound.values[0] # x[n], amplitudes
fs = sound.sampling_frequency  # fréquence d'échantillonnage du fichier (à lire dans sound)

# Bornes en indices (sécurisées pour pouvoir lire x[k+1])
start_idx = max(0, int(start * fs))
end_idx   = min(len(channel) - 2, int(end * fs))

new_start_time = start  # repli : si rien n'est trouvé, on garde le start brut

for k in range(start_idx, end_idx + 1):
    if channel[k] < 0 <= channel[k + 1]:          # intersection montante avec 0
        new_start_time = (k + 1) / fs
        break

print(channel[start_idx:end_idx])
print(new_start_time)