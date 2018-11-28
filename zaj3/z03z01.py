#!/ usr / bin / env python
# -*- coding : utf -8 -*-

import numpy as np
import matplotlib.pyplot as plt

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))

x = np.arange(-10, 10, 0.5)
y = a * x - b
plt.plot(x, y)

plt.title('Wykres f(x) = a*x-b = ' + str(a) + '*x-' + str(b))
plt.grid(True);

plt.show()
