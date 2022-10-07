import numpy as np
import matplotlib.pyplot as plt


X, Y = np.meshgrid(np.linspace(-1.5, 1.5, 1000), np.linspace(-1.5, 1.5, 1000))

# Formule magique
Z = np.exp(-np.abs(5*((X**2 + Y**2 - 1)**3 + X**2 * Y**3)))

# Affichage
plt.imshow(Z, cmap="plasma")
plt.axis("off")
plt.show()
#plt.savefig("jolikeur.png", bbox_inches="tight", pad_inches=0)