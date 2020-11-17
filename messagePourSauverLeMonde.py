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







