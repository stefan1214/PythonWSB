# Popraw program Wymieszane litery tak, żeby każdemu słowu towarzyszyła
# podpowiedź. Gracz powinien mieć możliwość zobaczenia podpowiedzi, jeśli
# utknie w martwym punkcie. Dodaj system punktacji, który nagradza graczy
# rozwiązujących anagram bez uciekania się do podpowiedzi.

import random

slowa = ("python", 'ziom', "dlaczego", "ziomeczek", "dom")

print("Gra: odgadnij słowa")
print("Za zgadniete słowo otrzymujesz 5 pkt")
print("Za każdą podpowiedź tracisz 1 pkt")
print("Musisz odgadnąć", len(slowa), "słów")
print("Możesz uzyskać maksymalnie", len(slowa) * 5, "pkt")

wynik = 0;
for runda in range(0, len(slowa)):
    word = random.choice(slowa)
    # print(word)
    poprawnie = word
    pomie = ""
    print("Runda " + str(runda + 1) + ": wynik:", wynik, "pkt")
    while word:
        position = random.randrange(len(word))
        pomie += word[position]
        word = word[:position] + word[(position + 1):]
    odp = ""
    odp = input("Ułóż poprawne słowo z liter: " + pomie + "\n")
    dlugoscPodpowiedzi = len(poprawnie)
    i = 0
    while odp != poprawnie:
        if i < dlugoscPodpowiedzi - 1:
            print("Tracisz 1 pkt")
            print("Podpowiedź", poprawnie[:i + 1])
            i += 1
            wynik -= 1
            odp = input("Podaj słowo: ")
            continue
        else:
            print("Nie zgadłeś!")
            break

    if odp == poprawnie:
        print("Zgadłeś!")
        wynik += 5

print("Ukończyłeś grę!")
print("Twój wynik:", wynik)
