#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

print("Gra w kości")

ileKosci = int(input("Iloma kośćmi chcesz rzucić: "))

kosci = []



def one():
    print("  - - -  ")
    print("|       |")
    print("|   *   |")
    print("|       |")
    print("  - - -  ")
def two():
    print("  - - -  ")
    print("| *     |")
    print("|       |")
    print("|     * |")
    print("  - - -  ")
def three():
    print("  - - -  ")
    print("| *     |")
    print("|   *   |")
    print("|     * |")
    print("  - - -  ")
def four():
    print("  - - -  ")
    print("| *   * |")
    print("|       |")
    print("| *   * |")
    print("  - - -  ")
def five():
    print("  - - -  ")
    print("| *   * |")
    print("|   *   |")
    print("| *   * |")
    print("  - - -  ")
def six():
    print("  - - -  ")
    print("| *   * |")
    print("| *   * |")
    print("| *   * |")
    print("  - - -  ")
switcher = {
    0: one,
    1: two,
    2: three,
    3: four,
    4: five,
    5: six
}
def koscGraficznie(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()

for kosc in range(0,ileKosci):
    input("Kliknij aby rzucić kością: ")
    kosci.append(random.randint(0, 5))
    koscGraficznie(kosci[kosc])
sumaOczek=0
for kosc in range(0,ileKosci):
    sumaOczek = sumaOczek + kosci[kosc]

print("Suma oczek wyrzuconych kosci: ", sumaOczek)
