import matplotlib.pyplot as plt
from matplotlib.legend import Legend
import numpy as np
import pandas as pd

# plt.style.use('seaborn-whitegrid')
# x = np.linspace(0, 10, 1000)
# # fig, ax = plt.subplots()
# # ax.plot(x, np.sin(x), '-b', label='Sine')
# # ax.plot(x, np.cos(x), '--r', label='Cosine')
# # ax.axis('equal')
# # # ax.legend()
# # # ax.legend(loc='upper left', frameon=True)  # Legend to the left and with frame
# # # ax.legend(loc='lower center', ncol=2)  # Legend with two columns
# # ax.legend(frameon=True, fancybox=True, framealpha=1, shadow=True, borderpad=1)  # Rounded frame with a shadow
#
# # Choosing Elements for the Legend
#
# y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
# # lines = plt.plot(x, y)
# # # lines is a list of plt.Line2D instances
# # plt.legend(lines[:3], ['first', 'second', 'third'], frameon=True)
#
# plt.plot(x, y[:, 0], label='first')  # Specify explicitly the label in legend
# plt.plot(x, y[:, 1], label='second')
# plt.plot(x, y[:, 2:], label='others')
# plt.legend(frameon=True)
#
# plt.show()

# Multiple Legends

fig, ax = plt.subplots()
lines = []
styles = ['-', '--', '-.', ':']
x = np.linspace(0, 10, 1000)
for i in range(4):
    lines += ax.plot(x, np.sin(x - i * np.pi / 2), styles[i], color='black')
ax.axis('equal')
ax.legend(lines[:2], ['line A', 'line B'], loc='upper right')  # First legend
leg = Legend(ax, lines[2:], ['line C', 'line D'], loc='lower right')  # Second legend
ax.add_artist(leg)
plt.show()
