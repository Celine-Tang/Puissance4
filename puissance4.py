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
def jouer(gril,j,col):
    if gril[5][col]==0:
        gril[5][col]=j
    elif gril[4][col]==0:
        gril[4][col]=j
    elif gril[3][col]==0:
        gril[3][col]=j
    elif gril[2][col]==0:
        gril[2][col]=j
    elif gril[1][col]==0:
        gril[1][col]=j
    elif gril[0][col]==0:
        gril[0][col]=j
    return gril


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

#3.7
def diag_haut(gril, j, lig, col):
    if lig>2 and col>2:
        if gril[lig][col]==j and gril[lig-1][col-1]==j and gril[lig-2][col-2]==j and gril[lig-3][col-3]==j:
            return True
        else:
            return False
    elif lig>2 and col<4:
        if gril[lig][col]==j and gril[lig-1][col+1]==j and gril[lig-2][col+2]==j and gril[lig-3][col+3]==j:
            return True
        else:
            return False

#3.8
def diag_bas(gril,j,lig,col):
    if lig<3 and col>2:
        if gril[lig][col]==j and gril[lig+1][col-1]==j and gril[lig+2][col-2]==j and gril[lig+3][col-3]:
            return True
        else:
            return False
    elif lig<3 and col<4:
        if gril[lig][col]==j and gril[lig+1][col+1]==j and gril[lig+2][col+2]==j and gril[lig+3][col+3]:
            return True
        else:
            return False

#3.9
def victoire(gril, j):
    for j in gril:
        if horiz == True:
            return(True)
        elif vert == True:
            return(True)
        elif diag_haut == True:
            return(True)
        elif diag_bas == True:
            return(True)
        else:
            return(False)

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

#3.11
import random
col=random.randint(0, 6)
def coup_aleatoire(gril,j,col):
    a=0
    for i in range(6):
        if gril[5-i][col]==0 and a==0:
            gril[5-i][col]=j
            a= a + 1
    return(gril)