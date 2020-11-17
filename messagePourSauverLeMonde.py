# -*- coding: utf-8 -*-
from __future__ import unicode_literals

file_volcan = open('messagePourSauverLeMonde.txt', "r")

for line1 in file_volcan:
    if 'volcan' in line1:
        print("A l’aide, tous aux abris !\n")
file_volcan.close()








