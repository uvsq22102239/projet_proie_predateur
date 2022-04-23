import random as rd

A_PRE = 5
E_PRE = 3


def identitePredateurs(matrice, x, y):
    """ Remplit la case de la matrice par le tuple correspondant à l'identité du prédateur"""
    
    matrice[x][y] = (2, A_PRE, E_PRE)

    return
### ajout du return


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


def reproductionPredateurs(matrice):
    """ Si 2 prédateurs sont à côté et que leur énergie est supérieure à l'énergie nécessaire pour la reproduction
    (E_repro), alors ils se reproduisent"""
    
    matrice_pred = [[(0,0, 0)]*len(matrice) for b in range(len(matrice))]


    # On commence par créer une nouvelle matrice de la même taille que la matrice d'entrée,
    # qui contient un 1 s'il y a un prédateur, un 0 sinon (cela simplifie l'utilisation de la matrice)
    for x in range(len(matrice_pred)):
        for y in range(len(matrice_pred)):
            if matrice[x][y][0] == 1:       ## Si c'est un prédateur
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