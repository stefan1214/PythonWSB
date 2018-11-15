# Utwórz program, który wczytuje komunikat użytkownika, a następnie wypisuje go w
# odwrotnej kolejności.

komunikat = input("Podaj treść komunikatu")

# nowyKomunikat=""
# for znak in range(0,len(komunikat)):
#     nowyKomunikat = nowyKomunikat + komunikat[len(komunikat)-1-znak:len(komunikat)-znak]
# print("Komunikat od tyłu: ", nowyKomunikat)

print("Komunikat od tyłu: ", komunikat[::-1])