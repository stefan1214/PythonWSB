cenaSamochodu=int(input("Podaj cenę samochdu: "))
podatek = cenaSamochodu * 0.03
oplataRejestracyjna = 180.50
prowizjaPrzygotowawczaDealera = cenaSamochodu * 0.08
opłataZaDostarczenie = 500

print("Cena samochodu:",round(cenaSamochodu,2))
print("Podatek:",round(podatek,2))
print("Koszt rejestrtacji pojazdu:",round(oplataRejestracyjna,2))
print("Prowizja dealera:",round(prowizjaPrzygotowawczaDealera,2))
print("Koszt dostraczenia:",round(opłataZaDostarczenie,2))
print("Całkowity koszt samochodu:"+str(round(cenaSamochodu+opłataZaDostarczenie+oplataRejestracyjna+prowizjaPrzygotowawczaDealera,2)))

