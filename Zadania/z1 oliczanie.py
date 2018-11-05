print("Program odliczający")

start = int(input("Podaj liczbę poczatkową: "))
end = int(input("Podaj liczbę końcową: "))
step = int(input("Podaj krok: "))

for i in range(start, end+1, step):
    print(i)