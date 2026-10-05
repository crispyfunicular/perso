from pathlib import Path


print("DEMOCRATIE_ET_CITOYENNETE")
print("--------------------------------")
corpus_file = Path("GDNcats/DEMOCRATIE_ET_CITOYENNETE.txt")
if corpus_file.exists():
    with open(corpus_file, "r", encoding="utf-8") as f:
        s = f.read()
else:
    s = "Charles de Gaulle n'était pas anticapitaliste"

from nltk.tokenize import word_tokenize 
print('NLTK:','|'.join([t for t in word_tokenize(s)]))

import spacy
nlp = spacy.load("fr_core_news_sm")
doc = nlp(s)
print('Spacy:','|'.join([str(t) for t in doc]))

import stanza
nlp = stanza.Pipeline(lang='fr', processors='tokenize', logging_level='ERROR')
doc = nlp(s)
print('Stanza:','|'.join([t.text for t in doc.sentences[0].tokens]))

from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained("google-bert/bert-base-multilingual-cased")
print('BERT:','|'.join([t.replace('#','') for t in tokenizer.tokenize(s)]))

import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")
print('GPT:','|'.join([enc.decode([t]) for t in enc.encode(s)]))


print("LA_FISCALITE_ET_LES_FINANCES_PUBLIQUES")
print("--------------------------------")
corpus_file = Path("GDNcats/LA_FISCALITE_ET_LES_FINANCES_PUBLIQUES.txt")
if corpus_file.exists():
    with open(corpus_file, "r", encoding="utf-8") as f:
        s = f.read()
else:
    s = "Charles de Gaulle n'était pas anticapitaliste"

from nltk.tokenize import word_tokenize 
print('NLTK:','|'.join([t for t in word_tokenize(s)]))

import spacy
nlp = spacy.load("fr_core_news_sm")
doc = nlp(s)
print('Spacy:','|'.join([str(t) for t in doc]))

import stanza
nlp = stanza.Pipeline(lang='fr', processors='tokenize', logging_level='ERROR')
doc = nlp(s)
print('Stanza:','|'.join([t.text for t in doc.sentences[0].tokens]))

from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained("google-bert/bert-base-multilingual-cased")
print('BERT:','|'.join([t.replace('#','') for t in tokenizer.tokenize(s)]))

import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")
print('GPT:','|'.join([enc.decode([t]) for t in enc.encode(s)]))


print("LA_TRANSITION_ECOLOGIQUE")
print("--------------------------------")
corpus_file = Path("GDNcats/LA_TRANSITION_ECOLOGIQUE.txt")
if corpus_file.exists():
    with open(corpus_file, "r", encoding="utf-8") as f:
        s = f.read()
else:
    s = "Charles de Gaulle n'était pas anticapitaliste"

from nltk.tokenize import word_tokenize 
print('NLTK:','|'.join([t for t in word_tokenize(s)]))

import spacy
nlp = spacy.load("fr_core_news_sm")
doc = nlp(s)
print('Spacy:','|'.join([str(t) for t in doc]))

import stanza
nlp = stanza.Pipeline(lang='fr', processors='tokenize', logging_level='ERROR')
doc = nlp(s)
print('Stanza:','|'.join([t.text for t in doc.sentences[0].tokens]))

from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained("google-bert/bert-base-multilingual-cased")
print('BERT:','|'.join([t.replace('#','') for t in tokenizer.tokenize(s)]))

import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")
print('GPT:','|'.join([enc.decode([t]) for t in enc.encode(s)]))



print("ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS")
print("--------------------------------")
corpus_file = Path("GDNcats/ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS.txt")
if corpus_file.exists():
    with open(corpus_file, "r", encoding="utf-8") as f:
        s = f.read()
else:
    s = "Charles de Gaulle n'était pas anticapitaliste"

from nltk.tokenize import word_tokenize 
print('NLTK:','|'.join([t for t in word_tokenize(s)]))

import spacy
nlp = spacy.load("fr_core_news_sm")
doc = nlp(s)
print('Spacy:','|'.join([str(t) for t in doc]))

import stanza
nlp = stanza.Pipeline(lang='fr', processors='tokenize', logging_level='ERROR')
doc = nlp(s)
print('Stanza:','|'.join([t.text for t in doc.sentences[0].tokens]))

from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained("google-bert/bert-base-multilingual-cased")
print('BERT:','|'.join([t.replace('#','') for t in tokenizer.tokenize(s)]))

import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")
print('GPT:','|'.join([enc.decode([t]) for t in enc.encode(s)]))

