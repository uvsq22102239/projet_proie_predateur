#######################################################################################################
# groupe LDDBI L1
# Lucas AUCLAIR 22102239
# Camille LE CORRE 22101284
# Nikita Vershynin 22101104


https://github.com/uvsq22102239/projet_proie_predateur
#######################################################################################################
# Présentation succinte du projet:


## Ce projet a été développé dans le cadre de l'UE LSIN200N en L1 à l'UVSQ.


### Projet d'Informatique destiné à la création d'un système simulant la cohabitation de deux types de populations différentes : des proies et des prédateurs. Cette ensemble de population sera nommé comme étant l'ensemble des animaux pour des raisons pragmatiques. Le projet fonctionne par "tours", à chaque tour de la simulation les animaux vieillissent et perdent de l'énergie. Ces notions seront discutées et précisées dans ce fichier.

#######################################################################################################
# Notions liés au fonctionnement du projet essentielles à la compréhension de celui-ci:


## Dans ce projet chaque case de la grille est associée à un tuple qui définit la nature de la case ainsi que ses paramètres associés. Ce tuple est définit selon trois indices principaux:

## Le premier indice correspond à la nature de la case, 0 pour une case dite du "décor" ou de "l'environnement", 1 pour une case définissant une proie (possiblement un lapin) et 2 pour une case définissant un prédateur (possiblement un renard).

## Le deuxième indice correspond à l'âge et donc au temps de vie qu'il reste aux animaux de la simulation. Celui-ci est donc soit l'âge des individus étants des proies soit celui des individus étant des prédateurs (cf. premier indice).

## Le troisième indice quant à lui est particulier et ne définit qu'un certain type d'individu de la simulation ; il s'agit des prédateurs. En effet, celui-ci définit l'énergie caractéristique des prédateurs. Cette notion d'énergie définit la notion de satiété des prédateurs et donc caractérise leur mort par famine si l'environnement devient limité en proies. Cette énergie diminue d'une unité par tour et augmente à chaque fois qu'un prédateur mange une proie. De plus, cette énergie définit si les prédateurs peuvent se reproduire ou non. Effectivement, les prédateurs ne peuvent se reproduire que si leur énergie est supérieure ou égale à un certain seuil énergétique.

#######################################################################################################
# Notions liées au déplacements des animaux

## Les proies se déplacent aléatoirement dans les 8 directions sur la grille de la simulation. Elles ne peuvent pas aller sur une case préalablement occupée par une autre proie. Ce faisant si toutes les cases entourant une proie sont occupées, celle-ci ne peut pas se déplacer et reste donc fixe. Un cas typique de cette situation est si il y a une surpopulation des proies.

### Les prédateurs se déplacent,eux aussi, aléatoirement dans les 8 directions et ne peuvent aller sur une case préalablement occupée par un prédateur. Néanmoins, ceux-ci peuvent aller sur la même case qu'une proie. Lorsque cela a lieu : le prédateur mange la proie.

#######################################################################################################
# Notions liées à l'apparition et à la reproduction des animaux sur la grille

## Au début de la simulation des proies apparaissent aléatoirement sur la grille, celles-ci vont se reproduire au début pendant quelques tours. Lorsque plusieurs proies sont côte-à-côte sur la grille, une nouvelle proie apparaît à proximité de celles-ci : il s'agit de la reproduction et de la naissance d'un nouvel individu.

### Après un certain nombre de tours, des prédateurs apparaissent, eux aussi, aléatoirement sur la simulation. Ceux-ci vont se reproduire similairement aux proies. Néanmoins, on rappelle qu'un prédateur doit avoir une certaine quantité d'énergie bien définie afin de se reproduire. (cf. notions d'énergie)


