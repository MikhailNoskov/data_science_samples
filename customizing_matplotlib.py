import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cycler

# plt.style.use('classic')

x = np.random.randn(1000)
# plt.hist(x)

# use a gray background
# fig = plt.figure(facecolor='white')
# ax = plt.axes(facecolor='#E6E6E6')
# ax.set_axisbelow(True)
#
# # draw solid white gridlines
# plt.grid(color='w', linestyle='solid')
#
# # hide axis spines
# for spine in ax.spines.values():
#     spine.set_visible(False)
#
# # hide top and right ticks
# ax.xaxis.tick_bottom()
# ax.yaxis.tick_left()
#
# # lighten ticks and labels
# ax.tick_params(colors='gray', direction='out')
# for tick in ax.get_xticklabels():
#     tick.set_color('gray')
# for tick in ax.get_yticklabels():
#     tick.set_color('gray')
#
# # control face and edge color of histogram
# ax.hist(x, edgecolor='#E6E6E6', color='#EE6666')

#Changing the Defaults: rcParams

colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('figure', facecolor='white')
plt.rc('axes', facecolor='#E6E6E6', edgecolor='none', axisbelow=True, grid=True, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')
plt.rc('xtick', direction='out', color='gray')
plt.rc('ytick', direction='out', color='gray')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)
# # plt.hist(x)
#
# for i in range(4):
#     plt.plot(np.random.rand(10))


def hist_and_lines():
    np.random.seed(0)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    ax[0].hist(np.random.randn(1000))
    for i in range(3):
        ax[1].plot(np.random.rand(10))
        ax[1].legend(['a', 'b', 'c'], loc='lower left')


with plt.style.context('ggplot'):
    hist_and_lines()

plt.show()
