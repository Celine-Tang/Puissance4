#3.1
def grille_vide():
    tableau = []
    while len(tableau)<6 :
        tableau.append([0,0,0,0,0,0,0])
    return tableau
grille_vide()

#3.2
def affiche(gril):
    for i in gril :
        for b in i :
            if b == 0:
                print("|.",end='')
            if b == 1:
                print("|x",end='')
            if b == 2:
                print("|0",end='')
        print("|")

#3.3
def coup_possible(gril,col):
    c = gril[0][col]
    if c == 0 :
        return True
    else : 
        return False
    
#3.4
def jouer(gril, j, col):
    if col == 0 :
        if j == 1:
            col = 1
        else :
            col = 2
            
#3.5
def horiz(gril,j,lig,col) :
    r = gril[lig][col] 
    if j == r :
        if gril[lig][col+1] == r and gril[lig][col+2] == r and gril[lig][col+3]:
            return True

#3.6
def vert(gril,j,lig,col) :
    r = gril[lig][col] 
    if j == r :
        if gril[lig+1][col] == r and gril[lig+2][col] == r and gril[lig+3][col]:
            return True
        elif gril[lig-1][col] == r and gril[lig-2][col] == r and gril[lig-3][col]:
            return True 

#3.10
def match_nul(gril) :
    h =[]
    for col in gril[0] :
        if col != 0 :
            h.append(7)
    if len(h) == 7 :
        return True
    else :
        return False

#3.9
def victoire(gril, j):
    for j in gril:
        if horiz() == True:
            return(True)
        elif vert() == True:
            return(True)
        elif diag_haut() == True:
            return(True)
        elif diag_bas() == True:
            return(True)
        else:
            return(False)
        
#3.10
def match_nul(gril) :
        
#3.11
import random 
def coup_aleatoire(gril, j):
    n = random.randint(0,7)
    if coup_possible(gril, ) == True:
        return jouer(gril, j, n)
    
