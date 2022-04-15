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

## Le premier indice correspond à la nature de la case, 0 pour une case dite du "décor" ou de "l'environnement", 1 pour une case définissant une proie (possiblement un lapin) et 2 pour une case définissant un prédateur (possiblment un renard).

## Le deuxième indice correspond à l'âge et donc au temps de vie qu'il reste aux animaux de la simulation. Celui-ci est donc soit l'âge des individus étants des proies soit celui des individus étant des prédateurs (cf. premier indice).

## Le troisième indice quant à lui est particulier et ne définit qu'un certain type d'individu de la simulaton ; il s'agit des prédateurs. En effet, celui-ci définit l'énergie caractéristique des prédateurs. Cette notion d'énergie définit la notion de satiété des prédateurs et donc caractérise leur mort de famine si l'environnement devient limité en proies. Cette énergie diminue d'une unité par tour et augmente de A DEFINIR unités à chaque fois qu'un prédateur mange une proie. De plus, cette énergie définit si les prédateurs peuvent se reproduire ou non. Effectivement, les prédateurs ne peuvent se reproduire que si leur énergie est supérieure ou égale à A DEFINIR.

#######################################################################################################



