# Napisz program, który podany przez użytkownika ciąg znaków szyfruje przy
# użyciu szyfru Cezara i wyświetla zaszyfrowany tekst.

# ! /usr/bin/env python3
# -*- coding: utf-8 -*-

KLUCZ = 3


def szyfruj(txt):
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KLUCZ:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ - 26)
        else:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ)
    return zaszyfrowny


# def deszyfruj(tekst):
#     odszyfrowany = ""
#     KLUCZM = KLUCZ % 26
#     for znak in tekst:
#         if (ord(tekst) - KLUCZM < 97):
#             odszyfrowany += chr(ord(tekst) - KLUCZM + 26)
#         else:
#             odszyfrowany += chr(ord(tekst) - KLUCZM)
#     return odszyfrowany

def main(args):
    tekst = input("Podaj ciąg do zaszyfrowania:\n")
    print("Ciąg zaszyfrowany:\n", szyfruj(tekst))
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
