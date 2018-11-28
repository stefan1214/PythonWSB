#!/ usr / bin / env python
# -*- coding : utf -8 -*-

import numpy as np
import matplotlib.pyplot as plt


x1 = np.arange(0, 20, 1)
x2 = np.arange(0, 100, 1)
x3 = np.arange(0, 100, 1)
y1 = x1
y2 = x2*x2
y3 = x3**x3

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)

plt.title('Trzy różne wykresy')
plt.grid(True);

plt.show()
