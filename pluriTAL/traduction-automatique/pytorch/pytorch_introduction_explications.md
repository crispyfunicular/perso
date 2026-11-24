# TP — Introduction à PyTorch : explications

Notes explicatives du notebook [pytorch_introduction.ipynb](pytorch_introduction.ipynb), adapté du chapitre 0 de [learnpytorch.io](https://www.learnpytorch.io/00_pytorch_fundamentals/).

## En résumé

Ce TP n'entraîne aucun modèle. Il présente le **tenseur**, la structure de données sur laquelle reposent tous les réseaux de neurones, et les opérations de base pour le manipuler. Un réseau de neurones n'est au fond qu'une longue suite d'opérations sur des tenseurs.

Le notebook suit six étapes :

1. [Qu'est-ce qu'un tenseur ?](#1-quest-ce-quun-tenseur--cellules-3-à-12)
2. [Créer des tenseurs](#2-créer-des-tenseurs-cellules-13-à-21)
3. [Type de données et périphérique](#3-type-de-données-et-périphérique-cellules-22-à-26)
4. [Opérations sur les tenseurs](#4-opérations-sur-les-tenseurs-cellules-27-à-38)
5. [Changer la forme d'un tenseur](#5-changer-la-forme-dun-tenseur-cellules-39-à-45)
6. [Indexation, NumPy et GPU](#6-indexation-numpy-et-gpu-cellules-46-à-57)

Viennent ensuite le [lien avec la traduction automatique](#lien-avec-la-traduction-automatique) et des [remarques sur l'état actuel du notebook](#remarques-sur-létat-actuel-du-notebook).

---

## 1. Qu'est-ce qu'un tenseur ? (cellules 3 à 12)

Un tenseur est un tableau de nombres qui peut avoir n'importe quel nombre de dimensions.

| Nom | Exemple | `ndim` | `shape` |
|---|---|---|---|
| Scalaire | `torch.tensor(7)` | 0 | `[]` |
| Vecteur | `torch.tensor([1, 2, 3])` | 1 | `[3]` |
| Matrice | `torch.tensor([[1, 2], [3, 4]])` | 2 | `[2, 2]` |
| Tenseur | `torch.tensor([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])` | 3 | `[2, 2, 3]` |

Deux attributs servent en permanence :

- `.shape` donne la taille de chaque dimension ;
- `.ndim` donne le nombre de dimensions, c'est-à-dire le nombre de crochets ouvrants au début du tenseur.

`.item()` convertit un tenseur à un seul élément en nombre Python : `torch.tensor(7).item()` renvoie `7`.

### Lire une forme

Les dimensions se lisent **de l'extérieur vers l'intérieur**. La forme `[2, 2, 3]` signifie :

```
[                       ← dimension 0 : 2 blocs
  [ [1, 2, 3],          ← dimension 1 : 2 lignes par bloc
    [4, 5, 6] ],        ← dimension 2 : 3 valeurs par ligne
  [ [7, 8, 9],
    [10, 11, 12] ]
]
```

---

## 2. Créer des tenseurs (cellules 13 à 21)

En pratique, on écrit rarement des tenseurs à la main. On utilise des fonctions de création :

| Fonction | Résultat | Utilité en apprentissage profond |
|---|---|---|
| `torch.rand(3, 4)` | valeurs aléatoires entre 0 et 1 | les **poids d'un modèle** sont aléatoires au départ, puis ajustés pendant l'apprentissage |
| `torch.zeros(3, 3)` / `torch.ones(3, 3)` | tenseur rempli de 0 ou de 1 | **masquage** : indiquer au modèle quelles positions ignorer |
| `torch.arange(0, 10, 1)` | `[0, 1, …, 9]` | créer une suite de valeurs (fin exclue, comme `range` en Python) |
| `torch.zeros_like(t)` / `torch.ones_like(t)` | 0 ou 1 avec la **même forme** que `t` | créer un masque adapté à un tenseur existant |

Remarques :

- `torch.rand(size=(224, 224, 3))` a la forme d'une image de 224 × 224 pixels avec 3 canaux de couleur (rouge, vert, bleu).
- `torch.range(0, 10)` est **obsolète**. Il inclut la borne de fin (`0` à `10`), contrairement à `range` en Python. Utilise `torch.arange`.

---

## 3. Type de données et périphérique (cellules 22 à 26)

Chaque tenseur possède trois propriétés à surveiller :

```python
t = torch.tensor([3.0, 6.0, 9.0])
t.shape   # torch.Size([3])
t.dtype   # torch.float32
t.device  # cpu
```

### Le type (`dtype`)

| Type | Autre nom | Précision |
|---|---|---|
| `torch.float16` | `torch.half` | 16 bits : plus rapide, moins précis |
| `torch.float32` | `torch.float` | 32 bits : **type par défaut** |
| `torch.float64` | `torch.double` | 64 bits : plus précis, plus lent |
| `torch.int8`, `int16`, `int32`, `int64` | | entiers |

Plus la précision est faible, plus les calculs sont rapides, au prix d'une précision moindre. On choisit le type avec le paramètre `dtype` :

```python
torch.tensor([3.0, 6.0, 9.0], dtype=torch.float16)
```

### Le périphérique (`device`)

Un tenseur se trouve soit en mémoire sur le **CPU** (par défaut), soit sur le **GPU** (`cuda` pour les cartes Nvidia).

### Les trois erreurs classiques de PyTorch

1. **Formes incompatibles** : par exemple, une multiplication matricielle impossible (voir la section 4).
2. **Types différents** : un tenseur en `float32` et l'autre en `float16`.
3. **Périphériques différents** : un tenseur sur le CPU et l'autre sur le GPU.

---

## 4. Opérations sur les tenseurs (cellules 27 à 38)

Toute l'architecture d'un réseau de neurones se construit avec quelques opérations de base : addition, soustraction, multiplication, division et **multiplication matricielle**.

### Opérations élément par élément

L'opération s'applique à chaque valeur du tenseur :

```python
tensor = torch.tensor([1, 2, 3])
tensor + 10   # tensor([11, 12, 13])
tensor * 2    # tensor([2, 4, 6])
tensor / 3    # tensor([0.3333, 0.6667, 1.0000])
```

### Multiplication matricielle

Elle s'écrit `torch.matmul(A, B)` ou `A @ B`. Elle est différente de `A * B`, qui multiplie élément par élément.

```python
A = torch.tensor([[1, 2], [3, 4]])
B = torch.tensor([[5, 6], [7, 8]])
torch.matmul(A, B)
# tensor([[19, 22],      19 = 1×5 + 2×7
#         [43, 50]])     22 = 1×6 + 2×8 ...
```

**Les deux règles à retenir :**

1. **Les dimensions intérieures doivent être égales.**

   | Opération | Résultat |
   |---|---|
   | `(3, 2) @ (3, 2)` | ❌ erreur, car 2 ≠ 3 |
   | `(2, 3) @ (3, 2)` | ✅ |
   | `(3, 2) @ (2, 3)` | ✅ |

2. **Le résultat prend les dimensions extérieures** : `(3, 2) @ (2, 3)` donne `(3, 3)`.

### Corriger une erreur de forme : la transposition

Quand les formes ne correspondent pas, on peut souvent **transposer** l'un des tenseurs, c'est-à-dire échanger ses lignes et ses colonnes, avec `.T` ou `.transpose(0, 1)` :

```python
tensor_A.shape                       # (3, 2)
tensor_B.shape                       # (3, 2)
torch.matmul(tensor_A, tensor_B)     # ❌ (3, 2) @ (3, 2)
torch.matmul(tensor_A, tensor_B.T)   # ✅ (3, 2) @ (2, 3) → (3, 3)
```

### Le lien avec les réseaux de neurones : `nn.Linear`

Une couche linéaire (aussi appelée couche entièrement connectée) réalise exactement cette opération :

$$ y = x \cdot A^T + b $$

- **x** est l'entrée de la couche ;
- **A** est la matrice des poids, aléatoire au départ puis ajustée pendant l'apprentissage. On la note souvent **W** ;
- **b** est le biais, un décalage ajouté au résultat ;
- **y** est la sortie.

```python
torch.manual_seed(42)              # pour obtenir les mêmes poids aléatoires à chaque exécution
linear = torch.nn.Linear(in_features=2, out_features=6)
output = linear(tensor_A)          # tensor_A : (3, 2)
output.shape                       # (3, 6)
```

`in_features` doit être égal à la dernière dimension de l'entrée, et `out_features` fixe la dernière dimension de la sortie. Les poids sont stockés avec la forme `(6, 2)`, et le calcul effectué est `(3, 2) @ (2, 6) → (3, 6)`.

### Agrégations

```python
x = torch.arange(0, 100, 10)        # tensor([0, 10, 20, ..., 90]), type int64
x.min(), x.max(), x.sum()           # 0, 90, 450
x.mean()                            # ❌ erreur : mean() exige un type flottant
x.type(torch.float32).mean()        # ✅ 45.0
```

---

## 5. Changer la forme d'un tenseur (cellules 39 à 45)

Ces méthodes servent à faire correspondre les formes avant une opération.

### D'où vient le tenseur de 7 éléments ?

Les exemples de cette section partent de :

```python
x = torch.arange(1., 8.)
# tensor([1., 2., 3., 4., 5., 6., 7.])
```

`arange` va de 1 jusqu'à 8 **exclu**, ce qui donne les valeurs de 1 à 7, soit **7 éléments**. La forme est donc `[7]`. Ce tenseur n'a aucun lien avec celui de forme `[2, 2, 3]` de la section 1.

### Le nombre d'éléments est le produit des dimensions

Le nombre total d'éléments d'un tenseur ne s'obtient pas en additionnant ses dimensions mais en les **multipliant** :

| Forme | Nombre d'éléments |
|---|---|
| `[7]` | 7 |
| `[1, 7]` | 1 × 7 = 7 |
| `[2, 2, 3]` | 2 × 2 × 3 = **12** (et non 2 + 2 + 3) |
| `[224, 224, 3]` | 224 × 224 × 3 = 150 528 |

`reshape` doit **conserver ce nombre d'éléments** :

```python
x.reshape(1, 7)   # ✅ 1 × 7 = 7
x.reshape(7, 1)   # ✅ 7 × 1 = 7
x.reshape(2, 4)   # ❌ erreur : 2 × 4 = 8 ≠ 7
```

Le nombre d'éléments s'obtient avec `x.numel()`.

### Les méthodes

| Méthode | Rôle | Exemple (avec `x = torch.arange(1., 8.)`, forme `[7]`) |
|---|---|---|
| `reshape` | change la forme sans changer les valeurs | `x.reshape(1, 7)` → `[1, 7]` |
| `stack` | empile plusieurs tenseurs selon une nouvelle dimension | `torch.stack([x, x, x, x], dim=0)` → `[4, 7]` ; avec `dim=1` → `[7, 4]` |
| `squeeze` | retire les dimensions de taille 1 | `[1, 7]` → `[7]` |
| `unsqueeze` | ajoute une dimension de taille 1 | `x.unsqueeze(dim=0)` → `[1, 7]` |
| `permute` | réordonne les axes | `(224, 224, 3).permute(2, 0, 1)` → `(3, 224, 224)` |

Usages courants :

- `unsqueeze(0)` ajoute une **dimension de lot** (batch) quand on veut passer un seul exemple à un modèle qui attend un lot ;
- `permute` sert notamment à mettre une image au format attendu par PyTorch, avec les canaux en premier : `(C, H, W)`.

---

## 6. Indexation, NumPy et GPU (cellules 46 à 57)

### Indexation

Elle fonctionne comme pour les listes Python et les tableaux NumPy, de la dimension extérieure vers la dimension intérieure :

```python
x = torch.arange(1, 10).reshape(1, 3, 3)
# tensor([[[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]])

x[0]          # la matrice 3×3
x[0][0]       # tensor([1, 2, 3])
x[0][0][0]    # tensor(1)

x[:, 0]       # tensor([[1, 2, 3]])   → première ligne
x[:, :, 1]    # tensor([[2, 5, 8]])   → deuxième colonne
x[:, 1, 1]    # tensor([5])           → élément central
x[0, 0, :]    # tensor([1, 2, 3])     → identique à x[0][0]
```

`:` signifie « toutes les valeurs de cette dimension ».

### Conversion NumPy ↔ PyTorch

```python
torch_tensor = torch.from_numpy(np_array)   # NumPy → PyTorch
np_array     = torch_tensor.numpy()         # PyTorch → NumPy
```

Attention : ces deux conversions **partagent la mémoire**. Modifier l'un modifie aussi l'autre.

### Utiliser le GPU

On écrit un code qui fonctionne qu'un GPU soit présent ou non :

```python
device = "cuda" if torch.cuda.is_available() else "cpu"

tensor_on_gpu = tensor.to(device)              # envoie le tenseur sur le GPU (s'il existe)
back_to_numpy = tensor_on_gpu.cpu().numpy()    # retour sur le CPU obligatoire avant .numpy()
```

NumPy ne fonctionne que sur le CPU. `tensor_on_gpu.numpy()` provoque donc une erreur si le tenseur est sur le GPU.

---

## Lien avec la traduction automatique

Tous les modèles de traduction neuronale, y compris les Transformers, reposent sur ces opérations :

| Notion du TP | Usage dans un modèle de traduction |
|---|---|
| Tenseur 3D | un lot de phrases : `(batch, longueur_phrase, dim_embedding)`, par exemple `(32, 20, 512)` |
| `zeros` / `ones` | **masque de padding** : on complète les phrases courtes pour qu'elles aient toutes la même longueur, et le masque indique au modèle d'ignorer ces positions |
| `matmul` et transposition | **attention** : scores = `Q @ Kᵀ`, soit `(batch, len, d) @ (batch, d, len)` → `(batch, len, len)` |
| `nn.Linear` | projections Q, K et V, couches feed-forward, couche de sortie qui prédit le mot suivant |
| `unsqueeze`, `permute`, `reshape` | adapter les formes, notamment pour l'attention multi-têtes |
| `.to(device)` | entraîner le modèle sur GPU |

La plupart des bugs rencontrés en pratique sont des erreurs de forme, de type ou de périphérique. D'où l'importance de vérifier régulièrement `.shape`, `.dtype` et `.device`.

---

## Remarques sur l'état actuel du notebook

### Cellules 32 et 34 : la démonstration ne fonctionne plus

Dans le tutoriel d'origine :

- la cellule 32 doit **échouer**, car elle calcule `(3, 2) @ (3, 2)` ;
- la cellule 34 montre la **correction** avec `tensor_B.T`.

Or la cellule 32 contient maintenant `tensor_B = tensor_B.transpose(1, 0)`, ce qui a deux conséquences :

1. `tensor_B` passe en `(2, 3)` et la cellule 32 **réussit** ;
2. la cellule 34 le transpose une **seconde fois** avec `.T`, il revient en `(3, 2)` et on obtient l'erreur :
   ```
   mm: mat1 and mat2 shapes cannot be multiplied (3x2 and 3x2)
   ```
   Le message « inner dimensions match » qu'elle affiche est donc faux.

**Correction possible :** retirer la ligne `tensor_B = tensor_B.transpose(1, 0)` de la cellule 32 pour retrouver le déroulé prévu (erreur, puis correction), ou utiliser `tensor_B` sans `.T` dans la cellule 34.

### Cellules 36 à 57 : pas encore exécutées

Elles n'ont aucune sortie. L'exécution s'est sans doute arrêtée sur l'erreur de la cellule 34.

### Cellule 26 : type demandé

La cellule 25 annonce la création d'un tenseur en `float16`, mais la cellule 26 crée un `float32` avec `torch.rand(3, 2, 4)`. Si l'exercice demande du `float16`, il faut ajouter `dtype=torch.float16`.

### Cellule 19 : commentaire et code collés

Sur la première ligne, du code est collé à la fin du commentaire (`...deprecatedzero_to_ten = ...`). C'est sans conséquence, car `zero_to_ten` est redéfini juste après.
