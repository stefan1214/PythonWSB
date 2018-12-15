import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
t = ("Słownik zastępujący domyślne właściwości tekstu. Jeśli fontdict ma wartość None, wartości domyślne są określane przez parametry rc.")
plt.text(7, 3, t, ha='left', rotation=15, wrap=True)
plt.text(3, 5, t, ha='left', rotation=15, wrap=True)
plt.text(1, 8, t, ha='right', rotation=-15, wrap=True)
plt.text(5, 10, t, fontsize=18, style='oblique', ha='center',
         va='top', wrap=True)
plt.text(3, 4, t, family='serif', style='italic', ha='right', wrap=True)
plt.text(-1, 0, t, ha='left', rotation=-15, wrap=True)

plt.show()