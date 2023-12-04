import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('classic')

x = np.linspace(0, 10, 100)
# fig = plt.figure()
# plt.plot(x, np.sin(x), '-')
# plt.plot(x, np.cos(x), '--')
#
# fig.savefig('my_figure.png')

# MATLAB-style Interface

# plt.figure() # create a plot figure
# # create the first of two panels and set current axis
# plt.subplot(2, 1, 1) # (rows, columns, panel number)
# plt.plot(x, np.sin(x))
# # create the second panel and set current axis
# plt.subplot(2, 1, 2)
# plt.plot(x, np.cos(x), '--')
# # plt.show()

# Object-oriented interface

# First create a grid of plots
# ax will be an array of two Axes objects
fig, ax = plt.subplots(2)
# Call plot() method on the appropriate object
ax[0].plot(x, np.sin(x), '-')
ax[1].plot(x, np.cos(x), '--')
plt.show()