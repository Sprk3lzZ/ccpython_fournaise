# -*- coding: utf-8 -*-

file_volcan = open('messagePourSauverLeMonde.txt', "r")

for line1 in file_volcan:
    if 'volcan' in line1:
        print("A l’aide, tous aux abris !\n")
file_volcan.close()

############################################################


file_arbre = open('livreDeLaNatureEtDesLacs.txt', "r")

for line2 in file_arbre:
    if 'arbre suspendu' in line2:
        print(line2)
file_arbre.close()

############################################################

file_abri = open('desProjectilesEtDesDodos.txt', "r")
pas = 0
gauche = 0
droite = 0
avant = 0

for line3 in file_abri:
    if 'rocher' in line3:
        pas += 5
        gauche += 5
    if 'arbre' in line3:
        pas += 10
        avant += 10
    if 'dodo' in line3:
        pas += 6
        droite += 6

    if pas >= 100 and 'lac' in line3:
        if droite > avant and droite > gauche:
            max = "droite"
        elif avant > droite and avant > gauche:
            max = "avant"
        else:
            max = "gauche"
        print("Vous avez fait un nombre de ",pas, " dont la pluspart vers la/l' : ", max)
        print("\n")
file_abri.close()



################################################################################################


file_abri = open('LafamilleDodo.txt','r')
dodo = file_abri.readline()
citoyen = dodo.split(", ")

citoyen = [int(x) for x in citoyen]
citoyen.sort()

for loop in range(len(citoyen)-10):
    if citoyen[loop+1] == citoyen[loop]:
        del citoyen[loop]

print(citoyen)



