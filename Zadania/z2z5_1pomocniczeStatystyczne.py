from statistics import median
import math


def srednia(lista):
    # ile = len(lista)
    # suma = 0
    # for i in lista:
    #     suma += i
    # return suma / ile
    return sum(lista) / float(len(lista))


def mediana(lista):
    return median(lista)


def odchylenieStandardowe(lista):
    ile = len(lista)
    x2 = [x ** 2 for x in lista]
    return math.sqrt(float(ile) / (ile - 1) * (srednia(x2) - srednia(lista) ** 2))
