
# TP Data Science - Python

## Lancer le code
Pour lancer l'analyse, il faut lancer le fichier python de cette manière : 
>classify_pages.py --images-list path/to/file.csv

## Analyse du code Python
### Sizing des images
Pour analyser les images, nous avons du les transformer.
Les images font dorénavant toutes la même taille et sont grisées.

### Split des données
Au sein de cette analyse, nous avons divisé notre dataset en Train/Test/Valid sets. 

Train | Test | Valid
--- | --- | ---
60% | 20% | 20%

### Limiter le training
Si le calcul est long, il est possible de limiter les données traitées temporairement. Pour ca ajouter :
>    --limit-sample


## Algorithme
J'ai choisi d'éxecuter une regression logistique.
### Résultat :
0.858547241944


 type | precision |   recall  | f1-score |  support
--- | --- | --- | --- | ---
calendrier  |     0.69  |    0.60   |   0.65     |  124
miniature  |     0.14  |    0.14 |     0.14   |      7
miniature + texte   |    0.71  |    0.49     | 0.58     |   76
pageblanche    |   0.63  |    0.50   |   0.56   |     76
reliure  |     0.63    |  0.65  |    0.64   |     49
texte  |     0.90  |    0.95    |  0.93   |   1447
texte + miniature   |    0.47   |   0.15    |  0.23    |    52


      avg / total       0.84      0.86      0.85      1831



Si j'avais le temps, j'aurai essayer de faire tourner un algorithme SVM.
