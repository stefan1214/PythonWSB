import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(8, 6), dpi=80)
plt.subplot(1, 1, 1)


X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C)
plt.plot(X, S)
plt.show()

