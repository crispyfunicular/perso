"""
Algorithmique et Programmation 2
Master PluriTAL — 2025-2026

Travail Pratique : Byte Pair Encoding (BPE)
"""

# BPE est un algorithme de tokenisation sous-lexicale.
# L'idée centrale : partir des caractères individuels d'un corpus,
# puis fusionner itérativement les paires de symboles les plus fréquentes
# jusqu'à atteindre la taille de vocabulaire souhaitée.
#
# On obtient ainsi un vocabulaire qui contient :
#   - les mots fréquents en entier
#   - des sous-unités pour les mots rares ou inconnus
#
# C'est l'algorithme utilisé dans GPT-2, RoBERTa, et bien d'autres modèles.

from collections import defaultdict


# =============================================================================
# Le corpus de travail
# =============================================================================
#
# Un corpus simplifié : un dictionnaire {mot: fréquence_dans_le_corpus}.
# On travaille sur des mots français contenant le digraphe -ail- pour que
# l'analyse linguistique soit intéressante.

CORPUS = {
    'faible':  4,
    'failles': 2,
    'taille':  6,
    'travail': 3,
    'email':   2,
    'bail':    1,
    'rail':    3,
    'detail':  2,
}


# =============================================================================
# Exercice 1 — Représentation du corpus  
# =============================================================================
#
# Avant de compter quoi que ce soit, on doit représenter chaque mot
# comme une séquence de symboles individuels.
#
# On ajoute un token spécial '</w>' en fin de mot pour marquer les frontières :
# sans lui, 'low' dans 'lower' et 'low' seul seraient identiques après fusion,
# ce qui ferait disparaître une information morphologique importante.
#
# Exemple :
#   'rail' → ('r', 'a', 'i', 'l', '</w>')
#
# Le vocabulaire segmenté est un dictionnaire :
#   { tuple_de_symboles : fréquence }


def preprocess(corpus):
    """
    Transforme un dictionnaire {mot: fréquence} en vocabulaire segmenté.

    Paramètres :
        corpus : dict  {str: int}  ex. {'rail': 3, 'bail': 1}

    Retourne :
        vocab  : dict  {tuple: int}  ex. {('r','a','i','l','</w>'): 3, ...}
    """
    # cas simple : un mot d'un seul caractère → ('x', '</w>')
    # cas complexe : itérer sur les caractères du mot et ajouter '</w>' à la fin

    NotImplemented


# Test 1.1
print("=" * 60)
print("Exercice 1.1 — preprocess")
print("=" * 60)
print(f"Corpus de départ: {CORPUS}")
vocab = preprocess(CORPUS)
for word_tuple, freq in vocab.items():
    print(f"  {''.join(word_tuple[:-1])!r:10} → {word_tuple}  ×{freq}")
print()


# -----------------------------------------------------------------------------

def get_pair_counts(vocab):
    """
    Compte la fréquence de chaque paire de symboles adjacents dans le vocab.
    La fréquence d'une paire est pondérée par la fréquence du mot qui la contient.

    Paramètres :
        vocab : dict  {tuple: int}  (résultat de preprocess)

    Retourne :
        counts : dict  {(symbole, symbole): int}

    Exemple :
        {('r','a'): 3, ('a','i'): 15, ('i','l'): 14, ...}

    Rappel : si 'taille' (×6) contient la paire ('a','i'),
             cette paire contribue 6 à son compteur total.
    """
    # astuce : pour chaque mot, parcourir les paires (symboles[i], symboles[i+1])
    #                et sommer leurs contributions pondérées par la fréquence du mot

    NotImplemented


# Test 1.2
print("=" * 60)
print("Exercice 1.2 — get_pair_counts")
print("=" * 60)
counts = get_pair_counts(vocab)
top5 = sorted(counts.items(), key=lambda x: -x[1])[:5]
print("  Top 5 paires :")
for pair, freq in top5:
    print(f"    {pair}  →  {freq}")
print()


# =============================================================================
# Exercice 2 — La boucle de fusion  
# =============================================================================
#
# Le cœur de BPE : à chaque étape, trouver la paire la plus fréquente,
# la fusionner en un nouveau symbole, et mettre à jour le vocabulaire.
#
# Exemple :
#   avant  : {('r','a','i','l','</w>'): 3}
#   fusion de ('a','i')
#   après  : {('r','ai','l','</w>'): 3}


