import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')
fig = plt.figure()
# ax = plt.axes()

x = np.linspace(0, 10, 1000)
# ax.plot()  # Empty plot

# ax.plot(x, np.sin(x))

# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x))

# plt.plot(x, np.sin(x - 0), color='blue')  # specify color by name
# plt.plot(x, np.sin(x - 1), color='g')  # short color code (rgbcmyk)
# plt.plot(x, np.sin(x - 2), color='0.75')  # grayscale between 0 and 1
# plt.plot(x, np.sin(x - 3), color='#FFDD44')  # hex code (RRGGBB, 00 to FF)
# plt.plot(x, np.sin(x - 4), color=(1.0, 0.2, 0.3))  # RGB tuple, values 0 to 1
# plt.plot(x, np.sin(x - 5), color='chartreuse')  # HTML color names supported

# plt.plot(x, x + 0, linestyle='solid')
# plt.plot(x, x + 1, linestyle='dashed')
# plt.plot(x, x + 2, linestyle='dashdot')
# plt.plot(x, x + 3, linestyle='dotted')
#
# # For short, you can use the following codes:
#
# plt.plot(x, x + 4, linestyle='-')  # solid
# plt.plot(x, x + 5, linestyle='--')  # dashed
# plt.plot(x, x + 6, linestyle='-.')  # dashdot
# plt.plot(x, x + 7, linestyle=':')  # dotted

# plt.plot(x, x + 0, '-g')  # solid green
# plt.plot(x, x + 1, '--c')  # dashed cyan
# plt.plot(x, x + 2, '-.k')  # dashdot black
# plt.plot(x, x + 3, ':r')  # dotted red

# Adjusting the Plot: Axes Limits

# plt.plot(x, np.sin(x))
# # plt.xlim(-1, 11)
# # plt.ylim(-1.5, 1.5)
#
# plt.xlim(10, 0)  # Reversed axis
# plt.ylim(1.2, -1.2)
#
# # plt.axis('tight')  # Tighten the bounds around the current content
# plt.axis('equal')  # Equal x and y axis plotting. Other axis options include 'on', 'off', 'square', 'image'

# Labeling Plots

# plt.plot(x, np.sin(x))
# plt.title("A Sine Curve")
# plt.xlabel("x")
# plt.ylabel("sin(x)")

# plt.plot(x, np.sin(x), '-g', label='sin(x)')
# plt.plot(x, np.cos(x), ':b', label='cos(x)')
# plt.axis('equal')
# plt.legend()

# Object-oriented interface to plotting variant

ax = plt.axes()
ax.plot(x, np.sin(x))
ax.set(
    xlim=(0, 10),
    ylim=(-2, 2),
    xlabel='x',
    ylabel='sin(x)',
    title='A Simple Plot'
)

plt.show()
