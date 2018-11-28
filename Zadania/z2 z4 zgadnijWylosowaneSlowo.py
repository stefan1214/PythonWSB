# Utwórz grę, w której komputer wybiera losowo słowo, które gracz musi
# odgadnąć. Komputer informuje gracza, ile liter znajduje się w wybranym
# słowie. Następnie gracz otrzymuje pięć szans na zadanie pytania, czy jakaś litera
# jest zawarta w tym słowie. Komputer może odpowiedzieć tylko „tak” lub „nie”.
# Potem gracz musi odgadnąć słowo.

import random

slowa = ("python", 'ziom', "dlaczego", "ziomeczek", "dom")

word = random.choice(slowa)
print("Wysloswany wyraz zawiera", len(word), "liter")

for i in range(0, 5):
    odp = input("Podaj literę: ")
    for znak in word:
        if znak == odp:
            print("TAK")
            break
    if znak != odp:
        print("NIE")
if input("Musisz teraz odgadnąć słowo: ") == word:
    print("Brawo zgadłeś")
else:
    print("Nie zgadłeś")
