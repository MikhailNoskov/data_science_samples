import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-white')

# Visualizing a Three-Dimensional Function


def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# plt.contour(X, Y, Z, colors='black')  # Single color
# plt.contour(X, Y, Z, 20, cmap='RdGy')

# plt.contourf(X, Y, Z, 20, cmap='RdGy')  # A filled contour plot
# plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy',
#            interpolation='gaussian', aspect='equal')  # A smooth two-dimensional
contours = plt.contour(X, Y, Z, 3, colors='black')
plt.clabel(contours, inline=True, fontsize=8)  # Contours added
plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy', alpha=0.5)
plt.colorbar()
plt.show()
