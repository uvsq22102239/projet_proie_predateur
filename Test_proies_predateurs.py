def predation(matrice):
    """ Si une proie et un prédateur sont sur la même case, alors la proie meure et le prédateur gagne MIAM"""
    
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j][0] == 2:
                



def voisinnage(i, j, matrice):
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