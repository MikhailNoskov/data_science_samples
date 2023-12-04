import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_olivetti_faces

plt.style.use('classic')
# ax = plt.axes(xscale='log', yscale='log')
# ax.set(xlim=(1, 1E3), ylim=(1, 1E3))
# ax.grid(True)


#Null tick example

# ax = plt.axes()
# rng = np.random.default_rng(1701)
# ax.plot(rng.random(50))
# ax.grid()
# ax.yaxis.set_major_locator(plt.NullLocator())
# ax.xaxis.set_major_formatter(plt.NullFormatter())

# fig, ax = plt.subplots(5, 5, figsize=(5, 5))
# fig.subplots_adjust(hspace=0, wspace=0)
#
# faces = fetch_olivetti_faces().images
# for i in range(5):
#     for j in range(5):
#         ax[i, j].xaxis.set_major_locator(plt.NullLocator())
#         ax[i, j].yaxis.set_major_locator(plt.NullLocator())
#         ax[i, j].imshow(faces[25 * i + j], cmap='binary_r')

# fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)
# For every axis, set the x and y major locator
# for axi in ax.flat:
#     axi.xaxis.set_major_locator(plt.MaxNLocator(3))
#     axi.yaxis.set_major_locator(plt.MaxNLocator(3))

#Fancy Tick Formats
# Plot a sine and cosine curve
fig, ax = plt.subplots()
x = np.linspace(0, 3 * np.pi, 1000)
ax.plot(x, np.sin(x), lw=3, label='Sine')
ax.plot(x, np.cos(x), lw=3, label='Cosine')

# Set up grid, legend, and limits
ax.grid(True)
ax.legend(frameon=False)
ax.axis('equal')
ax.set_xlim(0, 3 * np.pi)

ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))  # Adding major and minor ticks
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))


def format_func(value, tick_number):
    # find number of multiples of pi/2
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N % 2 > 0:
        return rf"${N}\pi/2$"
    else:
        return rf"${N // 2}\pi$"


ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))

plt.show()
