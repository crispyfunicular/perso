from pathlib import Path

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.utils import Bunch

DATA_DIR = Path("imdb_smol")
# Même valeur partout pour des runs reproductibles
RANDOM_STATE = 42

# Chargement des données
texts = []
targets = []

# label 1 = positif, label 0 = négatif
for target, dossier in [(1, "pos"), (0, "neg")]:
    # Lit tous les .txt du dossier correspondant
    for fichier in (DATA_DIR / dossier).glob("*.txt"):
        texts.append(fichier.read_text(encoding="utf-8"))  # le texte de la critique
        targets.append(target)  # la classe associée

data = Bunch(
    data=texts, #array NumPy
    target=targets, #variables cible
    target_names=["neg", "pos"], #noms des classes
)

print(len(data.data), "critiques chargées")

# Inputs X et outputs y
X_critiques, y_critiques = data.data, data.target

# Partition train / test
X_train, X_test, y_train, y_test = train_test_split(
    X_critiques,
    y_critiques,
    test_size=0.10,
    stratify=y_critiques,
    random_state=RANDOM_STATE,
)

# Vectorisation : sac de mots
vectorizer = CountVectorizer(stop_words="english")
X_train = vectorizer.fit_transform(X_train)  # données de train vectorisées
X_test = vectorizer.transform(X_test)
print(X_train.shape)


# Comparaison des classifieurs

# SVM linéaire (pas dans linear_model : dans sklearn.svm)
from sklearn.svm import LinearSVC

print("=== LinearSVC ===")
clf = LinearSVC(max_iter=5000)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=data.target_names))

# Régression logistique
from sklearn.linear_model import LogisticRegression

print("=== LogisticRegression ===")
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=data.target_names))

# Arbre de décision
from sklearn.tree import DecisionTreeClassifier

print("=== DecisionTreeClassifier ===")
clf = DecisionTreeClassifier(random_state=RANDOM_STATE)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=data.target_names))

# Forêt d'arbres
from sklearn.ensemble import RandomForestClassifier

print("=== RandomForestClassifier ===")
clf = RandomForestClassifier(random_state=RANDOM_STATE)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=data.target_names))

# Bayes naïf multinomial (adapté aux comptes de mots ; pas GaussianNB)
from sklearn.naive_bayes import MultinomialNB

print("=== MultinomialNB ===")
clf = MultinomialNB()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=data.target_names))

# K plus proches voisins
from sklearn.neighbors import KNeighborsClassifier

print("=== KNeighborsClassifier ===")
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=data.target_names))


# Optimisation des hyperparamètres
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

# Grille des hyperparamètres à tester :
# - C : force de la régularisation
#     petit C → modèle plus souple (accepte plus d'erreurs)
#     grand C → modèle plus strict (risque de surapprentissage)
# - kernel : forme de la frontière de décision
#     "linear" → droite / hyperplan. La décision dépend d'une somme pondérée des features → plus simple, plus rapide.
#     "rbf"    → frontière non linéaire. La décision dépend de la similarité entre les points → plus complexe, plus lent.
param_grid = {"C": [0.1, 1.0, 10.0], "kernel": ["rbf", "linear"]}
# GridSearchCV teste toutes les combinaisons (ici 3 × 2 = 6) :
# (C=0.1, rbf), (C=0.1, linear), (C=1.0, rbf), ...
grid = GridSearchCV(
    SVC(random_state=RANDOM_STATE),  # modèle de base
    param_grid,                      # valeurs à essayer
    cv=4,                            # validation croisée en 4 plis
    scoring="accuracy",              # score à maximiser
)
# Entraîne et compare les combos sur le train uniquement
estimator = grid.fit(X_train, y_train)

print("Meilleurs hyperparamètres :", estimator.best_params_)
print("Meilleure accuracy (CV) :", estimator.best_score_)
# Le meilleur modèle est re-testé sur le jeu de test (jamais vu pendant la grille)
y_pred = estimator.predict(X_test)
print("=== SVC (GridSearchCV) ===")
print(classification_report(y_test, y_pred, target_names=data.target_names))