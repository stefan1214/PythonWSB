#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
path='C:/xampp'
pliki = os.listdir(path)
a = len(pliki)
print(a)
for plik in pliki:
    print(plik)


