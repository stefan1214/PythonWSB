import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(8, 6), dpi=80)
plt.subplot(1, 1, 1)
X = np.linspace(-np.pi, np.pi,256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C, color="blue",linewidth=1.0, linestyle="-")
plt.plot(X, S, color="green",linewidth=1.0, linestyle="-")

# plt.xlim(-4.0, 4.0)
# plt.ylim(-1.0, 1.0)
#
# plt.xticks(np.linspace(-4, 4, 9,endpoint=True))
# plt.yticks(np.linspace(-1, 1, 5,endpoint=True))

plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.ylim(C.min() * 1.1, C.max() * 1.1)

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2,np.pi])
plt.yticks([-1, 0, +1])

plt.show()