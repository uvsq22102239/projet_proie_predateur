# définir HAUTEUR_CANEVAS + LARGEUR_CANEVAS + NB_CASAS

HAUTEUR_CANEVAS = 500
LARGEUR_CANEVAS = 500
NB_CASES = 30



import tkinter as tk

racine = tk.Tk()
racine.title("Simulation d'un système proies/prédateurs")

canevas = tk.Canvas(racine, height=HAUTEUR_CANEVAS, width=LARGEUR_CANEVAS, bg='white')
canevas.grid(column=0, row=0)

def creationGrille(NB_CASES):
    """ Créer une grille carrée de NB_CASES cases de largeur"""

    taille_case = LARGEUR_CANEVAS / NB_CASES

    for k in range(1, (NB_CASES)):
        # lignes verticales
        canevas.create_line((k * taille_case), 0, (k * taille_case), HAUTEUR_CANEVAS)
        # lignes horizontales
        canevas.create_line(0, (k * taille_case), LARGEUR_CANEVAS, (k * taille_case))

creationGrille(NB_CASES)

racine.mainloop()