#######################################################################################################
# groupe LDDBI L1
# Lucas AUCLAIR 22102239 Responsable GitHub
# Camille LE CORRE 22101284 Responsable Mise en Forme
# Nikita Vershynin 22101104


https://github.com/uvsq22102239/projet_proie_predateur
#######################################################################################################
# Présentation succincte du projet:


## Ce projet a été développé dans le cadre de l'UE LSIN200N en L1 à l'UVSQ.


### Projet d'Informatique destiné à la création d'un système simulant la cohabitation de deux populations différentes : des proies et des prédateurs. Cet ensemble de populations sera nommé comme étant l'ensemble des animaux pour des raisons pragmatiques. Le projet fonctionne par "tours", à chaque tour de la simulation les animaux vieillissent et perdent de l'énergie. Ces notions seront discutées et précisées dans ce fichier.

### Ce projet utilise Tkinter comme interface graphique et ne comporte pas de classes d'objet (cela étant interdit dans les consignes de celui-ci).

### Il est possible de mettre en pause et de sauvegarder cette simulation afin de la charger et de la relancer ultérieurement.


#######################################################################################################
# Notions liés au fonctionnement du projet, essentielles à la compréhension de celui-ci:


## Dans ce projet chaque case de la grille est associée à un tuple qui définit la nature de la case ainsi que ses paramètres associés. Ce tuple caractérisant l'identité des individus est défini selon trois indices principaux:

### Le premier indice correspond à la nature de la case (son identifiant) : 0 pour une case dite du "décor" ou de "l'environnement" (comme une prairie par exemple), 1 pour une case définissant une proie (possiblement un lapin) et 2 pour une case définissant un prédateur (possiblement un renard). Lorsqu'une proie et un prédateur sont sur la même case, cette indice passe à 3 avant de redevenir 2, ce qui indique que la proie a bien été mangée.

### Le deuxième indice correspond à l'âge et donc au temps de vie qu'il reste aux animaux de la simulation. Celui-ci est donc soit l'âge des proies, soit celui des prédateurs (cf. premier indice).

### Le troisième indice n'est appliqué qu'aux prédateurs. En effet, celui-ci définit l'énergie des prédateurs. Cette notion d'énergie définit la notion de satiété des prédateurs et donc caractérise leur mort par famine si l'environnement devient limité en proies. Cette énergie diminue d'une unité par tour et augmente à chaque fois qu'un prédateur mange une proie. On appelle l'énergie apportée à un prédateur par une proie : MIAM. De plus, cette énergie définit si les prédateurs peuvent se reproduire ou non. Effectivement, les prédateurs ne peuvent se reproduire que si leur énergie est supérieure ou égale à un certain seuil énergétique.

#######################################################################################################
# Notions liées au déplacements des animaux:

### Les proies et les prédateurs se déplacent aléatoirement dans les 8 directions sur la grille de la simulation (pour ceux se situant au milieu de la grille). Les proies ne peuvent pas aller sur une case déjà occupée par une autre proie. Ce faisant si toutes les cases entourant une proie sont occupées, celle-ci ne peut pas se déplacer et reste donc fixe. Un cas typique de cette situation est si il y a une surpopulation des proies. Il en est de même pour les prédateurs

### Cependant, une proie et un prédateur peuvent se retrouver sur la même case. Dans ce cas-ci, le prédateur mange la proie.

#######################################################################################################
# Notions liées à l'apparition et à la reproduction des animaux sur la grille:

### Au début de la simulation des proies et des prédateurs apparaissent aléatoirement sur la grille.

### Lorsque plusieurs individus de la même classe (proie ou prédateur) sont côte-à-côte sur la grille, un nouvel individu apparaît à proximité de ceux-ci (il faut aussi qu'une case soit libre pour la naissance du nouvel animal). Il s'agit de la reproduction et de la naissance d'un nouvel individu. Néanmoins, on rappelle qu'un prédateur doit avoir une certaine quantité d'énergie bien définie afin de se reproduire (cf. notions d'énergie) : ce n'est pas le cas pour les proies.

#######################################################################################################
# Notions liées à l'interface tkinter:

### La couleur verte représente le décor de la simulation, la couleur orange représente les prédateurs (les renards) et la couleur beige représente les proies (les lapins).

### Le bouton "Sauvegarder" enregistre la configuration de la matrice correspondante à la simulation au format binaire avec pickle et le bouton "Charger" lit ce fichier et met à jour la configuration de la matrice par rapport à celle qui est enregistrée.

### Le bouton "Réinitialiser" réinitialise la simulation à partir de nouvelles variables aléatoires et le bouton "Fermer" ferme évidemment la fenêtre du programme.

### Quant au bouton "Démarrer/relancer la simulation", il lance le programme de la simulation et l'affiche au niveau de la grille ou alors si la simulation était en pause, celui-ci la relance.


