##########################################################################################################
# groupe LDDBI L1
# Lucas AUCLAIR
# Camille LE CORRE
# Nikita Vershynin

# Projet informatique destiné à la création d'un système simulant la cohabitation de deux types de populations différentes : des proies et des prédateurs.


#https://github.com/uvsq22102239/projet_proie_predateur
##########################################################################################################



############################################
### Import des librairies
############################################

import tkinter as tk

import random as rd


############################################
### Définition des constantes
############################################

HAUTEUR_CANEVAS = 500
LARGEUR_CANEVAS = 500
NB_CASES = 30


N_PRO = 0 #nombre de proies présentes avant le début de la simulation
N_PRE = 0 #nombre de prédateurs disposés aléatoirement sur la grille au début de la simulation 
F_PRO = 0 #nombre de proies apparaissant aléatoirement à chaque tour
A_PRO = 0 #durée de vie des proies
A_PRE = 0 #durée de vie des prédateurs
E_PRE = 0 #énergie que dispose un prédateur au début de sa vie
MIAM = 0 #énergie apportée au prédateur (E_PRE) lorsqu'il mange une proie
E_REPRO = 0 #énergie nécessaire au prédateur pour qu'il puisse se reproduire


############################################
### Définition des fonctions
############################################




############################################
##### Fonctions en lien avec les widgets


def creationGrille(NB_CASES):
    """ Créer une grille carrée de NB_CASES cases de largeur"""

    taille_case = LARGEUR_CANEVAS / NB_CASES

    for k in range(1, (NB_CASES)):
        # lignes verticales
        canevas.create_line((k * taille_case), 0, (k * taille_case), HAUTEUR_CANEVAS)
        # lignes horizontales
        canevas.create_line(0, (k * taille_case), LARGEUR_CANEVAS, (k * taille_case))



def coordonneesCase(ligne, colonne):
    """ Définie les coordonnées d'une case de la grille """

    taille_case = LARGEUR_CANEVAS // NB_CASES
    
    x0 = colonne * taille_case
    y0 = ligne * taille_case
    x1 = (colonne + 1) * taille_case
    y1 = (ligne + 1) * taille_case

    liste_coordonnées = [x0, y0, x1, y1]

    return liste_coordonnées



def couleurCases(matrice):
    """ Colorie les cases de la grille en fonction de l'animal qui est dessus"""

    for i in range(len(matrice)):
        for j in range(len(matrice)):
            case = canevas.create_rectangle(coordonneesCase(i, j), fill="black")
            if matrice[i][j][0] == 0:
                canevas.itemconfigure(case, fill="green yellow")
            elif matrice[i][j][0] == 1:
                canevas.itemconfigure(case, fill="blanched almond")
            elif matrice[i][j][0] == 2:
                canevas.itemconfigure(case, fill="DarkOrange1")



def creationMatrice(n):
    """ Créér une matrice carrée de taille n contenant un tuple de 4 valeurs (qu'on initialise à 0)"""

    return [[(0,0,0,0)]*n for i in range(n)]



