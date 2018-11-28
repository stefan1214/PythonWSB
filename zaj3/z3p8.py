from pylab import *

figure(figsize=(12, 8), dpi=100)
x = linspace(-2 * pi, 2 * pi, 100)
subplot(211)  # 2- wiersze , 1 - kolumna ,plot -1
plot(x, sin(x))
subplot(234)  # 2- wiersze , 3 - kolumny ,plot -4
plot(x, sin(x) / x)
subplot(235)  # 2- wiersze , 3 - kolumny ,plot -5
plot(x, exp(-x ** 2))
subplot(236)  # 2- wiersze , 3- kolumny , plot-6
plot(x, sqrt(1 - x ** 2))
show()
