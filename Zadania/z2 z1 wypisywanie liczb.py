# Napisz program, który wypisuje liczby od START do STOP w kroku zadanym przez
# użytkownika. Umożliw użytkownikowi wprowadzenie liczby początkowej, liczby
# końcowej i wielkości odstępu między kolejnymi liczbami.

print("Program odliczający")

start = int(input("Podaj liczbę poczatkową: "))
end = int(input("Podaj liczbę końcową: "))
step = int(input("Podaj krok: "))

for i in range(start, end + 1, step):
    print(i)
