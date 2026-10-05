# Fouille de textes & extraction d'informations
# TP tokenisation
## Consignes
Implémentez un segmenteur simple qui sépare les tokens selon les espaces et les ponctuations.  
Réalisez des segmentations d’un extrait du corpus avec :
- votre segmenteur
- NLTK
- spacy
- stanza
- BERT  
Comparez le nombre de tokens et la liste des tokens.


| Méthode | Nombre de tokens |
| --- | ---: |
| Segmenteur perso (regex) | 104 |
| NLTK (word_tokenize) | 94 |
| spaCy (fr_core_news_sm) | 99 |
| Stanza (fr) | 95 |
| BERT (CamemBERT - subwords) | 127 |


## Regex (`re`) : 104 tokens
Approche symbolique, règles déterministes  
- Très rapide, aucune dépendance lourde, transparent et prévisible  
- Ne gère aucune règle morphologique ou syuntaxique
- Eclate systématiquement les apostrophes en deux tokens distincts
Sépare tous les symboles consécutifs (...) --> renvoie bcp de tokens (104)

```python
import re
def custom_tokenizer(text: str) -> list[str]:
    # Capture soit une suite de caractères alphanumériques (avec accents), soit un caractère de ponctuation
    pattern = r"\w+|[^\w\s]"
    return re.findall(pattern, text, flags=re.UNICODE)
```
- `\w+` regroupe les suites de caractères alphanumériques
- `[^\w\s]` isole chaque caractère de ponctuation un par un en ignorant les blancs

```
[Segmenteur perso (regex)] (104 total)
['|', '!', 'E', 'philippe', 'doit', 'démissionner', '-', 'son', 'manque', 'd', 'écoute', 'et', 'l', 'hypochrisie', 'qu', 'il', 'démontre', 'sur', 'les', '80', 'en', 'déguisant', 'un', 'Impôt', 'injuste']
```

## NLTK (`word_tokenize`) : 94 tokens
Semi-supervisé (modèle non supervisé entraîné sur la ponctuation de phrase + règles déterministes)  
- Repose sur l'algorithme Punkt (Kiss & Strunk, 2006) qui détecte d'abord les frontières de phrases, complété par le module `TreebankWordTokenizer` adapté au français.
- Utilise des tables d'abréviations connues pour ne pas couper au mauvais endroit (M., etc.) -> regroupe mieux les ponctuations consécutives ou les contractions que la regex brutes -> renvoie moins de tokens (94)
- Léger, standard historique en TAL, très efficace sur du texte bein formé mais moins robuste face aux bruits du web, aux émoticônes ou typographies approximatives

```python
import nltk
from nltk.tokenize import word_tokenize
tokens_nltk = word_tokenize(sample_text, language="french")
```
```
[NLTK (word_tokenize)] (94 total)
['|', '!', 'E', 'philippe', 'doit', 'démissionner', '-', 'son', 'manque', 'd', 'écoute', 'et', 'l', 'hypochrisie', 'qu', 'il', 'démontre', 'sur', 'les', '80', 'en', 'déguisant', 'un', 'Impôt', 'injuste']
```

## spaCy (`fr_core_news_sm`) : 99 tokens
Machine à états finis dirigée par des règles linguistiques spécifiques à la langue (*Rule-based Tokenizer*), intégrée dans un pipeline neuronal.
- La tokenisation de spaCy n'utilise pas de réseau de neurones
- Elle applique un algorithme de segmentation à base de préfixes, suffixes, infixes et exceptions lexicales propres au français.
- Elle connaît les règles d'élision française (d', l', qu', c') et les mots composés figés -> Isole systématiquement les clitiques et apostrophes
- Très rapide (implémenté en Cython)

```python
import spacy
nlp_spacy = spacy.load("fr_core_news_sm")
doc_spacy = nlp_spacy(sample_text)
tokens_spacy = [token.text for token in doc_spacy]
```
```
[spaCy (fr_core_news_sm)] (99 total)
['|', '!', 'E', 'philippe', 'doit', 'démissionner', '-', 'son', 'manque', 'd', 'écoute', 'et', 'l', 'hypochrisie', 'qu', 'il', 'démontre', 'sur', 'les', '80', 'en', 'déguisant', 'un', 'Impôt', 'injuste']
```

