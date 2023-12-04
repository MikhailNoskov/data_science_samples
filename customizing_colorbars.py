import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from sklearn.datasets import load_digits
from sklearn.manifold import Isomap

plt.style.use('seaborn-white')
# x = np.linspace(0, 10, 1000)
# I = np.sin(x) * np.cos(x[:, np.newaxis])
# plt.imshow(I)
# plt.imshow(I, cmap='jet')  # colored, check plt.cm.<TAB>
# plt.colorbar()


def grayscale_cmap(cmap):
    """Return a grayscale version of the given colormap"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))
    # Convert RGBA to perceived grayscale luminance
    # cf. http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]
    return LinearSegmentedColormap.from_list(cmap.name + "_gray", colors, cmap.N)


def view_colormap(cmap):
    """Plot a colormap with its grayscale equivalent"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))
    cmap = grayscale_cmap(cmap)
    grayscale = cmap(np.arange(cmap.N))
    fig, ax = plt.subplots(2, figsize=(6, 2), subplot_kw=dict(xticks=[], yticks=[]))
    ax[0].imshow([colors], extent=[0, 10, 0, 1])
    ax[1].imshow([grayscale], extent=[0, 10, 0, 1])
    plt.show()


# view_colormap('jet')
# view_colormap('viridis')
# view_colormap('RdBu')

# speckles = (np.random.random(I.shape) < 0.01)
# I[speckles] = np.random.normal(0, 3, np.count_nonzero(speckles))
# plt.figure(figsize=(10, 3.5))
# plt.subplot(1, 2, 1)
# plt.imshow(I, cmap='RdBu')
# plt.colorbar(extend='max')
# plt.subplot(1, 2, 2)
# plt.imshow(I, cmap='RdBu')
# plt.colorbar(extend='both')
# plt.clim(-1, 1)

# Discrete Colorbars

# plt.imshow(I, cmap=plt.cm.get_cmap('Blues', 12))  # 12 grades: 6 positive, 6 negative
# plt.colorbar(extend='both')
# plt.clim(-1, 1)

## Example: Handwritten Digits

digits = load_digits(n_class=10)  # Handwritten images of digits from sklearn
# print(digits)
# fig, ax = plt.subplots(8, 8, figsize=(16, 16))
# for i, axi in enumerate(ax.flat):
#     axi.imshow(digits.images[i], cmap='binary')
#     axi.set(xticks=[], yticks=[])

# project the digits into 2 dimensions using Isomap
iso = Isomap(n_components=2, n_neighbors=15)
projection = iso.fit_transform(digits.data)

# plot the results
plt.scatter(projection[:, 0], projection[:, 1], lw=0.1, c=digits.target, cmap=plt.cm.get_cmap('plasma', 10))
plt.colorbar(ticks=range(10), label='digit value')
plt.clim(-0.5, 10.5)

plt.show()
