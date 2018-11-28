#!/ usr / bin / env python
# -*- coding : utf -8 -*-

import numpy as np
import matplotlib.pyplot as plt

a = float(input("Podaj a: "))

x1 = np.arange(-10, 0, 0.5)
x2 = np.arange(0, 10, 0.5)

y1 = x1 / (-3) + a
y2 = x2 * x2 / 3

plt.plot(x1, y1)
plt.plot(x2, y2)

plt.title('Wykres f(x)')
plt.grid(True);

plt.show()
