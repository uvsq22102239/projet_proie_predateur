def identiteProies(matrice, x, y):
    """ Remplit la case de la matrice par le tuple correspondant à l'identité de la proie (son âge, etc...)"""
    
    matrice[x][y] = (1, A_PRO)



def identitePredateurs(matrice, x, y):
    """ Remplit la case de la matrice par le tuple correspondant à l'identité du prédateur"""
    
    matrice[x][y] = (2, A_PRE, E_PRE)