def merge_vocab(pair, vocab):
    """
    Applique une fusion à tout le vocabulaire segmenté.

    Paramètres :
        pair  : tuple  (symbole_gauche, symbole_droit)  ex. ('a', 'i')
        vocab : dict   {tuple: int}

    Retourne :
        new_vocab : dict  {tuple: int}  (nouveau dict, ne pas modifier vocab en place !)

    Exemple :
        >>> merge_vocab(('a','i'), {('r','a','i','l','</w>'): 3})
        {('r','ai','l','</w>'): 3}

    Indication : parcourir chaque mot, reconstruire son tuple en remplaçant
                 chaque occurrence de (pair[0], pair[1]) par leur concaténation.
    """
    # astuce : reconstruire chaque tuple symbole par symbole,
    #                en fusionnant les paires trouvées au passage

    # Quelques variables pour commencer :

    new_vocab = {} # Le nouveau vocabulaire à renvoyer
    left, right = pair # Les deux symboles qu'on aimerait fusionner dans notre vocabulaire
    merged = left + right # Le nouveau symbole à introduire au vocabulaire


# Test 2.1
print("=" * 60)
print("Exercice 2.1 — merge_vocab")
print("=" * 60)
test_vocab = {('r','a','i','l','</w>'): 3, ('b','a','i','l','</w>'): 1}
merged = merge_vocab(('a','i'), test_vocab)
print("  Avant  :", test_vocab)
print("  Fusion de ('a','i')")
print("  Après  :", merged)
print()


# -----------------------------------------------------------------------------

def train_bpe(corpus, n_merges):
    """
    Entraîne BPE sur le corpus pendant n_merges étapes.

    Paramètres :
        corpus   : dict  {str: int}
        n_merges : int   nombre de fusions à effectuer

    Retourne :
        vocab       : dict        vocabulaire final segmenté  {tuple: int}
        merge_rules : list[tuple] liste ordonnée des fusions effectuées
                                  ex. [('a','i'), ('ai','l'), ...]

    Algorithme :
        1. Prétraiter le corpus
        2. Répéter n_merges fois :
               a. Compter les paires
               b. Trouver la paire la plus fréquente
               c. L'ajouter à merge_rules
               d. Mettre à jour le vocabulaire avec merge_vocab
        3. Retourner vocab et merge_rules
    """
    NotImplemented


# Test 2.2
print("=" * 60)
print("Exercice 2.2 — train_bpe")
print("=" * 60)
vocab_final, merge_rules = train_bpe(CORPUS, n_merges=10)
print("  10 fusions effectuées (dans l'ordre) :")
for i, rule in enumerate(merge_rules, 1):
    print(f"    {i:2}. {rule[0]} + {rule[1]}  →  {rule[0]+rule[1]}")
print()
print("  Vocabulaire final (extrait) :")
for word_tuple, freq in list(vocab_final.items())[:5]:
    print(f"    {word_tuple}  ×{freq}")
print()


# =============================================================================
# Exercice 3 — Tokénisation et analyse  
# =============================================================================
#
# Une fois les règles apprises, on peut tokéniser un mot inconnu :
# on lui applique les règles dans leur ordre d'apprentissage.
#
# C'est crucial : une règle de l'étape k ne peut utiliser que des symboles
# existant à cette étape — d'où l'importance de respecter l'ordre.


def tokenize(word, merge_rules):
    """
    Tokénise un mot en appliquant les règles de fusion dans l'ordre.

    Paramètres :
        word        : str        le mot à tokéniser
        merge_rules : list[tuple] liste ordonnée des fusions (résultat de train_bpe)

    Retourne :
        tokens : list[str]  ex. ['de', 'tail', '</w>']

    Indication :
        1. Convertir word en tuple de caractères + '</w>'
        2. Appliquer merge_vocab pour chaque règle, une par une
        3. Retourner la liste des symboles restants
    """
    # cas simple : word est vide → retourner ['</w>']
    # cas complexe : appliquer chaque règle de fusion dans l'ordre

    NotImplemented


# Test 3.1
print("=" * 60)
print("Exercice 3.1 — tokenize")
print("=" * 60)
mots_test_31 = ['faible', 'taille', 'rail']   # dans le corpus d'entraînement
for mot in mots_test_31:
    tokens = tokenize(mot, merge_rules)
    print(f"  {mot!r:12} → {tokens}")
print()


# -----------------------------------------------------------------------------
# Analyse linguistique — Question 3.2
# -----------------------------------------------------------------------------
#
# Appliquez votre tokéniseur sur ces mots ABSENTS du corpus d'entraînement.

mots_test_32 = ['ail', 'portail', 'maillot', 'braille', 'aille']

print("=" * 60)
print("Exercice 3.2 — analyse linguistique")
print("=" * 60)
for mot in mots_test_32:
    tokens = tokenize(mot, merge_rules)
    print(f"  {mot!r:12} → {tokens}")
print()

# Voici quelques questions à considérer :
#
# Q1. Les frontières de tokens correspondent-elles à des frontières morphémiques ?
#
# Q2. Identifiez un cas où BPE produit une segmentation morphologiquement pertinente,
#     et un cas où elle ne l'est pas.
#
# Q3. Que se passerait-il si le corpus d'entraînement était 100× plus grand ?
#     Et 10× plus petit ?
