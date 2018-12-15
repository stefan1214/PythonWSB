import numpy as np
from matplotlib import pyplot as plt

data = np.array([2, 4, 6, 8, 10])
data = data * 5

plt.plot(data)

x = np.arange(100)
linear = np.arange(100)
square = [v * v for v in np.arange(0, 10, 0.1)]

lines = plt.plot(x, linear, 'y--', x, square, 'r--')

my_plot = plt.gca()

line0 = my_plot.lines[0]
line0.set_marker('d')
line0.set_linestyle('--')
line0.set_color('b')

plt.setp(lines, linewidth=2)
plt.setp(lines, markersize=6)
plt.setp(lines, dashes=[10, 5, 100, 5])

plt.legend(('funkcja 1', 'funkcja liniowa', 'funkcja 2'), loc='upper left')

plt.title('Trzy różne wykresy')
plt.xlabel('oś X')
plt.ylabel('oś Y')

plt.show()
