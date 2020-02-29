#1
def grille_vide():
    return [[0 for j in range(7)] for i in range(6)]
grille_vide()

assert len(grille_vide()[0])==7
assert len(grille_vide())==6