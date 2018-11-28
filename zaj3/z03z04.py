#!/ usr / bin / env python
# -*- coding : utf -8 -*-

import numpy as np
import matplotlib.pyplot as plt

a = 1
b = -3
c = 1

x = np.arange(-10, 10, 1)

y = a * x * x + b * x + c

plt.plot(x, y)

plt.title('Wykres f(x) = a*x^2+b*x+ c')
plt.grid(True)

plt.show()
