import random

ludz = (
("""
------
|    |
|
|
|
|
|
|
|
---------
"""),
("""
------
|    |
|    0
|
|
|
|
|
|
---------
"""),
("""
------
|    |
|    0
|   -+-
|
|
|
|
|
---------
"""),
("""
------
|    |
|    0
|  /-+-
|
|
|
|
|
---------
"""),
("""
------
|    |
|    0
|  /-+-/
|
|
|
|
|
---------
"""),
("""
------
|    |
|    0
|  /-+-/
|    |
|    
|
|
|
---------
"""),
("""
------
|    |
|    0
|  /-+-/
|    |
|    |
|
|
|
---------
"""),
("""
------
|    |
|    0
|  /-+-/
|    |
|    |
|   |
|   |
|
---------
"""),
("""
------
|    |
|    0
|  /-+-/
|    |
|    |
|   | |
|   | |
|
---------
""")

)

MAX_POMYLKA=len(ludz)-1
slowa = ("MORZE", "BALTYK", "GDYNIA", "SLASKA", "PYTHON")
slowo = random.choice(slowa)
dlugosc_slowa = "-" * len(slowo)
POMYLKA=0
uzyte=[]
print("Witaj w grze ’Wisielec'. Powodzenia!")
while POMYLKA < MAX_POMYLKA and dlugosc_slowa != slowo:
    print(ludz[POMYLKA])
    print("\nWykorzystałeś już następujące litery:\n", uzyte)
    print("\nNa razie zagadkowe słowo wygląda tak:\n", dlugosc_slowa)
    zgadnij = input("\n\nWprowadź literę: ")
    zgadnij = zgadnij.upper() # zamiana na duże litery wprowadzonych liter
    while zgadnij in uzyte:
        print("Już wykorzystałeś literę", zgadnij)
        zgadnij = input("Wprowadź literę: ")
        zgadnij = zgadnij.upper()
    uzyte.append(zgadnij)

    if zgadnij in slowo:
        print("\nTak!", zgadnij, "znajduje się w zagadkowym słowie!")
        nowa = ""
        for i in range(len(slowo)):
            if zgadnij == slowo[i]:
                nowa += zgadnij
            else:
                nowa += dlugosc_slowa[i]
        dlugosc_slowa = nowa
    else:
        print("\nNiestety,", zgadnij, "nie występuje w zagadkowym słowie.")
        POMYLKA += 1

    if POMYLKA == MAX_POMYLKA:
        print(ludz[POMYLKA])
        print("\nZostałeś powieszony!")
    else:
        print("\nOdgadłeś!")
        print("\nZAagadkowe słowo to", slowo)