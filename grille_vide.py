#3.1
def grille_vide():
    tableau = []
    while len(tableau)<6 :
        tableau.append([0,0,0,0,0,0,0])
    return tableau
grille_vide()

assert len(grille_vide()[0])==7
assert len(grille_vide())==6
