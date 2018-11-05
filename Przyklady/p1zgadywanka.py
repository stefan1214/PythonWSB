#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

liczba = random.randint(1, 49)
#print("Wylosowana liczba: ", liczba)


for i in range(6):
    print("Próba ", i+1)
    odp = input("Jaka liczbę od 1 do 49 wylosowano: ")

    if liczba == int(odp):
        print("Hura!!!")
        break
    elif i==5:
        print("wyslowano: ", liczba)
    else:
        print("No niestety")
        if int(odp) > liczba:
            print("Wyslosowana liczba jest mniejsza od: ", odp)
        else:
            print("Wyslosowana liczba jest większa od: ", odp)
