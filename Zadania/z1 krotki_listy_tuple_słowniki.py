#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Napisz program, który pobiera od użytkownika słowo, a następnie
#wypisuje je litera po literze jedna pod drugą

slowo = input("Podaj słowo które mam przeliterować: ")

for znak in slowo:
    print(znak)

# Napisz program który liczy od 0 do 10, od 0 do 100 co 5, od 20 do 10
print("---0-10")
for i in range(0, 10):
    print(i)

print("---0-100 co 5")
for i in range(0, 100, 5):
    print(i)

print("---20-10")
for i in range(20, 10, -1):
    print(i)

komunikat = input("Wprowadź komunikat: ")
print("\nDługość Twojego komunikatu wynosi:", len(komunikat))
print("\nNajczęściej używana litera w języku polskim, 'a',")
if "a" in komunikat:
    print("wystąpiła w Twoim komunikacie.")
else:
    print("nie wystąpiła w Twoim komunikacie.")
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
