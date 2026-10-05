"""
Consignes :
Implémentez un segmenteur simple qui sépare les tokens selon les espaces et les ponctuations.
Réalisez des segmentations d’un extrait du corpus avec :
    • votre segmenteur
    • NLTK
    • spacy
    • stanza
    • BERT
Comparez le nombre de tokens et la liste des tokens.
"""

import re
from pathlib import Path
import nltk
from nltk.tokenize import word_tokenize
import spacy
import stanza
from transformers import AutoTokenizer

# Téléchargement ponctuel des ressources NLTK et Stanza
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
stanza.download("fr", verbose=False)

# 1. Chargement d'un extrait du corpus
corpus_file = Path("GDNcats/DEMOCRATIE_ET_CITOYENNETE.txt")

if corpus_file.exists():
    with open(corpus_file, "r", encoding="utf-8") as f:
        # Prise des 500 premiers caractères non vides pour l'exemple
        sample_text = f.read(500).strip()
else:
    # Texte de repli représentatif du corpus si le fichier n'est pas trouvé
    sample_text = (
        "Qu'est-ce qui pourrait permettre d'améliorer la participation citoyenne ? "
        "Il faudrait, par exemple, un référendum d'initiative citoyenne (RIC)."
    )

print(f"--- Extrait analysé ---\n{sample_text}\n{'=' * 50}")

# 2. Implémentation des segmenteurs

# A. Segmenteur maison (regex : mots ou ponctuations individuelles)
def custom_tokenizer(text: str) -> list[str]:
    # Capture soit une suite de caractères alphanumériques (avec accents), soit un caractère de ponctuation
    pattern = r"\w+|[^\w\s]"
    return re.findall(pattern, text, flags=re.UNICODE)

tokens_custom = custom_tokenizer(sample_text)

# B. NLTK
tokens_nltk = word_tokenize(sample_text, language="french")

# C. spaCy
nlp_spacy = spacy.load("fr_core_news_sm")
doc_spacy = nlp_spacy(sample_text)
tokens_spacy = [token.text for token in doc_spacy]

# D. Stanza
nlp_stanza = stanza.Pipeline("fr", processors="tokenize", verbose=False)
doc_stanza = nlp_stanza(sample_text)
tokens_stanza = [token.text for sentence in doc_stanza.sentences for token in sentence.tokens]

# E. BERT (CamemBERT, modèle de référence pour le français)
tokenizer_bert = AutoTokenizer.from_pretrained("camembert-base")
# Tokenisation brute en sous-mots (WordPiece / SentencePiece)
tokens_bert = tokenizer_bert.tokenize(sample_text)


# 3. Comparaison et affichage

results = {
    "Segmenteur perso (regex)": tokens_custom,
    "NLTK (word_tokenize)": tokens_nltk,
    "spaCy (fr_core_news_sm)": tokens_spacy,
    "Stanza (fr)": tokens_stanza,
    "BERT (CamemBERT - subwords)": tokens_bert,
}

print(f"\n{'Méthode':<30} | {'Nombre de tokens':<18}")
print("-" * 52)
for name, tokens in results.items():
    print(f"{name:<30} | {len(tokens):<18}")
print("=" * 52)

# Affichage des 25 premiers tokens de chaque approche
print("\n--- Comparaison des 25 premiers tokens ---\n")
for name, tokens in results.items():
    print(f"[{name}] ({len(tokens)} total)")
    print(tokens[:25])
    print("-" * 40)
