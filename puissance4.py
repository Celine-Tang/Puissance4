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
	if 3 >= col :
		if gril[lig][col+1] == j and gril[lig][col+2] == j and gril[lig][col+3] == j:
			return True
		else :
			return False
	elif col >= 3 :
		if gril[lig][col-1] == j and gril[lig][col-2] == j and gril[lig][col-3] == j:
			return True
		else :
			return False

#3.6
def vert(gril,j,lig,col) :
	if 3>lig :
		if gril[lig+1][col] == j and gril[lig+2][col] == j and gril[lig+3][col] == j:
			return True
		else :
			return False
	elif lig>=3 :
		if gril[lig-1][col] == j and gril[lig-2][col] == j and gril[lig-3][col] == j:
			return True
		else :
			return False

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
def victoire(gril, j, lig, col):
	if horiz(gril, j, lig, col)== True:
		return True
	elif vert(gril, j, lig, col) == True:
		return True
	elif diag_haut(gril, j, lig, col) == True:
		return True
	elif diag_bas(gril, j, lig, col) == True:
		return True
	else:
		return False

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
def coup_aleatoire(gril,j):
	a = random.randint(0,6)
	if gril[5][a] == 0 :
		gril[5][a] = j
	elif gril[4][a] == 0 :
		gril[4][a] = j
	elif gril[3][a] == 0 :
		gril[3][a] = j
	elif gril[2][a] == 0 :
		gril[2][a] = j
	elif gril[1][a] == 0 :
		gril[1][a] = j
	elif gril[0][a] == 0 :
		gril[0][a] = j
	return(gril)


#fonction du jeu final
def jeu_fini():
	gril = grille_vide()
	j = 1 #futil (pour éviter une erreur à la fonction victoire)
	lig = 0 #futil (pour éviter une erreur à la fonction victoire)
	col = 0 #futil (pour éviter une erreur à la fonction victoire)
	while match_nul(gril) or victoire(gril,j,lig,col) == False :
		j = int(input("insérer votre joueur :"))
		x = str(input("voulez-vous un coup aléatoire ? (répondre 'oui' ou 'non')"))
		if x == "oui" :
			coup_aleatoire(gril,j)
		else :
			lig = int(input("insérer la ligne :")) #pour vérifier s'il y a victoire du joueur
			col = int(input("insérer la colonne:"))
			if coup_possible(gril,col) == True :
				jouer(gril,j,col)
		affiche(gril)
	if match_nul(gril) == True :
		return ("match nul")
	elif victoire(gril,j,lig,col) == True :
		return ("victoire du joueur", j)


