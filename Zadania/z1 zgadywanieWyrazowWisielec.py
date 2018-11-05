import random
slowa = ("python", 'ziom', "dlaczego", "ziomeczek", "dom")

word = random.choice(slowa)
print("Wysloswany wyraz zawiera", len(word), "liter")

for i in range(0,5):
    odp = input("Podaj literę: ")
    for znak in word:
        if znak == odp:
            print("TAK")
            break
    if znak!= odp:
        print("NIE")
if input("Musisz teraz odgadnąć słowo: ") == word:
    print("Brawo zgadłeś")
else:
    print("Nie zgadłeś")


