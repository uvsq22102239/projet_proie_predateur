##########################################################################################################
# groupe LDDBI L1
# Lucas AUCLAIR
# Camille LE CORRE
# Nikita Vershynin

# Projet informatique destiné à la création d'un système simulant la cohabitation de deux types de populations différentes : des proies et des prédateurs.

from xml.sax import parseString


https://github.com/uvsq22102239/projet_proie_predateur
##########################################################################################################

### Définition des constantes

N_PRO = 0 #nombre de proies présentes avant le début de la simulation
N_PRE = 0 #nombre de prédateurs disposés aléatoirement sur la grille au début de la simulation 
F_PRO = 0 #nombre de proies apparaissant aléatoirement à chaque tour
A_PRO = 0 #durée de vie des proies
A_PRO = 0 #durée de vie des prédateurs
E_PRE = 0 #énergie que dispose un prédateur au début de sa vie
MIAM = 0 #énergie apportée au prédateur (E_PRE) lorsqu'il mange une proie
E_REPRO = 0 #énergie nécessaire au prédateur pour qu'il puisse se reproduire

### Fonctions

def apparitionProies():
    """ Fait apparaître N_PRO proies aléatoirement sur la grille (avant le 1er tour)"""
    pass


def apparitionPredateurs():
    """ Fait apparaître N_PRE prédateurs aléatoirement sur la grille (au début du 1er tour)"""
    pass


def naissanceAleatoireProies():
    """ Fait apparaître F_PRO proies aléatoirement (à chaque début de tour)""" ## on considère cette fonction inutile, à voir si on la fait ou pas
    pass


def identiteProies():
    """ Remplit la case de la matrice par le tuple correspondant à l'identité de la proie (son âge, etc...)"""
    pass


def identitePredateurs():
    """ Remplit la case de la matrice par le tuple correspondant à l'identité du prédateur"""
    pass


def identitePrédateurs():
    """ Remplit la case de la matrice par l'identité du prédateur (son âge, etc...)"""
    pass


def ageProies():
    """ Prend en argument la matrice et diminue de 1 l'âge de toutes les proies"""
    pass


def ageEnergiePredateurs():
    """ Prend en argument la matrice et diminue de 1 l'âge et l'énergie de tous les prédateurs"""
    pass


def deplacementProies():
    """ Fait bouger toutes les proies"""
    pass


def deplacementPredateurs():
    """ Fait bouger tous les prédateurs"""
    pass


def reproductionProies():
    """ Si 2 proies sont à côté, elles se reproduisent"""
    pass


def reproductionPredateurs():
    """ Si 2 prédateurs sont à côté et que leur énergie est supérieure à l'énergie nécessaire pour la reproduction
    (E_repro), alors ils se reproduisent"""
    pass


def predation():
    """ Si une proie et un prédateur sont sur la même case, alors la proie meure et le prédateur gagne MIAM"""
    pass


def mortProies():
    """ Prend en argument une matrice, vérifie la durée de vie restante de toutes les proies, si elle est égale à 0,
    alors elle meurt donc l'identité de la case devient un tuple de 0"""
    pass


def mortPrédateurs():
    """ Prend en argument une matrice, vérifie la durée de vie restante et l'énergie E_PRE de tous les prédateurs, 
    si au moins l'une des deux est égale à 0, alors il meurt donc l'identité de la case devient un tuple de 0"""
    pass







# Création fenêtre + canevas + grille




# Création matrice 30x30