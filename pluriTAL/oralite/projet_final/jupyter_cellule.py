# cellule 1
"""
Modèle phonème-to-speech — LG007, session2_mic_L
"""
import numpy as np
import pyworld as pw
import textgrids
import soundfile as sf
from collections import defaultdict
from pathlib import Path

SR    = 44100
PAS   = 0.005

# Dictionnaires globaux (agrégés sur tous les fichiers)
dico_sp, dico_ap, dico_f0, dico_dur = (
    defaultdict(list),
    defaultdict(list),
    defaultdict(list),
    defaultdict(list),
)

# Chemins fichiers audio et TextGrid
wavs = sorted(Path("audio").glob("*.wav"))
for wav_path in wavs:
    NOM = wav_path.stem          # ex: "1-1"
    signal, _ = sf.read(str(wav_path))
    tg_path = wav_path.with_suffix(".TextGrid")
    if not tg_path.exists():
        print(f"[WARN] TextGrid manquant, fichier ignoré: {tg_path}")
        continue
    tier = textgrids.TextGrid(str(tg_path))["phones"]

    # ---- Analyse WORLD ----
    signal     = signal.astype(np.float64)
    f0, t      = pw.harvest(signal, SR)
    f0         = pw.stonemask(signal, f0, t, SR)
    sp         = pw.cheaptrick(signal, f0, t, SR)
    ap         = pw.d4c(signal, f0, t, SR)

    for a in tier:
        p = a.text.strip()
        # MFA (Kaldi) utilise typiquement "sil" (silence) et "spn" (bruit/parole non analysable)
        if not p or p in {"sil", "spn"}:
            continue

        fd = int(a.xmin / PAS)
        ff = int(a.xmax / PAS)
        if ff <= fd:
            continue

        # Sécurise les slices vides (peut arriver à cause des arrondis temps→trames)
        sp_seg = sp[fd:ff]
        ap_seg = ap[fd:ff]
        f0_seg = f0[fd:ff]
        if sp_seg.shape[0] == 0:
            continue
        #sp[fd:ff] extrait les frames WORLD du phonème courant — c'est une matrice de
        # shape (n_frames, n_bins). La boucle ajoute chaque frame individuellement dans
        # la liste dico_sp[p]. À la fin on aura toutes les frames de toutes les occurrences
        # du phonème p dans la même liste.
        #Pour f0 en revanche, on ne stocke pas chaque frame mais une seule valeur par
        # occurrence : la moyenne de F0 sur le segment. C'est un choix de simplification.

        for frame in sp_seg: dico_sp[p].append(frame)
        for frame in ap_seg: dico_ap[p].append(frame)
        dico_f0[p].append(np.nanmean(f0_seg))
        dico_dur[p].append(a.xmax - a.xmin)
print(dico_sp)


# Dictionnaire final (moyennes globales par phonème)
dico = {}
for p in dico_sp:
    dico[p] = {
        "sp":  np.mean(dico_sp[p], axis=0),
        "ap":  np.mean(dico_ap[p], axis=0),
        "f0":  np.mean(dico_f0[p]),
        "dur": np.mean(dico_dur[p]),
    }

print(f"Dictionnaire : {sorted(dico.keys())}")


# cellule 2

# ---- Synthèse ----
def synthetiser(sequence):
    f0_tot, sp_tot, ap_tot = [], [], []
    for p in sequence:
        dur = dico[p]["dur"]
        f0_val = dico[p]["f0"]

        #On calcule combien de frames correspond à la durée moyenne du phonème.
        #Par exemple si dur = 0.08s et PAS = 0.005s, alors n = 16 frames.
        #Le max(1, ...) garantit qu'on a au moins 1 frame.
        n = max(1, int(dur / PAS))

        #[dico[p]["f0"]] * n crée une liste de n fois la même valeur de F0
        # .extend() ajoute ces valeurs à la liste globale.
        #extend ajoute les éléments d’une liste un par un, alors que append ajoute
        #la liste entière comme un seul bloc.
        if f0_val > 0:
          f0_tot.extend([f0_val] * n)
        else:
          f0_tot.extend([0] * n)

        sp_tot.extend([dico[p]["sp"]] * n)
        ap_tot.extend([dico[p]["ap"]] * n)

    # WORLD attend des arrays, pas des listes Python
    return pw.synthesize(np.array(f0_tot), np.array(sp_tot), np.array(ap_tot), SR)


