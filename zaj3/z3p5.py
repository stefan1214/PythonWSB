import numpy as np
import matplotlib.pyplot as plt


#Funkcja arange jest podobna do standardowej funkcji range wytwarzającej określone sekwencje w postaci listy.
# Funkcja arange zamiast listy wytwarza tablicę zawierającą ciąg liczb zmiennoprzecinkowych
# zaczynający się od pierwszego podanego argumentu funkcji arange 0 do ostatniego 2 w kroku co 0.01 (0.00, 0.01, … 1.99,2.00)

x = np.arange(0.0, 2.0, 0.01)
y = np.sin(2.0 * np.pi * x)
plt.plot(x, y)
plt.show()