def voisinage(i, j, matrice):
    """ Créer une liste contenant le type des individus voisins d'un animal"""

    # l'ordre des voisins dans la liste est défini de gauche à droite puis de haut en bas
    l = []

    if i==0 and j==0 :
        l.append(matrice[i][j+1][0])
        l.append(matrice[i+1][j][0])
        l.append(matrice[i+1][j+1][0])
    elif i==0 and (j==len(matrice)-1):
        l.append(matrice[i][j-1][0])
        l.append(matrice[i+1][j-1][0])
        l.append(matrice[i+1][j][0])
    elif (i==len(matrice)-1) and j==0:
        l.append(matrice[i-1][j][0])
        l.append(matrice[i-1][j+1][0])
        l.append(matrice[i][j+1][0])
    elif (i==len(matrice)-1) and (j==len(matrice)-1):
        l.append(matrice[i-1][j-1][0])
        l.append(matrice[i-1][j][0])
        l.append(matrice[i][j-1][0])
    elif i==0 and 0<j<(len(matrice)-1):
        l.append(matrice[i][j-1][0])
        l.append(matrice[i][j+1][0])
        l.append(matrice[i+1][j-1][0])
        l.append(matrice[i+1][j][0])
        l.append(matrice[i+1][j+1][0])
    elif (i==len(matrice)-1) and 0<j<(len(matrice)-1):
        l.append(matrice[i-1][j-1][0])
        l.append(matrice[i-1][j][0])
        l.append(matrice[i-1][j+1][0])
        l.append(matrice[i][j-1][0])
        l.append(matrice[i][j+1][0])
    elif (0<i<(len(matrice)-1) and j==0):
        l.append(matrice[i-1][j][0])
        l.append(matrice[i-1][j+1][0])
        l.append(matrice[i][j+1][0])
        l.append(matrice[i+1][j][0])
        l.append(matrice[i+1][j+1][0])
    elif 0<i<(len(matrice)-1) and j==(len(matrice)-1):
        l.append(matrice[i-1][j-1][0])
        l.append(matrice[i-1][j][0])
        l.append(matrice[i][j-1][0])
        l.append(matrice[i+1][j-1][0])
        l.append(matrice[i+1][j][0])
    else :
        l.append(matrice[i-1][j-1][0])
        l.append(matrice[i-1][j][0])
        l.append(matrice[i-1][j+1][0])
        l.append(matrice[i][j-1][0])
        l.append(matrice[i][j+1][0])
        l.append(matrice[i+1][j-1][0])
        l.append(matrice[i+1][j][0])
        l.append(matrice[i+1][j+1][0])

    return l



def coordonneesVoisins(i, j, matrice):

    """ Créer une liste contenant les coordonnées des cases voisines d'une case"""

    # l'ordre des voisins dans la liste est défini de gauche à droite puis de haut en bas
    l = []

    if i==0 and j==0 :
        l.append((i, j+1))
        l.append((i+1, j))
        l.append((i+1, j+1))
    elif i==0 and (j==len(matrice)-1):
        l.append((i, j-1))
        l.append((i+1, j-1))
        l.append((i+1, j))
    elif (i==len(matrice)-1) and j==0:
        l.append((i-1, j))
        l.append((i-1, j+1))
        l.append((i, j+1))
    elif (i==len(matrice)-1) and (j==len(matrice)-1):
        l.append((i-1, j-1))
        l.append((i-1, j))
        l.append((i, j-1))
    elif i==0 and 0<j<(len(matrice)-1):
        l.append((i, j-1))
        l.append((i, j+1))
        l.append((i+1, j-1))
        l.append((i+1, j))
        l.append((i+1, j+1))
    elif (i==len(matrice)-1) and 0<j<(len(matrice)-1):
        l.append((i-1, j-1))
        l.append((i-1, j))
        l.append((i-1, j+1))
        l.append((i, j-1))
        l.append((i, j+1))
    elif (0<i<(len(matrice)-1) and j==0):
        l.append((i-1, j))
        l.append((i-1, j+1))
        l.append((i, j+1))
        l.append((i+1, j))
        l.append((i+1, j+1))
    elif 0<i<(len(matrice)-1) and j==(len(matrice)-1):
        l.append((i-1, j-1))
        l.append((i-1, j))
        l.append((i, j-1))
        l.append((i+1, j-1))
        l.append((i+1, j))
    else :
        l.append((i-1, j-1))
        l.append((i-1, j))
        l.append((i-1, j+1))
        l.append((i, j-1))
        l.append((i, j+1))
        l.append((i+1, j-1))
        l.append((i+1, j))
        l.append((i+1, j+1))

    return l


############################################
##### Fonctions pour la gestion des populations



def apparitionProies(matrice, n):
    """ Fait apparaître n proies aléatoirement dans la matrice (avant le 1er tour)"""
    
    cpt = 0

    while cpt != n:
        i = rd.randint(0, len(matrice)-1)
        j = rd.randint(0, len(matrice)-1)
        # On choisit au hasard une coordonnée (i,j) où une proie apparaîtra
        if matrice [i][j][0] == 0:        ## Si la case n'est pas déjà occupée
            identiteProies(matrice, i, j)
            cpt += 1

    return matrice



def apparitionPredateurs(matrice, n):
    """ Fait apparaître n prédateurs aléatoirement dans la matrice (au début du 1er tour)"""
    
    cpt = 0

    while cpt != n:
        i = rd.randint(0, len(matrice)-1)
        j = rd.randint(0, len(matrice)-1)
        # On choisit au hasard une coordonnée (i,j) où une proie apparaîtra
        if matrice [i][j][0] == 0:        ## Si la case n'est pas déjà occupée
            identitePredateurs(matrice, i, j)
            cpt += 1

    return matrice



