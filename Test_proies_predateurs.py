import random as rd



def predation(matrice):
    """ Si une proie et un prédateur sont sur la même case, alors la proie meure et le prédateur gagne MIAM"""
    

    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j][0] == 2:
                voisins = voisinnage(i, j, matrice)