## Stanza (`stanza.Pipeline("fr")`) : 95 tokens
- Modèle enuronal de bout en bout : Utilise un réseau récurrent (Bi-LSTM) au niveau caractère combiné avec un modèle d'alignement pour prédire simultanément les coupures de phrases et les frontières de tokens
- Aligné sur la norme internationale Universal Dependencies (UD)
- Capable de gérer les tokens multi-mots (au = à + le)
- Beaucoup plus lent que spaCy ou NLTK (tourne sur PyTorch)

```python
import stanza
nlp_stanza = stanza.Pipeline("fr", processors="tokenize", verbose=False)
doc_stanza = nlp_stanza(sample_text)
tokens_stanza = [token.text for sentence in doc_stanza.sentences for token in sentence.tokens]
```
```
[Stanza (fr)] (95 total)
['|!', 'E', 'philippe', 'doit', 'démissionner', '-', 'son', 'manque', 'd', 'écoute', 'et', 'l', 'hypochrisie', 'qu', 'il', 'démontre', 'sur', 'les', '80', 'en', 'déguisant', 'un', 'Impôt', 'injuste', 'avec']
```

## BERT (`AutoTokenizer`) : 127 tokens
- Tokenisation statistique en sous-mots
- Son objectif n'est pas linguistique, mais algorithmique : résoudre le problème du vocabulaire hors-dictionnaire (OOV - Out-Of-Vocabulary)
- Les mots fréquents sont conservés entiers (▁doit, ▁démissionner), tandis que les mots rares, fautes de frappe ou noms propres sont découpés en fragments statistiques : philippe = phili + ppe
- Pas de mot inconnu : n'importe quel texte peut être encodé
- Réversible (detokenisation) sans perte d'information
- C'est la méthode qui produit le plus de tokens (127) car la granularité descend sous le niveau du mot pour pallier le vocabulaire non vu et les fautes d'orthographe du corpus.

```python
from transformers import AutoTokenizer
tokenizer_bert = AutoTokenizer.from_pretrained("camembert-base")
# Tokenisation brute en sous-mots (WordPiece / SentencePiece)
tokens_bert = tokenizer_bert.tokenize(sample_text)
```
```
[BERT (CamemBERT - subwords)] (127 total)
['▁|', '!', '▁E', '▁', 'phili', 'ppe', '▁doit', '▁démissionner', '▁-', '▁son', '▁manque', '▁d', '▁écoute', '▁et', '▁l', '▁hypo', 'ch', 'ris', 'ie', '▁qu', '▁il', '▁démontre', '▁sur', '▁les', '▁80']
```

## Comparatif des méthodes de tokenisation (TAL)

| Outil / Méthode | Type d'approche | Niveau de granularité | Nombre de tokens (extrait) | Gestion des mots hors-vocabulaire (OOV) | Cas d'usage privilégié |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **Regex** | Heuristique / Règles symboliques | Caractères / Chaînes alphanumériques | 104 | Non applicable (découpage déterministe aveugle) | Scripts légers, prototypage rapide, extraction ciblée |
| **NLTK** | Hybride (non-supervisé Punkt + règles) | Mots syntaxiques | 94 | Dictionnaire de mots entiers / risque d'inconnus | Enseignement, prototypage TAL traditionnel, corpus standard |
| **spaCy** | Règles linguistiques optimisées (Cython) | Tokens morpho-syntaxiques | 99 | Dictionnaire de vocabulaire / pas de sous-mots | Pipelines industriels (NER, POS, dépendances), traitement rapide |
| **Stanza** | Réseau de neurones profond (Bi-LSTM) | Mots selon Universal Dependencies (UD) | 95 | Modélisation au niveau caractère | Analyse syntaxique rigoureuse, recherche en linguistique |
| **CamemBERT** | Statistique sous-lexicale (SentencePiece / BPE) | Sous-mots et caractères | 127 | **0 OOV** (découpe les mots rares/inconnus en fragments) | Modèles de langage Transformers, plongements contextuels, Deep Learning |