def naissanceAleatoireProies():
    """ Fait apparaître F_PRO proies aléatoirement (à chaque début de tour)""" ## on considère cette fonction inutile, à voir si on la fait ou pas
    pass



def identiteProies(matrice, x, y):
    """ Remplit la case de la matrice par le tuple correspondant à l'identité de la proie (son âge, etc...)"""
    
    matrice[x][y] = (1, A_PRO, 0)

    return



def identitePredateurs(matrice, x, y):
    """ Remplit la case de la matrice par le tuple correspondant à l'identité du prédateur"""
    
    matrice[x][y] = (2, A_PRE, E_PRE)

    return



def ageProies(matrice):
    """ Prend en argument la matrice et diminue de 1 l'âge de toutes les proies"""
    
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j][0] == 1:       # si c'est une proie
                matrice[i][j][1] -= 1       # son âge diminue de 1



def ageEnergiePredateurs(matrice):
    """ Prend en argument la matrice et diminue de 1 l'âge et l'énergie de tous les prédateurs"""
    
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j][0] == 2:       # si c'est un prédateur
                matrice[i][j][1] -= 1       # son âge diminue de 1
                matrice[i][j][2] -= 1       # son énergie diminue de 1


def deplacementProies():
    """ Fait bouger toutes les proies"""
    pass


def deplacementPredateurs():
    """ Fait bouger tous les prédateurs"""
    pass


def reproductionProies(matrice):
    """ Si 2 proies sont à côté, alors elles se reproduisent (on décide que les proies ne 
    peuvent se reproduire au maximum qu'une seule fois par tour)"""
    
    matrice_proies = [[(0,0)]*len(matrice) for b in range(len(matrice))]


    # On commence par créer une nouvelle matrice de la même taille que la matrice d'entrée,
    # qui contient un 1 s'il y a une proie, un 0 sinon (cela simplifie l'utilisation de la matrice)
    for x in range(len(matrice_proies)):
        for y in range(len(matrice_proies)):
            if matrice[x][y][0] == 1:       ## Si c'est une proie
                matrice_proies[x][y] = (1,0)


    # On parcourt notre matrice contenant les informations des positions des proies puis l'on regarde
    # si une proie est à coté d'une autre ; si c'est le cas, elles se reproduisent
    for i in range(len(matrice_proies)):
        for j in range(len(matrice_proies)):
            if matrice_proies[i][j] == (1,0) :       ## Si c'est une proie
                voisins = voisinage(i, j, matrice_proies)
                voisins_vide = voisinage(i, j, matrice)
                if (1 in voisins) and (0 in voisins_vide):        
                    ## Si la proie est à côté d'une autre proie et qu'il y a une case vide pour la naissance
                    verif_naissance = 0
                    while matrice_proies[i][j] == (1,0):        ## Tant que la proie ne s'est pas reproduit
                        h = rd.randint(0, (len(voisins)-1))
                        if voisins[h] == 1:      ## Si un voisin pris au hasard est une proie, il y a reproduction
                            matrice_proies[i][j] = (0,0)        ## La proie ne peut plus se reproduire pendant ce tour          
                            coord_pro = coordonneesVoisins(i, j, matrice)
                            matrice_proies[coord_pro[h][0]][coord_pro[h][1]] = (0,0)
                            while verif_naissance == 0:      ## Tant qu'il n'y a pas eu la naissance 
                                k = rd.randint(0, (len(voisins_vide)-1))
                                if voisins_vide[k] == 0:           ## Si la case choisie au hasard est vide
                                    identiteProies(matrice, coord_pro[k][0], coord_pro[k][1])
                                    #matrice[coord_pro[k][0]][coord_pro[k][1]] = (1, A_PRO)
                                    verif_naissance = 1
                                

    return matrice