# celulle 3
phrases = [
    "Celui qui croyait au ciel, celui qui n'y croyait pas.",
    "Tous deux adoraient la belle, prisonière des soldats.",
    "Lequel montait à l'échelle et lequel guettait en bas",
    "Quand les blés sont sous la grelle, fou qui fait le délicat.",
    "Fou qui songe à ses querelles au coeur du commun combat.",
    "L'alouette et l'hirondelle, la rose et le réséda."
]

synth = call("Create SpeechSynthesizer", "French (France)", "Steph")

for i, texte in enumerate(phrases, start=1):
    _, snd = call(synth, "To Sound", texte, "yes")
    sf.write(f"tts_{i:02d}.wav", snd.values[0], int(snd.sampling_frequency))

#phonetisation_praat = call
synthese_praat = call("Create SpeechSynthesizer", "French (France)", "Steph")


grille_synthetisee,son_synthetise = call(synthese_praat,"To Sound", texte, "yes")

# Récupérer le signal audio et le taux d'échantillonnage
signal = son_synthetise.values[0]
sr     = son_synthetise.sampling_frequency
pitch = son_synthetise.to_pitch(time_step=0.01, pitch_floor = 75, pitch_ceiling = 500)


nb_phonemes = call(grille_synthetisee, "Get number of intervals", 4)

#phonemes = [parselmouth.praat.call(grille_synthetisee, "Get label of interval", 4, i + 1) for i in range(nb_phonemes)]
#print(phonemes)

resultats = []

for i in range(1, nb_phonemes + 1):
  label = call(grille_synthetisee, "Get label of interval", 4, i)
  if label =="":
    continue
  xmin = call(grille_synthetisee, "Get start time of interval", 4, i)
  xmax = call(grille_synthetisee, "Get end time of interval", 4, i)
  dur= xmax-xmin
  milieu = (xmin+xmax)/2
  f0_val = pitch.get_value_at_time(milieu)
  if f0_val is None:
    f0_val = 0

  resultats.append({
      "phoneme": label,
      "duree": dur,
      "f0": f0_val
  })

print(resultats)


# cellule 4

sequence = []
durees = []
f0s = []

for r in resultats:
  p = r["phoneme"]
  # On garde seulement les phones qui existent dans le dico (sinon KeyError à la synthèse)
  if p not in dico:
    continue
  sequence.append(p)
  durees.append(r["duree"])
  f0s.append(r["f0"])


print(resultats)

# celulle 5
"""
Fonction
"""
def synthetiser(sequence, durees=None, f0s=None):
    f0_tot, sp_tot, ap_tot = [], [], []

    for i, p in enumerate(sequence):
        dur = (durees[i] if durees is not None else dico[p]["dur"])
        n = max(1, int(dur / PAS))

        # Ici, dico[p]["sp"] et dico[p]["ap"] sont déjà des VECTEURS moyens (1 frame),
        # pas des trajectoires temporelles : on les répète n fois.
        f0_val = (f0s[i] if f0s is not None else dico[p]["f0"])
        if np.isnan(f0_val) or f0_val <= 0:
            f0_tot.extend([0.0] * n)
        else:
            f0_tot.extend([float(f0_val)] * n)

        sp_tot.extend([dico[p]["sp"]] * n)
        ap_tot.extend([dico[p]["ap"]] * n)

    return pw.synthesize(
        np.array(f0_tot),
        np.array(sp_tot),
        np.array(ap_tot),
        SR
    )
