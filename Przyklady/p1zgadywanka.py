#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

ileliczb = int(input("Podaj ilość typowanych liczb: "))
maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))


liczba=[]

for x in range(ileliczb):
    liczba.append(random.randint(1, maksliczba))

for n in range(ileliczb):
    print("Liczba %s z %s" % (n+1,ileliczb))

    for i in range(6):
        print("Próba ", i+1)
        odp = int(input("Jaka liczbę od 1 do "+str(maksliczba)+" wyslowoano"))

        if liczba[n] == int(odp):
            print("Hura!!!")
            break
        elif i==5:
            print("wyslowano: ", liczba[n])
        else:
            print("No niestety")
            if int(odp) > liczba[n]:
                print("Wyslosowana liczba jest mniejsza od: ", odp)
            else:
                print("Wyslosowana liczba jest większa od: ", odp)