def reproductionPredateurs(matrice):
    """ Si 2 prédateurs sont à côté et que leur énergie est supérieure à l'énergie nécessaire pour la reproduction
    (E_repro), alors ils se reproduisent"""
    
    matrice_pred = [[(0,0,0)]*len(matrice) for b in range(len(matrice))]


    # On commence par créer une nouvelle matrice de la même taille que la matrice d'entrée,
    # qui contient un 1 s'il y a un prédateur, un 0 sinon (cela simplifie l'utilisation de la matrice)
    for x in range(len(matrice_pred)):
        for y in range(len(matrice_pred)):
            if matrice[x][y][0] == 2:       ## Si c'est un prédateur
                if matrice[x][y][2] >= E_REPRO:       ## S'il a une energie suffisante pour se reproduire
                    matrice_pred[x][y] = (1,0,0)


    # On parcourt notre matrice contenant les informations des positions des proies puis l'on regarde
    # si une proie est à coté d'une autre ; si c'est le cas, elles se reproduisent
    for i in range(len(matrice_pred)):
        for j in range(len(matrice_pred)):
            if matrice_pred[i][j] == (1,0,0) :       ## Si c'est un prédateur
                voisins = voisinage(i, j, matrice_pred)
                voisins_vide = voisinage(i, j, matrice)
                if (1 in voisins) and (0 in voisins_vide):        
                    ## Si le prédateur est à côté d'un autre prédateur et qu'il y a une case vide pour la naissance
                    verif_naissance = 0
                    while matrice_pred[i][j] == (1,0,0):        ## Tant que le prédateur ne s'est pas reproduit
                        h = rd.randint(0, (len(voisins)-1))
                        if voisins[h] == 1:      ## Si un voisin pris au hasard est aussi un prédateur, il y a reproduction
                            matrice_pred[i][j] = (0,0,0)        ## Le prédateur ne peut plus se reproduire pendant ce tour          
                            coord_pro = coordonneesVoisins(i, j, matrice)
                            matrice_pred[coord_pro[h][0]][coord_pro[h][1]] = (0,0,0)          ### = 0 ?
                            while verif_naissance == 0:      ## Tant qu'il n'y a pas eu la naissance 
                                k = rd.randint(0, (len(voisins_vide)-1))
                                if voisins_vide[k] == 0:           ## Si la case choisie au hasard est vide
                                    identitePredateurs(matrice, coord_pro[k][0], coord_pro[k][1])
                                    #matrice[coord_pro[k][0]][coord_pro[k][1]] = (1, A_PRO)
                                    verif_naissance = 1

    return matrice



def predation():
    """ Si une proie et un prédateur sont sur la même case, alors la proie meure et le prédateur gagne MIAM"""
    pass



def mortProies(matrice):
    """ Prend en argument une matrice, vérifie la durée de vie restante de toutes les proies, si elle est égale à 0,
    alors elle meurt donc l'identité de la case devient un tuple de 0"""
    #global matrice => un paramètre peut pas être global => voir cmt on gère le code
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j][1] == 0 and matrice[i][j][0] == 1: #si c'est une proie et
                #qu'elle est trop âgée
                matrice[i][j][0] = 0 #devient une case du décor



def mortPrédateurs(matrice):
    """ Prend en argument une matrice, vérifie la durée de vie restante et l'énergie E_PRE de tous les prédateurs, 
    si au moins l'une des deux est égale à 0, alors il meurt donc l'identité de la case devient un tuple de 0"""
    #global matrice => un paramètre peut pas être global => voir cmt on gère le code
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j][1] == 0 and matrice[i][j][0] == 2: #si c'est un prédateur et
                #qu'il est trop âgé
                matrice[i][j][0] = 0 #devient une case du décor
            elif matrice[i][j][0] == 2 and matrice[i][j][2] == 0: #si c'est un prédateur et
                #qu'il n'a plus d'énergie
                matrice[i][j][0] = 0 #devient une case du décor



def tours():
    """Fonction qui gère les tours et les conditions associées à ceux-ci en appelant toutes
    les fonctions qui gèrent les variations d'états liés aux tours"""
    #appeler toutes les fonctions liées et voir pour le global de la matrice
    #vérifier que ça fonctionne avec des prints
    canevas.after(30, tours())
    return




############################################
### Boucle principale
############################################

racine = tk.Tk()
racine.title("Simulation d'un système proies/prédateurs")


############################################
##### Création des widgets

canevas = tk.Canvas(racine, height=HAUTEUR_CANEVAS, width=LARGEUR_CANEVAS, bg='white')
creationGrille(NB_CASES)


############################################
##### Placement des widgets

canevas.grid(column=0, row=0)



racine.mainloop()