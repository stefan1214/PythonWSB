# Napisz program, który umożliwi wprowadzanie ocen z podanego przedmiotu,
# następnie policzy i wyświetla średnią, medianę i odchylenie standardowe
# wprowadzonych ocen. Funkcje pomocnicze i statystyczne umieść w osobnym
# module.

from Zadania.z2z5_1pomocniczeStatystyczne import srednia, mediana, odchylenieStandardowe

czyPodacOcene = 0
listaOcen= []
przedmiot = input("Podaj nazwę przedmiotu: ")


def podajOceny():
    while True:
        wprowadzonaOcena = input("Podaj ocene lub niaciśnij ENTER aby zakończyć podawanie ocen: ")
        if wprowadzonaOcena == "":
            break
        try:
            if float(wprowadzonaOcena) % 0.5 != 0 or float(wprowadzonaOcena) < 1.0 or float(wprowadzonaOcena) > 6.0:
                print("Ta ocena jest nieporpwana i nie zostanie dodana \nMożna wprowadzać oceny 1-6 z krokiem 0.5")
                continue
        except ValueError:
            print("Ta ocena jest nieporpwana i nie zostanie dodana \nMożna wprowadzać oceny 1-6 z krokiem 0.5")
            continue
        listaOcen.append(float(wprowadzonaOcena))


def wyswietlOceny():
    print("Oceny z przedmiotu: " + przedmiot)
    for ocena in listaOcen:
        print(ocena)


def oceny():
    return listaOcen


podajOceny()
wyswietlOceny()

print("średnia: " + str(srednia(oceny())))
print("mediana: " + str(mediana(oceny())))
print("odchylenie standardowe: " + str(odchylenieStandardowe(oceny())))
